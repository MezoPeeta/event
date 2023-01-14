from django.test import LiveServerTestCase
from selenium import webdriver

from selenium.webdriver.common.by import By

class Test_registration(LiveServerTestCase):
    def setUp(self):
        self.path = "C:\Program Files (x86)\msedgedriver.exe"
        self.browser = webdriver.Edge(self.path)
        
        
    def test_registration(self):
        register = self.live_server_url + "/en/register"
        
        self.browser.get(register)
        
        username_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_username"]')
        first_name_textbox = self.browser.find_element(By.XPATH,'//*[@id="id_first_name"]')
        last_name_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_last_name"]')
        Email_textbox = self.browser.find_element(By.XPATH,'//*[@id="id_email"]')
        Registration_code_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_registration_code"]')
        password_textbox = self.browser.find_element(By.XPATH,'//*[@id="id_password1"]')
        confirm_password_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_password2"]')
        
        username_textbox.send_keys("hamadaa")
        first_name_textbox.send_keys("Hamdi")
        last_name_textbox.send_keys("Mahmoud")
        Email_textbox.send_keys("Mahmoud@email.com")
        Registration_code_textbox.send_keys("481294894")
        password_textbox.send_keys("Password")
        confirm_password_textbox.send_keys("Password")
        self.assertEquals(username_textbox.get_attribute("value"), "hamadaa")
        self.assertEquals(first_name_textbox.get_attribute("value"), "Hamdi")
        self.assertEquals(last_name_textbox.get_attribute("value"), "Mahmoud")
        self.assertEquals(Email_textbox.get_attribute("value"), "Mahmoud@email.com")
        self.assertEquals(Registration_code_textbox.get_attribute("value"), "481294894")
        self.assertEquals(password_textbox.get_attribute("value"), "Password")
        self.assertEquals(confirm_password_textbox.get_attribute("value"), "Password")
    def test_login(self):
        login = self.live_server_url + "/en/login"
        self.browser.get(login)
        
        username_textbox = self.browser.find_element(By.XPATH, '//*[@id="id_username"]')
        password_textbox = self.browser.find_element(By.XPATH,'//*[@id="id_password"]')
        username_textbox.send_keys("hamadaaa")
        password_textbox.send_keys("Password")
        
        self.assertEquals(username_textbox.get_attribute("value"), "hamadaaa")
        self.assertEquals(password_textbox.get_attribute("value"), "Password")





     
        

        
        
        