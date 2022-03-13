import graphene
from graphene_django import DjangoObjectType
from app.models import Person, Address

class PersonType(DjangoObjectType):
    class Meta:
        model=Person
        fields="__all__"

class AddressType(DjangoObjectType):
    class Meta:
        model=Address
        fields="__all__"

class Query(graphene.ObjectType):
    person = graphene.Field(PersonType)

    def resolve_person(root, info):
        # here we just default return the only entry in our database right now. Me!
        person = Person.objects.get()
        return PersonType(email=person.email, name=person.name, address=person.address)

schema = graphene.Schema(query=Query)