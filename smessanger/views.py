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
            # message = models.SlackMessage.objects.create(
            #     RecordType = serializer.data.get('RecordType'),
            #     Type = serializer.data.get('Type'),
            #     TypeCode = serializer.data.get('TypeCode'),
            #     Name = serializer.data.get('Name'),
            #     Tag = serializer.data.get('Tag'),
            #     MessageStream = serializer.data.get('MessageStream'),
            #     Description = serializer.data.get('Description'),
            #     From = serializer.data.get('From'),
            #     Email = serializer.data.get('Email'))

            # payload = models.SlackMessage.objects.last().__dict__
            # new_payload = payload.pop('_state', 'id')
            print("#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%")
            print(message)
            print("#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%#$%")


            client = WebClient(token="xoxp-2662551942742-2666298219765-4924786785060-71aa4576034942fbc1452c0a3a527df8")
            logger = logging.getLogger(__name__)
            channel_id = "C04T4A8NEPL"

            try:
                if message['Type'] == 'SpamNotification':

                    result = client.chat_postMessage(
                        channel=channel_id,
                        text=f"{message}"
                        # You could also use a blocks[] array to send richer content
                    )
                    # Print result, which includes information about the message (like TS)
                    print(result)

                    return Response({'status':True,
                            'message':'Message sent successfully'})
                else:
                    return Response({'status':False,
                                'message':'Message sending unsuccessful. Can only send messages of type SpamNotification'})


            except SlackApiError as e:
                print(f"Error: {e}")
                return Response({'status':True,
                                'message':'Message sending unsuccessful'})