from django.db import models

# Create your models here.
class SlackMessage(models.Model):
    RecordType = models.CharField(max_length=255)
    Type = models.CharField(max_length=255)
    TypeCode = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Tag = models.CharField(max_length=255)
    MessageStream = models.CharField(max_length=255)
    Description = models.TextField()
    From = models.EmailField()
    Email = models.EmailField()
    BouncedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name