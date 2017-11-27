# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Advertisers_2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Advertisers_2(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Рекламодателям").click()
        wd.find_element_by_link_text("Тарифы на услуги").click()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.get("https://toprussianbloggers.ru/upload/docs/prices.pdf")
        wd.find_element_by_id("download").click()
        alert = wd.switch_to.alert
        alert.accept
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Главная").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
