from telethon import TelegramClient, events


class Bot(object):
    def __init__(self, api_id, api_hash, app_name, phone_number):
        self.client = TelegramClient(app_name, api_id, api_hash, update_workers=1, spawn_read_thread=False)
        self.client.start(phone=phone_number)

        self.client.add_event_handler(Bot.handle_channel_message, events.NewMessage)

    @staticmethod
    def handle_channel_message(event):
        print(event)

    def run(self):
        self.client.idle()
