from store.models import Product
from faker import Faker
faker = Faker()

for _ in range(10):
    Product.objects.create(name=faker.sentence(), price=99.99, digital=faker.boolean())

#python3 manage.py shell < script.py