import os

from celery import Celery

# from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dms.settings.dev")

# Get the base REDIS URL, default to redis' default
CELERY_BROKER = os.environ.get("CELERY_BROKER", "redis://platform-redis:6379/0")

app = Celery("dms", broker=CELERY_BROKER)

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"

app.conf.beat_schedule = {
    # here add tasks schedule configuration
}
