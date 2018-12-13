import graphene
import api.users.schema


class Mutation(
    api.users.schema.Mutation
):
    pass


schema = graphene.Schema(mutation=Mutation)
