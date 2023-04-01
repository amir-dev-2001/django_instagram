# from celery import app
from time import sleep
from celery import shared_task, app
from django.contrib.auth import get_user_model
# from celery.task import periodic_task
from celery.schedules import crontab
from django.utils import timezone

User = get_user_model()

# @app.task(name='send verification code')
@shared_task
def send_verification_code(username):
    # TODO: send verification code
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    sleep(10)
    return "phone number received of user: {}".format(user.username)

# TODO: add periodic task
# @periodic_task(name='time pinger', run_every=crontab(minute='*'))
# def minute_pinger():
    # return "time: {}".format(timezone.now())
