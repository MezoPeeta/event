from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestingPrHr(LiveServerTestCase):
    def test_pr(self):
        PATH = "C:/Users/abdo/Downloads/chromedriver_win32.exe"
        self.browser = webdriver.Chrome(PATH)
        dashboard = self.live_server_url + "/en//dashboard/" 
        #creating a user
        self.user = User.objects.create(username="Test")
        self.user.set_password("123456789")
        self.user.profile.committee = "PR"
        self.user.save()
        self.user.profile.save()

        # entering user credentials
        self.browser.get(dashboard)
        username = self.browser.find_element(By.XPATH,'//*[@id="id_username"]')
        username.send_keys("Test")
        password = self.browser.find_element(By.XPATH,'//*[@id="id_password"]')
        password.send_keys("123456789")
        # logging in 
        login_button = self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div/form/div[2]/input')
        login_button.click()
        # navigating to profile
        profile_button = self.browser.find_element(By.XPATH,'/html/body/nav/ul/li[7]/a')
        profile_button.click()
        # navigating to the dashbord
        dashboard_button = self.browser.find_element(By.XPATH,'/html/body/div[1]/center/div/a[2]')
        dashboard_button.click()
        # adding video 
        action_button = self.browser.find_element(By.XPATH,'/html/body/section/div/a[2]')
        action_button.click()
    def test_hr(self):
        PATH = "C:/Users/abdo/Downloads/chromedriver_win32.exe"
        self.browser = webdriver.Chrome(PATH)
        dashboard = self.live_server_url + "/en//dashboard/"
        #creating a user
        self.user = User.objects.create(username="Test2")
        self.user.set_password("123456789")
        self.user.profile.committee = "HR"
        self.user.save()
        self.user.profile.save()

        # entering user credentials
        self.browser.get(dashboard)
        username = self.browser.find_element(By.XPATH,'//*[@id="id_username"]')
        username.send_keys("Test2")
        password = self.browser.find_element(By.XPATH,'//*[@id="id_password"]')
        password.send_keys("123456789")
        # logging in 
        login_button = self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div/form/div[2]/input')
        login_button.click()
        # navigating to profile
        profile_button = self.browser.find_element(By.XPATH,'/html/body/nav/ul/li[7]/a')
        profile_button.click()
        # navigating to the dashbord
        dashboard_button = self.browser.find_element(By.XPATH,'/html/body/div[1]/center/div/a[2]')
        dashboard_button.click()
        