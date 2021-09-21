import factory
from faker import Faker
from factory.django import DjangoModelFactory
from .models import User

faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = ""
    email = factory.Faker('email')
    password = factory.PostGenerationMethodCall('set_password', faker.password())
