import graphene
from chat.pm.schema import GetChat, ChatMutation


class Query(GetChat, graphene.ObjectType):
    pass


class Mutation(ChatMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
