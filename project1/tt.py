import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'project1.settings')
import django
django.setup()
from firstapp.models import jaipurjobs
from faker import Faker
def populate(n):
    fake=Faker('hi_IN')
    for i in range(n):
        fname=fake.name()
        jaipurjobs=jaipurjobs.objects.get_or_create(company=fname)

populate(25)
