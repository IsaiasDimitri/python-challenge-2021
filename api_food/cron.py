from django.core import management
import logging

logger = logging.getLogger(__name__)

def feed_db_once_per_day():
    logger.info('Starting feeding DB...')
    management.call_command('feed_db')
