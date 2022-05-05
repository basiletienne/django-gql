# from rest_framework import serializers

# from .models import Message, Conversation


# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = [
#             'pk', #private key
#             'message',
#             'date',
#             'conversation',
#             # 'seen',
#             'sender']
#         extra_kwargs = {
#             # "seen" : {"required": False}
#         }

#     def validate_content(self, value):
#         if len(value) > 500:
#             raise serializers.ValidationError('Your message is too long')
