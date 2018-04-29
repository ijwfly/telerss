from django.conf import settings
from django.core.management.base import BaseCommand
from rss.bot import Bot


class Command(BaseCommand):
    help = 'start telerss client'

    def handle(self, *args, **options):
        bot = Bot(settings.API_ID, settings.API_HASH, settings.APP_NAME, settings.PHONE_NUMBER)
        bot.run()
