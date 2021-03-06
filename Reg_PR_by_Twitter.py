# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from settings import *
import time, unittest

from Auth_facebook_TRB import myWait


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Reg_PR_by_Twitter(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Reg_PR_by_Twitter(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("Присоединиться к сообществу").click()
        wd.find_element_by_xpath("//label[@for='i-prPOPUP']").click()
        if not wd.find_element_by_id("i-prPOPUP").is_selected():
            wd.find_element_by_id("i-prPOPUP").click()
        wd.find_element_by_xpath("//a[contains(@onclick,'Twitter')]").click()
        wd.find_element_by_css_selector("a.bx-ss-button.twitter-button").click()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_id("username_or_email").clear()
        wd.find_element_by_id("username_or_email").send_keys("coolcat89@mail.ru")
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("11043212")
        wd.find_element_by_id("allow").click()
        self.assertTrue(success)
        myWait()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
