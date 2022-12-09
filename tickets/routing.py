from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/tickets/(?P<room_name>\w+)/$", consumers.TicketsConsumer.as_asgi()),
]