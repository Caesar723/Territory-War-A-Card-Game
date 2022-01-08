#from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from first import consumers

    
websocket_urlpatterns=[re_path(r'wss/(?P<group>\w+)/$',consumers.ChatConsumer.as_asgi()),]