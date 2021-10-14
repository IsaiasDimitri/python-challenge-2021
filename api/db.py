from gzip import compress, decompress
import json
import logging
import os
import time
import math
import requests
import tempfile
import tarfile
import json
from tqdm import tqdm
from django.conf import settings
from api import utils
from api.models import Product

logger = logging.getLogger(__name__)


class DatabaseManager:
    """
    Manage dumps download / load in database.
    """

    INDEXES = settings.INDEXES
    DUMP_URL = settings.DUMP_URL

    # INDEXES = "https://challenges.coode.sh/food/data/json/index.txt"
    # DUMP_URL = "https://challenges.coode.sh/food/data/json/"

    def download_file(self, url, filename):
        """
        Download a file
        """
        response = requests.get(url, stream=True)

        block_size = 1024
        total_size = int(response.headers.get("content-length", 0))

        path = os.path.join(f"{settings.BASE_DIR}/tmp/", filename)
        with open(path, "wb") as outfile:
            iterator = tqdm(
                response.iter_content(block_size),
                total=math.ceil(total_size // block_size),
                unit="KB",
                unit_scale=True,
            )
            for chunk in iterator:
                outfile.write(chunk)

        return path

    def download_compressed_file(self, url, filename):
        path = os.path.join(f"{settings.BASE_DIR}/tmp/", filename)
        with requests.get(url, stream=True) as File:
            block_size = 1024
            total_size = int(File.headers.get("content-length", 0))
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                with open(tmp_file.name, "wb") as fd:
                    iterator = tqdm(
                        File.iter_content(block_size),
                        total=math.ceil(total_size // block_size),
                        unit="KB",
                        unit_scale=True,
                    )
                    for chunk in iterator:
                        fd.write(chunk)
            utils.decompress(tmp_file.name, path)

        return path

    def download_indexes(self):
        """
        Download indexes txt and return its path
        """
        indexes = self.download_file(self.INDEXES, "indexes.txt")

        return indexes

    def load_dump(self):
        """
        Download, parse and load latest dump in DB
        """
        all_count = 0
        new_count = 0
        upd_count = 0
        err_count = 0

        # Download JSON
        try:
            indexes = self.download_indexes()
        except Exception as e:
            logger.error(e)
            logger.error("[DATABASE] - An error occurred during indexes download")
            return

        counter = 0
        with open(indexes, "r") as file:
            for line in file:
                line = line.rstrip()
                url = self.DUMP_URL + line
                logger.info("[DATABASE] - Starting dump download...")
                timestamp = time.time()
                logger.info("[DATABASE] Downloading %s ..." % (url))
                dump_file = self.download_compressed_file(url, line[:-3])
                logger.info(
                    "[DATABASE] - Dump n°%s downloaded in %ss"
                    % (counter, int(time.time() - timestamp))
                )
                counter += 1

                logger.info("[DATABASE] - opening %s and saving to DB..." % (dump_file))
                with open(dump_file, "r") as file:
                    file.seek(0)

                    # Preload last_modified values
                    last_modified_map = dict(
                        Product.objects.all().values_list("code", "last_modified_t")
                    )

                    # Parse JSON
                    with open(dump_file, "r") as file:
                        for e in file:
                            entry = json.loads(e)
                            code = entry.get("code", "")
                            if code == "":
                                continue

                            all_count += 1

                            saved_last_modified = last_modified_map.get(code)
                            try:
                                if saved_last_modified is None:
                                    Product.load(data=entry, create=True)
                                    new_count += 1
                                elif (
                                    int(entry.get("last_modified_t"))
                                    > saved_last_modified
                                ):
                                    Product.load(data=entry)
                                    upd_count += 1
                            except Exception as e:
                                logger.exception(e)
                                err_count += 1
                                continue

                            if all_count != 0 and all_count % 50000 == 0:
                                logger.info(
                                    "[DATABASE] - %s products parsed, %s created, %s updated, %s errors"
                                    % (all_count, new_count, upd_count, err_count)
                                )

            os.remove(dump_file)  # removing dump
        logger.info("[DATABASE] - load_dump done")
