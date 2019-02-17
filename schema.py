import graphene
import api.users.schema
import api.requests.schema
import api.requests.schema_admin


class Query(
    api.requests.schema.Query,
    api.requests.schema_admin.Query
):
    pass


class Mutation(
    api.users.schema.Mutation,
    api.requests.schema.Mutation,
    api.requests.schema_admin.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
