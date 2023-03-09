from django.shortcuts import render
from . import models
# Create your views here.


from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from . import serializers


import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SendSlackSpamMessageView(CreateAPIView):
    serializer_class = serializers.SlackMessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = serializer.data

            client = WebClient(token="xoxp-2662551942742-2666298219765-4924786785060-71aa4576034942fbc1452c0a3a527df8")
            logger = logging.getLogger(__name__)
            channel_id = "C04T4A8NEPL"

            try:
                if message['Type'] == 'SpamNotification':

                    result = client.chat_postMessage(
                        channel=channel_id,
                        text=f"{message}"
                        )
                    return Response({'status':True,
                            'message':'Message sent successfully'})
                else:
                    return Response({'status':False,
                                'message':'Message sending unsuccessful. Can only send messages of type SpamNotification'})

            except SlackApiError as e:
                print(f"Error: {e}")
                return Response({'status':False,
                                'message':'Message sending unsuccessful'})