from django.db import models
# Create your models here.
import json

import datetime


# def json_default(value):
#     if isinstance(value, datetime.timezone) :
#         print(value)
#         return dict(tzoffset = value.utcoffset)
#     if isinstance(value, datetime.datetime):
#         print('datetime')
#         return dict(year=value.year, month=value.month, day=value.day, hour = value.hour, minute=value.minute, second= value.second, microsecond = value.microsecond)
#     else:
#         return value.__dict__

class Conversation(models.Model):
    user1 = models.CharField(max_length=30)
    user2 = models.CharField(max_length=30)  # (userId, username)

    def __str__(self):
        return self.user1+', '+self.user2


class Message(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(
        to=Conversation, on_delete=models.CASCADE, related_name="conversation")

    sender = models.CharField(
        max_length=10)

    def __str__(self):
        return self.message
    # def toJSON(self):
    #     return json.dumps(self, default=json_default,
    #         sort_keys=True, indent=4)
