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

class About_project(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_About_project(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("О проекте").click()
        self.assertIn("О проекте", wd.title)
        wd.find_element_by_name("EMAIL").click()
        wd.find_element_by_name("EMAIL").clear()
        wd.find_element_by_name("EMAIL").send_keys("maria12@toprussianbloggers.ru")
        wd.find_element_by_xpath("//form[@id='subscribtion-form']//button[.='Подписаться']").click()
        if wd.find_element_by_css_selector("div.alert.alert-success"):
           print ("Element exists")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Главная").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
