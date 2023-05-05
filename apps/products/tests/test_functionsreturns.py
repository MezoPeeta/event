from django.test import TestCase 
from apps.products.models import Products, Customer

class TestingRetruns(TestCase):
    def test_products(self):
        self.product = Products.objects.create(price=200)
        self.assertEquals(self.product.name, "Product Name")


    def test_customers(self):
        self.customer1 = Customer.objects.create(name='testcustomer', device='testdevice')
        self.assertEquals(self.customer1.name, "testcustomer")
        self.customer2 = Customer.objects.create(device='testdevice2')
        self.assertEquals(str(self.customer2), "testdevice2")
        