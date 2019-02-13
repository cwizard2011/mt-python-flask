import graphene
import api.users.schema
import api.requests.schema


class Query(
    api.requests.schema.Query
):
    pass


class Mutation(
    api.users.schema.Mutation,
    api.requests.schema.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
