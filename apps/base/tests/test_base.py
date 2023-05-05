from django.test import LiveServerTestCase, TestCase
from selenium.webdriver.common.by import By
from apps.base.models import Videos, Subscribe, Contact
from utils.selenium_test import TestUtils
from apps.users.models import Committee

class TestVideos(LiveServerTestCase, TestUtils):
    def setUp(self):
        self.browser = self.selenium_admin_login()

    def test_videos(self):
        committee = Committee.objects.create(name="Marketing")
        committee.save()
        self.user.profile.committee = committee
        self.user.profile.save()
        self.browser.get(self.live_server_url + "/en/new/video")
        video_url = self.browser.find_element(By.XPATH, '//*[@id="id_urlID"]')
        video_url.send_keys("2vqlQxOOxYY")
        btn = self.browser.find_element(By.TAG_NAME, "button")
        btn.click()

        videos_page = self.live_server_url + "/en/watchus/"
        video = Videos.objects.get(urlID="2vqlQxOOxYY")

        self.assertTrue(video)
        self.assertEqual(self.browser.current_url, videos_page)
        self.assertEqual(str(video), "video")
        self.assertTemplateUsed("base/watch-us.html")


class TestBase(TestCase):
    def test_subscribe(self):
        subscribe = Subscribe.objects.create(name="test", email="test@gmail.com")
        self.assertEqual(str(subscribe), "test")

    def test_contact(self):
        self.client.post(
            "/en/contact/",
            {
                "name": "test",
                "subject": "Test",
                "message": "Test",
                "email": "Tester@gmail.com",
            },
        )

        self.assertEqual(str(Contact.objects.get(name="test")), "test")

   