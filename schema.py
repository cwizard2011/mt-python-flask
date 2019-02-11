import graphene
import api.users.schema
import api.requests.schema


class Mutation(
    api.users.schema.Mutation,
    api.requests.schema.Mutation
):
    pass


schema = graphene.Schema(mutation=Mutation)
