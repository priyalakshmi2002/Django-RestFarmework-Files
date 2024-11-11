# from django.test import TestCase
# from .models import Category, Products
# from .factories import CategoryFactory, ProductsFactory

# class ModelTest(TestCase):
#     def test_product_creation(self):
#         category = CategoryFactory()  # Using Factory Boy to create a category
#         product = ProductsFactory(category_reference=category)
#         self.assertEqual(product.category_reference, category)
#         self.assertTrue(product.product_name)
#         self.assertTrue(product.code)
#         self.assertGreater(product.price,0)

#     def test_category_creation(self):
#         category = CategoryFactory()
#         self.assertTrue(category.category_name)

## tests.py  example for fixtures
# from django.test import TestCase
# from .models import Book

# class BookTestCase(TestCase):
#     fixtures = ['books.json']  # Specify the fixture file to load before tests

#     def test_books_loaded(self):
#         # Test if the books from the fixture are correctly loaded
#         book1 = Book.objects.get(pk=1)
#         book2 = Book.objects.get(pk=2)
#         self.assertEqual(book1.title, 'Django for Beginners')
#         self.assertEqual(book2.title, 'Two Scoops of Django')

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Products, Category
from .factories import CategoryFactory, ProductsFactory
from django.contrib.auth.models import User
from unittest.mock import patch


class CategoryViewSetTest(APITestCase):
    
    def setUp(self):
        # Creating a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username=self.user.username, password='testpassword')

        # Using the factory to create a category
        self.category_data = CategoryFactory() #Computer -> #fOOD
        # self.category_data = {
        #     'category_name': self.category.category_name,
        # }

    # Test for post
    def test_create_category(self):
        url = reverse('category-list')
        response = self.client.post(url, self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
       # self.assertEqual(response.data['result']['name'], category_data.name)
        # self.assertEqual()

    # Test for invalid input
    def test_create_category_invalid(self):
        invalid_data = self.category_data.copy()    
        invalid_data['category_name'] = ''  # Invalid data (empty category name)
        url = reverse('category-list')
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # Test for delete
    def test_delete_category(self):
        url = reverse('category-detail', kwargs={'pk': self.category.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Deleted")
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())
        

class ProductsViewSetTest(APITestCase):

    def setUp(self):
        # Creating a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username=self.user.username, password='testpassword')

        # Using the factory to create a product and a category
        self.category = CategoryFactory()
        self.product = ProductsFactory(category_reference=self.category)
        self.product_data = {
            'product_name': self.product.product_name,
            'code': self.product.code,
            'price': self.product.price,
            'category_reference': self.category.id
        }

    # Test for post
    def test_create_product(self):  
        url = reverse('products-list')
        response = self.client.post(url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Data Saved")

    # Test for patch or put
    def test_partial_update_product(self):
        url = reverse('products-detail', kwargs={'pk': self.product.id})
        updated_data = {'price': 999}  # Updated price
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Updated")
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, updated_data['price'])

    # Test for invalid input
    def test_create_product_invalid(self):
        invalid_data = self.product_data.copy()
        invalid_data['product_name'] = ''  # Invalid data (empty name)
        url = reverse('products-list')
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test for get
    def test_get_products_list(self):
        url = reverse('products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Products.objects.count())

    # Test for delete
    def test_delete_products(self):
        url = reverse('products-detail', kwargs={'pk': self.product.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Products.objects.filter(id=self.product.id).exists())




