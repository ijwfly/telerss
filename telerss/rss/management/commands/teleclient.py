from django.core.management.base import BaseCommand
from rss.bot import Bot


class Command(BaseCommand):
    help = 'start telerss client'

    def handle(self, *args, **options):
        bot = Bot()
        bot.run()
