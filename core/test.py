from    django.test import TestCase
from .models import Category

class ModelTesting(TestCase):

    def setUp(self):
        self.prod= Category.objects.create(cid='abcdefgh12345', title='django', image='category.jpg')

    def test_cat_model(self):
        d=self.prod
        self.assertTrue(isinstance(d, Category))