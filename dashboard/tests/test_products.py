from django.test import LiveServerTestCase
from selenium import webdriver
from time import sleep
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By
from base.models import Videos
from products.models import Products

from django.urls import reverse
# virus task is done here
class TestProduct(LiveServerTestCase):
    def setUp(self):
        PATH = r'E:\coding tedx\driver\chromedriver.exe'
        self.browser = webdriver.Chrome(PATH)
        self.user = User.objects.create(username="TestUser")
        self.user.set_password("123456789")
        self.user.save()
        self.client.login(username="TestUser",password="123456789")
        cookie = self.client.cookies['sessionid']
        self.browser.get(self.live_server_url + '/us/')  #selenium will set cookie domain based on current page domain
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh() #need to update page for logged in user
        self.browser.get(self.live_server_url + '/us/')
        

    def test_videos(self):
        self.user.profile.committee = "Marketing"
        self.user.profile.save()
        self.browser.get(self.live_server_url + "/en//new/video")
        video_url = self.browser.find_element(By.XPATH,'//*[@id="id_urlID"]')
        video_url.send_keys("2vqlQxOOxYY")
        btn = self.browser.find_element(By.TAG_NAME,"button")
        btn.click()

        is_video_uploaded = True if Videos.objects.get(urlID="2vqlQxOOxYY") else False

        videos_page = self.live_server_url + "/en/watchus/"

        
        self.assertTrue(is_video_uploaded) #Check in Database
        self.assertEqual(self.browser.current_url,videos_page) #Check eno ra7 URL ( Redirect )

    
    def test_product(self):
        
        self.user.profile.committee = "PR"
        self.user.profile.save()
        self.browser.get(self.live_server_url + "/en//new/product")
        products_name = self.browser.find_element(By.XPATH,'//*[@id="id_name"]')
        products_name.send_keys('tests1')
        products_price = self.browser.find_element(By.XPATH,'//*[@id="id_price"]')
        products_price.send_keys(10)
        btn = self.browser.find_element(By.TAG_NAME,"button")
        btn.click()

        is_product_uploaded = True if Products.objects.get(name="tests1",price=10) else False
        store_page = self.live_server_url + reverse("Store")
        self.assertTrue(is_product_uploaded)

        self.assertEqual(self.browser.current_url,store_page)
        



