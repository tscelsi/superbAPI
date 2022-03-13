"""

Here we convert our Django database models into GraphQL fields such that they can be queried at the '/graphql' endpoint.

"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Person, Address

# here we make each Django Model compatible as a GraphQL field.
class PersonType(DjangoObjectType):
    class Meta:
        model=Person
        fields="__all__"

class AddressType(DjangoObjectType):
    class Meta:
        model=Address
        fields="__all__"

class Query(graphene.ObjectType):
    """This class describes the logic for the '/graphql' API endpoint. It simply returns the only entry in the database back
    as a PersonType
    """
    person = graphene.Field(PersonType)

    def resolve_person(root, info):
        # here we just default return the only entry in our database right now. Me!
        person = Person.objects.get()
        return PersonType(email=person.email, name=person.name, address=person.address)

# we define our schema here and reference it in other files
schema = graphene.Schema(query=Query)