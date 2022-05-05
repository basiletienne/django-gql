from django.shortcuts import render
from django.http import JsonResponse, Http404


# Create your views here.
from .models import Message, Conversation
# from .serializers import MessageSerializer
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import mixins

# RetrieveUpdateDestroyAPIView = generics.RetrieveUpdateDestroyAPIView


# class MessageList(generics.ListCreateAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


# class MessageDetail(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):

#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#     def get_queryset(self):
#         conversation = Conversation.objects.get(pk=self.kwargs.get('conversation', None))
        
#         messages = Message.objects.filter(conversation=conversation.id)
#         return messages


#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# def message_send_view(request, *args, **kwargs):


# def conversation_view(request, conversation_id) :
#     data = {
#         'id' : conversation_id,
#         # "messages" : list(map(messages,messages.toJSON))
#     }
#     status = 200
#     try :
#         q_messages = Message.objects.filter(conversation = conversation_id)
#         # messages = [m.toJSON() for m in q_messages]
#         data['messages'] = q_messages
#     except :
#         print('404')
#         data['message'] = "Not Found"
#         status = 404

#     return JsonResponse(data, status = status)
