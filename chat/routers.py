from django.urls import re_path
from chat import consumers


websocket_urlpatterns = [
    # consumers.ChatConsumer is the synchronous version of the consumer.
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.AsyncChatConsumer.as_asgi()),
]
