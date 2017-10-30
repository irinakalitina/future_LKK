# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class ExpectedCondition(object):
    pass

def myWait():
    pass


class toprussianbloggers(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def test_toprussianbloggers(self, windowHandler=None):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Главная").click()
        wd.find_element_by_link_text("войти").click()
        wd.find_element_by_xpath("//a[contains(@onclick,'Facebook')]").click()
        wd.find_element_by_css_selector("a.bx-ss-button.facebook-button").click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("user@rambler.ru")
        wd.find_element_by_id("pass").click()
        wd.find_element_by_id("pass").clear()
        wd.find_element_by_id("pass").send_keys("password")
        wd.find_element_by_id("u_0_0").click()
        self.assertTrue(success)
        wd.find_element_by_link_text("Кампании").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
