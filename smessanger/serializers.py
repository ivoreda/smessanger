from rest_framework.serializers import ModelSerializer
from .models import SlackMessage

class SlackMessageSerializer(ModelSerializer):
    class Meta:
        model = SlackMessage
        fields = ["RecordType", "Type","TypeCode","Name", "Tag",
                  "MessageStream","Description", "From", "Email", "BouncedAt",]
