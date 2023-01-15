from datetime import timedelta
from dockproject.celery import Celery
from celery.schedules import crontab
# from celery.task.base import PeriodicTask
from dockproject.celery import app
from celery import shared_task




# @shared_task

@shared_task(name='add')
def add(x, y):
    return x + y

# celery -A dockproject worker --loglevel=INFO

# class DailyPolicyExpirationReminder(PeriodicTask):
#     # run_every = timedelta(days=1)
#     run_every = timedelta(seconds=2)

#     def run(self, *args, **kwargs):
#         print('CELERY WORKER WORKING')