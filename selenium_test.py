from selenium import webdriver
from django.contrib.auth.models import User
import sys
from enum import Enum
from winreg import *
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class Browser(Enum):
    CHROME, FIREFOX, EDGE, BRAVE = "chrome", "firefox", "edge", "brave"


class TestUtils:
    def get_default_browser(self):
        """
        Get the default browser on the system and return the browser name as a string
        (e.g. "chrome", "firefox", etc.)
        """
        if sys.platform == "win32":
            with OpenKey(
                HKEY_CURRENT_USER,
                r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice",
            ) as key:
                browser = QueryValueEx(key, "Progid")[0]
                return browser.lower()
        else:
            return "firefox"

    def init_selenium(self, headless=True):
        """
        Initialize selenium webdriver based on the default browser on the system
        and return the webdriver object
        """
        browser = self.get_default_browser()
        if Browser.EDGE.value in browser:
            options = webdriver.EdgeOptions()
            options.headless = headless
            self.browser = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif Browser.FIREFOX.value in browser:
            options = webdriver.FirefoxOptions()
            options.headless = headless
            self.browser = webdriver.Firefox(GeckoDriverManager().install())
        elif Browser.CHROME.value in browser:
            options = webdriver.ChromeOptions()
            options.headless = headless
            self.browser = webdriver.Chrome(ChromeDriverManager().install())
        elif Browser.BRAVE.value in browser:
            options = webdriver.ChromeOptions()
            options.headless = headless
            self.browser = webdriver.Chrome(
                ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()
            )

        return self.browser

    def login_admin(self):
        self.user = User.objects.create(username="Test")
        self.user.set_password("123456789")
        self.user.save()
        self.client.login(username="Test", password="123456789")

        return self.client

    def selenium_admin_login(self):
        client = self.login_admin()
        browser = self.init_selenium()
        cookie = client.cookies["sessionid"]
        browser.get(self.live_server_url + "/us/")
        browser.add_cookie(
            {"name": "sessionid", "value": cookie.value, "secure": False, "path": "/"}
        )
        browser.refresh()
        browser.get(self.live_server_url + "/us/")
        return browser
