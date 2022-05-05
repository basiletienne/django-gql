import graphene


from graphene_django import DjangoObjectType
from django.db.models import Max

from .models import Message, Conversation



class ConversationType(DjangoObjectType):
    class Meta:
        model = Conversation
        fields = ("id", "user1", "user2")


class MessageType(DjangoObjectType):
    max_id = graphene.Int(required=False)

    class Meta:
        model = Message
        fields = ("id", "message", "date", "sender", "conversation")


class Query(graphene.ObjectType):
    all_Messages = graphene.List(MessageType)  # query
    all_Messages_by_Conversation = graphene.List(
        MessageType, conversation=graphene.String(required=True))
    all_Conversation_Previews = graphene.List(MessageType)

    def resolve_all_Messages(root, info):  # resolve the query
        return Message.objects.all()

    def resolve_all_Messages_by_Conversation(root, info, conversation):
        try:
            msg = Message.objects.filter(conversation=conversation)
            return msg
        except Message.DoesNotExist:
            return None

    def resolve_all_Conversation_Previews(root, info):
        qs = Message.objects.values('conversation').annotate(max_id=Max('id'))
        ids = qs.values_list('max_id', flat=True)
        conversation_previews = Message.objects.filter(pk__in=set(ids))
        return conversation_previews


class MessageMutation(graphene.Mutation):
    class Arguments:
        message = graphene.String(required=True)
        sender = graphene.String(required=True)
        user1 = graphene.String(required=True)
        user2 = graphene.String(required=True)
        id = graphene.String(required=True)

    message = graphene.Field(MessageType)

    @classmethod
    def mutate(cls, root, info, message, sender, id, user1, user2):
        if user1 == user2:
            raise "Can't send a message to yourself"
        try:
            conversation = Conversation.objects.get(id=id)
        except:
            conversation = Conversation(user1=user1, user2=user2)
            conversation.save()
        message = Message(message=message, sender=sender,
                          conversation=conversation)
        message.save()
        return MessageMutation(message=message)


class ConversationMutation(graphene.Mutation):
    class Arguments:
        user1 = graphene.String(required=True)
        user2 = graphene.String(required=True)

    conversation = graphene.Field(ConversationType)

    @classmethod
    def mutate(cls, root, info, user1, user2):
        conversation = Conversation(user1=user1, user2=user2)
        conversation.save()
        print(conversation)
        return ConversationMutation(conversation=conversation)


class Mutation(graphene.ObjectType):
    add_message = MessageMutation.Field()
    add_conversation = ConversationMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
