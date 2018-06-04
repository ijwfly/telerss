from django.contrib.syndication.views import Feed
from django.urls import reverse

from rss.models import TelegramChannel, ChannelMessage


FEED_LENGTH = 100
ITEM_TITLE_LENGTH = 30


class ChannelMessageFeed(Feed):
    def get_object(self, request, channel_id, message_id=None):
        return TelegramChannel.objects.filter(chat_id=channel_id).first()

    def title(self, obj):
        return obj.title

    def link(self, obj):
        if isinstance(obj, TelegramChannel):
            return reverse('channel-item', args=[obj.chat_id])
        elif isinstance(obj, ChannelMessage):
            return reverse('message-item', args=[obj.channel.chat_id, obj.message_id])

    def description(self, obj):
        return obj.title

    def items(self, obj):
        return ChannelMessage.objects.filter(channel=obj).order_by('-creation_time')[:FEED_LENGTH]

    def item_link(self, item):
        return reverse('message-item', args=[item.channel.chat_id, item.message_id])

    def item_title(self, item):
        return item.raw_text[:ITEM_TITLE_LENGTH]

    def item_description(self, item):
        return item.raw_text


# # class MessageFeed(Feed):
#     def item_title(self, item):
#         return item.raw_text[:100]
#
#     def
#