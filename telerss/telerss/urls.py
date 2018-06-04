"""telerss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter

from rss.views import ChannelMessageFeed


class SignedIntConverter(object):
    regex = '-*[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(SignedIntConverter, 'sint')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('channels/<sint:channel_id>/rss/', ChannelMessageFeed(), name='channel-item'),
    path('channels/<sint:channel_id>/rss/<int:message_id>', ChannelMessageFeed(), name='message-item'),
]
