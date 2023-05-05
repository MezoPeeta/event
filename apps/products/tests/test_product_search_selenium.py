# from django.test import LiveServerTestCase
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from apps.products.models import Products
# from utils.selenium_test import TestUtils


# class TestSearching(LiveServerTestCase, TestUtils):
#     def setUp(self):
#         self.product_name = "calculator"
#         self.product_1 = Products.objects.create(name=self.product_name, price=10)
#         self.product_2 = Products.objects.create(
#             name=self.product_name + "sadahkl", price=10
#         )
#         self.browser = self.init_selenium()
#         self.store = self.live_server_url + "/store/"
#         self.product_url = self.live_server_url + "/products/"

#         self.browser.get(self.store)

#         self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#         self.search_bar = self.browser.find_element(By.XPATH, '//*[@id="search_box"]')
#         self.search_bar.send_keys(self.product_name)

#     # def test_search_bar(self):
#     #     self.assertEqual(self.search_bar.get_attribute("value"), self.product_name)

#     def test_searching(self):
#         self.search_button = self.browser.find_element(
#             By.XPATH, '//*[@id="search-bar"]'
#         )
#         self.search_button.click()
#         url = self.browser.current_url

#         search_query_is_in_url = f"?search_query={self.product_name}" in url
#         self.assertTrue(search_query_is_in_url)

#     # def test_search_products(self):
#     #     self.search_button = self.browser.find_element(
#     #         By.XPATH, '//*[@id="search-bar"]'
#     #     )
#     #     self.search_button.click()
#     #     search_query_is_in_product_names = True
#     #     products = self.browser.find_elements(
#     #         By.XPATH, "//*[contains(text(), 'View Product')]"
#     #     )

#     #     products = self.browser.find_elements(
#     #         By.XPATH, "//*[contains(text(), 'View Product')]"
#     #     )

#     #     for product in products:
#     #         self.browser.get(self.product_url + str(self.product_1.pk))

#     #         title = self.browser.find_element(By.TAG_NAME, "h3").text

#     #         if self.product_name not in title:
#     #             search_query_is_in_product_names = False
#     #             break

#     #     self.assertTrue(search_query_is_in_product_names)
