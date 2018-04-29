from django.core.management import call_command
from django.test import TestCase


class TeleClientTest(TestCase):
    def test_run(self):
        args = []
        opts = {}
        call_command('teleclient', *args, **opts)