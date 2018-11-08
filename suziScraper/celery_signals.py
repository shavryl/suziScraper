from celery.signals import after_task_publish
from celery.signals import celeryd_after_setup


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
