from django.core.management.base import BaseCommand
from django.utils import timezone
from home.models import Booking

class Command(BaseCommand):
    help = 'Delete rows older than 7 days from the booking date'

    def handle(self, *args, **options):
        seven_days_ago = timezone.now() - timezone.timedelta(days=7)
        old_bookings = Booking.objects.filter(booking_date__lt=seven_days_ago)
        old_bookings.delete()
        self.stdout.write(self.style.SUCCESS('Deleted old bookings.'))