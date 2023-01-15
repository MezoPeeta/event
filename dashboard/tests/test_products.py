from django.test import LiveServerTestCase
from time import sleep
from selenium.webdriver.common.by import By
from base.models import Videos
from products.models import Products

from django.urls import reverse
from selenium_test import TestUtils

from django.test import override_settings



class TestProduct(LiveServerTestCase,TestUtils):
    def setUp(self):
        self.browser = self.selenium_admin_login()
        
    
    def test_videos(self):
        self.user.profile.committee = "Marketing"
        self.user.profile.save()
        self.browser.get(self.live_server_url + "/en/new/video")
        video_url = self.browser.find_element(By.XPATH,'//*[@id="id_urlID"]')
        video_url.send_keys("2vqlQxOOxYY")
        btn = self.browser.find_element(By.TAG_NAME,"button")
        btn.click()
        is_video_uploaded = True if Videos.objects.get(urlID="2vqlQxOOxYY") else False
        videos_page = self.live_server_url + "/en/watchus/"
        
        self.assertTrue(is_video_uploaded) #Check in Database
        self.assertEqual(self.browser.current_url,videos_page) #Check eno ra7 URL ( Redirect )

    
    @override_settings(DEBUG=True)
    def test_product(self):
        
        self.user.profile.committee = "PR"
        self.user.profile.save()
        self.browser.get(self.live_server_url + "/en/new/product")
        products_price = self.browser.find_element(By.XPATH,'//*[@id="id_price"]')
        products_price.send_keys(10)
        element = self.browser.find_element(By.ID,'ftco-loader')
        self.browser.execute_script("arguments[0].style.visibility='hidden'", element)

        btn = self.browser.find_element(By.TAG_NAME,"button")
        btn.click()

        is_product_uploaded = True if Products.objects.get(price=10) else False
        store_page = self.live_server_url + reverse("Store")
        self.assertTrue(is_product_uploaded)

        self.assertEqual(self.browser.current_url,store_page)
        



