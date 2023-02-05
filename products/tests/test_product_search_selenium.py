from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from products.models import Products
from utils.selenium_test import TestUtils
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time


class Test_Searching(LiveServerTestCase, TestUtils):
    def setUp(self):
        self.product_name = "calculator"
        Products.objects.create(name=self.product_name, price=10)
        Products.objects.create(name=self.product_name + "sadahkl", price=10)
        self.browser = self.init_selenium()
        self.store = self.live_server_url + "/en/store/"

        self.browser.get(self.store)

        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="search_box"]'))
        )
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
        search_query_is_in_url = f"?q={self.product_name}" in url
        self.assertTrue(search_query_is_in_url)

    # def test_search_products(self):
    #     search_query_is_in_product_names = True
    #     products = self.browser.find_elements(
    #         By.XPATH, "//*[contains(text(), 'View Product')]"
    #     )
    #     ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

    #     wait = WebDriverWait(self.browser, 10, ignored_exceptions  = ignored_exceptions)
    #     products = self.browser.find_elements(By.XPATH, "//*[contains(text(), 'View Product')]")

        
    #     # wait = WebDriverWait(self.browser, 10,ignored_exceptions=ignored_exceptions).until(
    #     #     EC.element_to_be_clickable(i)
    #     #     )

    #     for i in products:
    #         # print("current url:",self.browser.current_url)
    #         i = wait.until(EC.element_to_be_clickable(i))
    #         i.click()
    #         # print("current url:",self.browser.current_url)
    #         title = self.browser.find_element(By.TAG_NAME, "h3").text
    #         # print("title:",title)
    #         if self.product_name not in title:
    #             search_query_is_in_product_names = False
    #             break
    #         self.browser.back()
    #         # print("current url:",self.browser.current_url)
            
    #     self.assertTrue(search_query_is_in_product_names)
