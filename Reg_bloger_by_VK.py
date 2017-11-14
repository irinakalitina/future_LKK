# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

from Auth_facebook_TRB import myWait


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Reg_bloger_by_VK(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Reg_bloger_by_VK(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("Присоединиться к сообществу").click()
        wd.find_element_by_css_selector("label.radio-inline.form-register__user-type__label ").click()
        if not wd.find_element_by_id("i-blogerPOPUP").is_selected():
            wd.find_element_by_id("i-blogerPOPUP").click()
        wd.find_element_by_xpath("//a[contains(@onclick,'VKontakte')]").click()
        wd.find_element_by_css_selector("a.bx-ss-button.vkontakte-button").click()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("kalitina.irina@rambler.ru")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("Rjkbptq1989")
        wd.find_element_by_id("install_allow").click()
        self.assertTrue(success)
        myWait()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
