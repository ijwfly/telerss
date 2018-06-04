from telethon import TelegramClient, events
from django.conf import settings

from rss.models import TelegramChannel, ChannelMessage


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


class Bot(object):
    def __init__(self):
        api_id = settings.API_ID
        api_hash = settings.API_HASH
        app_name = settings.APP_NAME
        phone_number = settings.PHONE_NUMBER
        self.client = TelegramClient(app_name, api_id, api_hash, update_workers=1, spawn_read_thread=False)
        self.client.start(phone=phone_number)

    @staticmethod
    def handle_incoming_message(event):
        if event.is_channel:
            Bot.handle_channel_message(event)
        else:
            # TODO: можно добавить функционал по добавлению лент через бота
            pass

    @staticmethod
    def handle_channel_message(event):
        print(event.raw_text)
        chat_id = event.chat_id
        title = event.chat.title
        channel = TelegramChannel.objects.filter(chat_id=chat_id).first()
        if not channel:
            channel = TelegramChannel.objects.create(chat_id=chat_id, title=title)
            print('new channel!')
        message_id = event.message.id
        raw_text = event.raw_text
        ChannelMessage.objects.create(channel=channel, message_id=message_id, raw_text=raw_text)
        print('[{}] {}:\n{}'.format(chat_id, title, raw_text))

    def run(self):
        self.client.add_event_handler(Bot.handle_incoming_message, events.NewMessage(incoming=True))
        print('connecting...')
        self.client.idle()

