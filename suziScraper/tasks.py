from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task()
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@shared_task(bind=True, autoretry_for=(NameError,),
             retry_kwargs={'max_retries': 5})  # retry in 30 minutes.
def ask_exc(self, x, y):
    try:
        # to get exception for retries
        something_raising()
    except Exception as exc:
        # overrides the default delay to retry after 1 minute
        raise self.retry(exc=exc, countdown=30)


@shared_task
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
