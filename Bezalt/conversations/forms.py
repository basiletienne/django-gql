from django import forms

# from .models import Conversation

class CreateNewMessage(forms.Form) :
    message = forms.TextField()
    date = forms.DateTimeField(auto_now_add=True)
    # conversation = forms.ForeignKey(
    #     to=Conversation, on_delete=models.CASCADE, related_name="conversation")

    sender = forms.CharField(
        choices=[('1', 'user1'), ('2', 'user2')], max_length=10)
