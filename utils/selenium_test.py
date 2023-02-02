from selenium import webdriver
from django.contrib.auth.models import User
import sys
from enum import Enum
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver import ActionChains


class Browser(Enum):
    CHROME, FIREFOX, EDGE, BRAVE = "chrome", "firefox", "edge", "brave"


class TestUtils:        
        


    def get_default_browser(self):
        #pylint: disable=too-many-lines
        """
        Get the default browser on the system and return the browser name as a string
        (e.g. "chrome", "firefox", etc.)
        """
        if sys.platform == "win32":
            from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER

            with OpenKey(
                HKEY_CURRENT_USER,
                r"Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice",
            ) as key:
                browser = QueryValueEx(key, "Progid")[0]
                return browser.lower()
        else:
            return "chrome"

    def init_selenium(self, headless=True):
        """
        Initialize selenium webdriver based on the default browser on the system
        and return the webdriver object
        """
        browser = self.get_default_browser()
        if Browser.EDGE.value in browser:
            options = webdriver.EdgeOptions()
            options.headless = headless
            self.browser = webdriver.Edge(
                EdgeChromiumDriverManager(path=r"driver").install(), options=options
            )
        elif Browser.CHROME.value in browser:
            options = webdriver.ChromeOptions()
            options.headless = headless
            self.browser = webdriver.Chrome(
                ChromeDriverManager(path=r"driver").install(), options=options
            )
        elif Browser.BRAVE.value in browser:
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1200,1200,--ignore-certificate-errors")
            options.headless = headless
            self.browser = webdriver.Chrome(
                ChromeDriverManager(chrome_type=ChromeType.BRAVE,path=r"driver").install(),
                options=options,
            )
        elif Browser.FIREFOX.value in browser:
            options = webdriver.FirefoxOptions()
            options.headless = headless
            options.add_argument("--window-size=1200,1200,--ignore-certificate-errors")
            self.browser = webdriver.Firefox(
                executable_path=GeckoDriverManager(path=r"driver").install(), options=options
            )
        else:
            raise Exception("Browser not supported")

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

    def send_keys_action_chains(self, element, keys):
        return (
            ActionChains(self.browser)
            .move_to_element(element)
            .click(element)
            .send_keys(keys)
            .perform()
        )

    def click_action_chains(self, element):
        return (
            ActionChains(self.browser).move_to_element(element).click(element).perform()
        )
