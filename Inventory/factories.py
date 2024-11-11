import factory
from faker import Faker
from Inventory.models import Products, Category

faker = Faker()

class CategoryFactory(factory.DictFactory):
    # class Meta:
    #     model = Category
    category_name = factory.Faker('word')


class ProductsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Products
    product_name = factory.Faker('word')
    code = factory.Faker('ean8')  # Generates a random 8-digit barcode
    price = factory.Faker('random_number', digits=3)  # Adjust as per your need
    category_reference = factory.SubFactory(CategoryFactory)
    