from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from products.models import Products
from utils.selenium_test import TestUtils

class Test_Searching(LiveServerTestCase, TestUtils):
    def setUp(self):
        self.product_name = "calculator"
        Products.objects.create(name=self.product_name, price=10)
        Products.objects.create(name=self.product_name + "sadahkl", price=10)
        self.browser = self.init_selenium()
        self.store = self.live_server_url + "/en/store/"

        self.browser.get(self.store)

        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.search_bar = self.browser.find_element(By.XPATH, '//*[@id="search_box"]')
        self.search_bar.send_keys(self.product_name)

    def test_search_bar(self):
        self.assertEquals(self.search_bar.get_attribute("value"), self.product_name)

    def test_searching(self):
        self.search_button = self.browser.find_element(
            By.XPATH, '//*[@id="search-bar"]'
        )
        self.search_button.click()
        url = self.browser.current_url
        
        search_query_is_in_url = f"?search_query={self.product_name}" in url
        self.assertTrue(search_query_is_in_url)

