# -*- coding: utf-8 -*-
from lib2to3.pgen2 import driver

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

        all_handles = wd.window_handles  # сюда придет список всех окон all_handles = wd.window_handles
        for x in all_handles:   # попробуем напечатать весь список окон
            print(x)

        wd.find_element_by_css_selector("a.bx-ss-button.facebook-button").click()
        #wd.switch_to_window("https://www.facebook.com/login.php?skip_api_login=1&api_key=193086034367632&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Ftoprussianbloggers.ru%252Fajax%252Fregistration%252Fauth%252F%253Fauth_service_id%253DFacebook%2526check_key%253D5ff4430e3477903c98b7dc2003e341ff%2526backurl%253D%25252Fajax%25252Fregistration%25252Fauth%25252F%26display%3Dpopup%26scope%3Demail%252Cpublish_actions%252Cuser_friends%26client_id%3D193086034367632%26ret%3Dlogin%26logger_id%3Db17710a6-459c-01ba-8ba6-ebcec2fdc2c3&cancel_url=https%3A%2F%2Ftoprussianbloggers.ru%2Fajax%2Fregistration%2Fauth%2F%3Fauth_service_id%3DFacebook%26check_key%3D5ff4430e3477903c98b7dc2003e341ff%26backurl%3D%252Fajax%252Fregistration%252Fauth%252F%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=popup&locale=ru_RU&logger_id=b17710a6-459c-01ba-8ba6-ebcec2fdc2c3")
        wd.get('https://www.facebook.com/login.php?skip_api_login=1&api_key=193086034367632&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fredirect_uri%3Dhttps%253A%252F%252Ftoprussianbloggers.ru%252Fajax%252Fregistration%252Fauth%252F%253Fauth_service_id%253DFacebook%2526check_key%253D5ff4430e3477903c98b7dc2003e341ff%2526backurl%253D%25252Fajax%25252Fregistration%25252Fauth%25252F%26display%3Dpopup%26scope%3Demail%252Cpublish_actions%252Cuser_friends%26client_id%3D193086034367632%26ret%3Dlogin%26logger_id%3Db17710a6-459c-01ba-8ba6-ebcec2fdc2c3&cancel_url=https%3A%2F%2Ftoprussianbloggers.ru%2Fajax%2Fregistration%2Fauth%2F%3Fauth_service_id%3DFacebook%26check_key%3D5ff4430e3477903c98b7dc2003e341ff%26backurl%3D%252Fajax%252Fregistration%252Fauth%252F%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=popup&locale=ru_RU&logger_id=b17710a6-459c-01ba-8ba6-ebcec2fdc2c3')

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
