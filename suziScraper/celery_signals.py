from celery.signals import after_task_publish
from celery.signals import celeryd_after_setup
from celery.signals import celeryd_init


@after_task_publish.connect(sender='suziScraper.tasks.add')
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(info=info,))


@celeryd_after_setup.connect
def setup_direct_queue(sender, instance, **kwargs):
    # sender is the nodename of the worker
    queue_name = '{0}.dq'.format(sender)
    instance.app.amqp.queues.select_add(queue_name)


@celeryd_init.connect(sender='worker12@example.com')
def configure_worker12(conf=None, **kwargs):
    conf.task_default_rate_limit = '10/m'


@celeryd_init.connect
def configure_workers(sender=None, conf=None, **kwargs):
    if sender in ('worker1@example.com', 'worker2@example.com'):
        conf.task_default_rate_limit = '10/m'
    if sender == 'worker3@example.com':
        conf.worker_prefetch_multiplier = 0
