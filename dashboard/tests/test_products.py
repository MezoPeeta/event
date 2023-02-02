from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from products.models import Products

from django.urls import reverse
from utils.selenium_test import TestUtils



class TestProduct(LiveServerTestCase, TestUtils):
    def setUp(self):
        self.browser = self.selenium_admin_login()


    def test_product(self):
        self.user.profile.committee = "PR"
        self.user.profile.save()
        self.browser.get(self.live_server_url + "/en/new/product")
        products_price = self.browser.find_element(By.XPATH, '//*[@id="id_price"]')
        products_price.send_keys(10)
        element = self.browser.find_element(By.ID, "ftco-loader")
        self.browser.execute_script("arguments[0].style.visibility='hidden'", element)

        btn = self.browser.find_element(By.TAG_NAME, "button")
        btn.click()

        is_product_uploaded = True if Products.objects.get(price=10) else False
        store_page = self.live_server_url + reverse("Store")
        self.assertTrue(is_product_uploaded)

        self.assertEqual(self.browser.current_url, store_page)
