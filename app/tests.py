"""

Author: Thomas Scelsi
Email: tlscelsi@gmail.com

This file covers the testing of graphql query endpoints. 
It is inspired somewhat from the graphene-django test suite found at:
https://github.com/graphql-python/graphene-django/blob/master/graphene_django/tests/test_query.py

"""

from django.test import TestCase
from app.schema import schema
from app.models import Address, Person

class SimpleTestCase(TestCase):
    def setUp(self) -> None:
        # create entry in test database
        a1 = Address.objects.create(number=47,street="Magnolia Court",city="Melbourne",state="VIC")
        p1 = Person.objects.create(name="Thomas Scelsi",email="tlscelsi@gmail.com",address=a1)
        return super().setUp()

    def test_should_return_correct_user_info(self):
        query = '''
            query {
                person {
                    email
                    name
                    address {
                    number
                    street
                    city
                    state
                    }
                }
            }
        '''
        result = schema.execute(query)
        # we check to see if there are any status code errors
        assert not result.errors
        # let's make sure that the information contained in the query response is as expected.
        expected = {
            "person": {
                "name": "Thomas Scelsi",
                "email": "tlscelsi@gmail.com",
                "address": {
                    "number": 47,
                    "street": "Magnolia Court",
                    "city": "Melbourne",
                    "state": "VIC"
                }
            }
        }
        assert result.data == expected, str(result.data)
        
        
        
