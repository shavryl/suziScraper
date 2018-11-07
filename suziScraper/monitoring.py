from pprint import pformat
from celery.events.snapshot import Polaroid
from suziScraper.celeryapp import app


class DumpCam(Polaroid):
    clear_after = True

    def on_shutter(self, state):
        if not state.event_count:
            return
        print('Workers: {0}'.format(pformat(state.workers, indent=4)))
        print('Tasks: {0}'.format(pformat(state.tasks, indent=4)))
        print('Total: {0.event_count} events, {0.task_count} tasks'.format(state))


def my_monitor(app):
    state = app.events.State()

    def announce_failed_tasks(event):
        state.event(event)
        task = state.tasks.get(event['uuid'])

        print('TASK FAILED: %s[%s] %s' % (
            task.name, task.uuid, task.info(),))

    with app.connection() as connection:
        recv = app.events.Receiver(connection, handlers={
            'task-failed': announce_failed_tasks,
            '*': state.event,
        })
        recv.capture(limit=None, timeout=None, wakeup=True)


my_monitor(app)
