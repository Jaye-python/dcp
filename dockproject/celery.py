
# from __future__ import absolute_import
# import os

# from django.conf import settings

# from celery import Celery

# settings_file = 'local' if os.environ.get('IS_LOCAL') else 'production'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c2s.settings." + settings_file)

# app = Celery('c2s', broker=settings.BROKER_URL)
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


from datetime import timedelta
import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dockproject.settings')

app = Celery('dockproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# ? Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
#     # sender.add_periodic_task(
#     #     crontab(minute=0, hour=0),  # Calls every midnight
#     #     task_generate_next_premiums.s(),
#     # )
#     # sender.add_periodic_task(
#     #     crontab(minute=0, hour=0),  # Calls every midnight
#     #     task_collect_debit_orders.s(),
#     # )
    sender.add_periodic_task(2.0, g.s('Get it done'),
    )
    
#  TODO: Add
@app.task
def g(arg):
    """
    ? thus This is a simple task that returns a string."""
    
    # return 'Get it done'
    print(arg) # ? this is done before now

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'add': {                        #specified in decorator
        'task': 'add',
        'schedule': 10.0,
        'args': (16, 16)
    },
}

app.conf.timezone = 'UTC'
