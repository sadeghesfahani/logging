from django.core.management import BaseCommand
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Send email to user'

    def handle(self, *args, **options):
        send_mail("test command", "this is a test command", "tracking@leadpaka.de", ["sadeghesfahani.sina@gmail.com"], )
        print('Hello World')
