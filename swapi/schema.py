import graphene

from app.schema import Mutation as sw_mutation
from app.schema import Query as sw_query


class Query(sw_query):
    pass


class Mutation(sw_mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
