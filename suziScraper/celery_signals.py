from celery.signals import after_task_publish


@after_task_publish.connect(sender='suziScraper.tasks.add')
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(info=info,))
