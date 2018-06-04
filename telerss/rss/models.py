from django.db import models
from django.db.models import CASCADE
from django.utils.timezone import now


class TelegramChannel(models.Model):
    chat_id = models.CharField(verbose_name="идентификатор канала", max_length=50)
    title = models.CharField(verbose_name="название канала", max_length=500)


class ChannelMessage(models.Model):
    channel = models.ForeignKey(TelegramChannel, on_delete=CASCADE)
    message_id = models.CharField(verbose_name="идентификатор сообщения", max_length=50)
    raw_text = models.TextField(verbose_name="текст сообщения")
    creation_time = models.DateTimeField(verbose_name="время создания", default=now)

    def __str__(self):
        return self.raw_text
