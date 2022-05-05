import graphene

import conversations.schema
import users.schema



class Query(conversations.schema.Query, users.schema.Query,  graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(conversations.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
