
import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecomsite.settings")
django.setup()
from django_seed import Seed

seeder = Seed.seeder()

from .models import Product

seeder.add_entity(Product, 2)

inserted_pks = seeder.execute()