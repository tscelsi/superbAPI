from django.db import models

class Address(models.Model):
    number = models.IntegerField()
    # We'll use a TextField for all our text-based attributes. This doesn't enforce any
    # max length constraints in the DB.
    street = models.TextField()
    city = models.TextField()
    # let's make it so that we're only dealing with Australian states
    state = models.CharField(
        max_length=3,
        choices=[
            ("VIC", "Victoria"), 
            ("NSW", "New South Wales"), 
            ("QLD", "Queensland"), 
            ("TAS", "Tasmania"), 
            ("WA", "Western Australia"), 
            ("NT", "Northern Territory"), 
            ("SA", "South Australia")
        ])


class Person(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.TextField()
    # here we link an address to a person. If we remove the address, then we set the address of the 
    # person to null.
    address = models.ForeignKey(Address, related_name="person", on_delete=models.SET_NULL, null=True)