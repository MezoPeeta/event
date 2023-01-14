from selenium import webdriver
from django.contrib.auth.models import User
import json 

class TestUtils:
    def init_selenium(self):
        f = open("driver_config.json", "r")
        self.driver_config = json.load(f)
        self.path = self.driver_config["path"]
        if self.driver_config["driver"].lower() == "chrome":
            self.browser = webdriver.Chrome(self.path)
        elif self.driver_config["driver"].lower() == "firefox":
            self.browser = webdriver.Firefox(self.path)
        elif self.driver_config["driver"].lower() == "edge":
            self.browser = webdriver.Edge(self.path)

        return self.browser

    def selenium_admin_login(self):
        self.user = User.objects.create(username="Test")
        self.user.set_password("123456789")
        self.user.save()
        browser = self.init_selenium()
        self.client.login(username="Test", password='123456789') #Native django test client
        cookie = self.client.cookies['sessionid']
        browser.get(self.live_server_url + '/us/')  #selenium will set cookie domain based on current page domain
        browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        browser.refresh() #need to update page for logged in user
        browser.get(self.live_server_url + '/us/')   
        return browser
    
    def login_admin(self):
        self.user = User.objects.create(username="Test")
        self.user.set_password("123456789")
        self.user.save()
        self.client.login(username='Test', password='123456789')

        return self.client