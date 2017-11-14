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

class Reg_PR_by_email(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Reg_PR_by_email(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("Присоединиться к сообществу").click()
        wd.find_element_by_xpath("//label[@for='i-prPOPUP']").click()
        if not wd.find_element_by_id("i-prPOPUP").is_selected():
            wd.find_element_by_id("i-prPOPUP").click()
        wd.find_element_by_id("NAME").click()
        wd.find_element_by_id("NAME").clear()
        wd.find_element_by_id("NAME").send_keys("Katya")
        wd.find_element_by_id("EMAIL").click()
        wd.find_element_by_id("EMAIL").clear()
        wd.find_element_by_id("EMAIL").send_keys("katya2@toprussianblogers.ru")
        wd.find_element_by_id("PASSWORD").click()
        wd.find_element_by_id("PASSWORD").clear()
        wd.find_element_by_id("PASSWORD").send_keys("123456")
        wd.find_element_by_id("CONFIRM_PASSWORD").click()
        wd.find_element_by_id("CONFIRM_PASSWORD").clear()
        wd.find_element_by_id("CONFIRM_PASSWORD").send_keys("123456")
        wd.find_element_by_css_selector("label.form-register__label-personal").click()
        if not wd.find_element_by_id("iaccessPOPUP").is_selected():
            wd.find_element_by_id("iaccessPOPUP").click()
        wd.find_element_by_id("register-submitPOPUP").click()
        wd.find_element_by_link_text("Кампании").click()
        wd.find_element_by_link_text("Блогеры").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
