
from celery import task
from django.core.management import call_command

@task
def delete_old_bookings():
    call_command('delete_old_bookings')