from graphQl import schema
import graphene


class Query(graphene.ObjectType, schema.Query):
    pass


schema = graphene.Schema(query=Query)
