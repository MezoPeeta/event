from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from utils.selenium_test import TestUtils


class TestRegistration(LiveServerTestCase, TestUtils):
    def setUp(self):
        self.init_selenium()

    def test_registration(self):
        register = self.live_server_url + "/en/register"

        self.browser.get(register)

        username_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_username"]')
        first_name_textbox = self.browser.find_element(
            By.XPATH, '//*[@id="id_first_name"]'
        )
        last_name_textbox = self.browser.find_element(
            By.XPATH, '//*[@id="id_last_name"]'
        )
        email_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_email"]')
        registration_code_textbox = self.browser.find_element(
            By.XPATH, '//*[@id="id_registration_code"]'
        )
        password_textbox = self.browser.find_element(
            By.XPATH, '//*[@id="id_password1"]'
        )
        confirm_password_textbox = self.browser.find_element(
            By.XPATH, '//*[@id="id_password2"]'
        )

        username_textbox.send_keys("hamadaa")
        first_name_textbox.send_keys("Hamdi")
        last_name_textbox.send_keys("Mahmoud")
        email_textbox.send_keys("Mahmoud@email.com")
        registration_code_textbox.send_keys("481294894")
        password_textbox.send_keys("Password")
        confirm_password_textbox.send_keys("Password")
        self.assertEqual(username_textbox.get_attribute("value"), "hamadaa")
        self.assertEqual(first_name_textbox.get_attribute("value"), "Hamdi")
        self.assertEqual(last_name_textbox.get_attribute("value"), "Mahmoud")
        self.assertEqual(email_textbox.get_attribute("value"), "Mahmoud@email.com")
        self.assertEqual(registration_code_textbox.get_attribute("value"), "481294894")
        self.assertEqual(password_textbox.get_attribute("value"), "Password")
        self.assertEqual(confirm_password_textbox.get_attribute("value"), "Password")

    def test_login(self):
        login = self.live_server_url + "/en/login"
        self.browser.get(login)

        username_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_username"]')
        password_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_password"]')
        username_textbox.send_keys("hamadaaa")
        password_textbox.send_keys("Password")
        self.assertEqual(username_textbox.get_attribute("value"), "hamadaaa")
        self.assertEqual(password_textbox.get_attribute("value"), "Password")
