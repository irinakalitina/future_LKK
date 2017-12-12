# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from settings import *
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Invite_bloggers(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Invite_bloggers(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("войти").click()
        wd.find_element_by_id("system-auth-form-login").click()
        wd.find_element_by_id("system-auth-form-login").clear()
        wd.find_element_by_id("system-auth-form-login").send_keys("katya4@toprussianblogers.ru")
        wd.find_element_by_id("system-auth-form-password").click()
        wd.find_element_by_id("system-auth-form-password").clear()
        wd.find_element_by_id("system-auth-form-password").send_keys("123456")
        wd.find_element_by_xpath("//div[@class='modal-body']/form/div[4]/input").click()
        wd.find_element_by_link_text("Кампании").click()
        wd.find_element_by_link_text("Найти блогеров").click()
        wd.find_element_by_name("pr_search").click()
        wd.find_element_by_name("pr_search").clear()
        wd.find_element_by_name("pr_search").send_keys("Анна Павлова")
        wd.find_element_by_xpath("//div[@class='blogers-filter']//button[.='Найти']").click()
        wd.find_element_by_css_selector("label.user-checkbox__label.js-select-bloger").click()
        if not wd.find_element_by_id("select6170").is_selected():
            wd.find_element_by_id("select6170").click()
        wd.find_element_by_link_text("Отправить приглашения").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
