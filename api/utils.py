import gzip
import tarfile
from tqdm import tqdm # pip3 install tqdm


def decompress(infile, path, members=None):
    """
    Extracts `gzip_file` and put into `path`.
    If members is None, all members on `gzip_file` will be extracted.
    """
    with open(infile, 'rb') as inf, open(path, 'w', encoding='utf8') as tof:
        decom_str = gzip.decompress(inf.read()).decode('utf-8')
        tof.write(decom_str)
