from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from django.urls import reverse
from base.models import Contact
from selenium_test import TestUtils
from selenium.webdriver import ActionChains


class TestingPrHr(LiveServerTestCase, TestUtils):
    def setUp(self):
        self.selenium_admin_login()

    def test_pr(self):
        # saving the test profile as a PR member
        dashboard_page = reverse("Dashboard")
        dashboard = self.live_server_url + dashboard_page
        self.user.profile.committee = "PR"
        self.user.profile.save()
        # accessing the dashboard
        self.browser.get(dashboard)
        request = self.client.get(dashboard_page)
        # checking the url + status code + comittee
        current_url = self.browser.current_url
        self.assertEqual(current_url, dashboard)
        self.assertEqual(request.status_code, 200)
        self.assertFalse(self.user.profile.committee != "PR")

    def test_hr(self):
        # saving the test profile as a HR member
        dashboard_page = reverse("Inbox")
        dashboard = self.live_server_url + dashboard_page
        contact_page = reverse("Contact")
        self.user.profile.committee = "HR"
        self.user.profile.save()
        # accessing the dashboard
        self.browser.get(dashboard)
        self.browser.get(self.live_server_url + contact_page)
        # creating a contact report
        name = self.browser.find_element(
            By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[1]/input"
        )
        self.send_keys_action_chains(name, "Tester")
        email = self.browser.find_element(
            By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[2]/input"
        )
        self.send_keys_action_chains(email, "Tester@gmail.com")

        subject = self.browser.find_element(
            By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[3]/input"
        )
        self.send_keys_action_chains(subject, "Testing")

        message = self.browser.find_element(
            By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[4]/textarea"
        )
        self.send_keys_action_chains(message, "Test")
        submit_btn = self.browser.find_element(
            By.XPATH, "/html/body/section/div/div[2]/div[1]/form/div[5]/input"
        )
        submit_btn.click()
        # checking the contact in the inbox page
        self.browser.get(dashboard)
        # checking if report is saved
        is_contacted = True if Contact.objects.get(name="Tester") else False
        self.assertTrue(is_contacted)
        # checking the current url
        current_url = self.browser.current_url
        self.assertEqual(current_url, dashboard)
