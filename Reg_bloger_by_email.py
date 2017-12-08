# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

testdata = [

]

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

    def test_Reg_bloger_by_email(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("Присоединиться к сообществу").click()
        wd.find_element_by_css_selector("label.radio-inline.form-register__user-type__label ").click()
        if not wd.find_element_by_id("i-blogerPOPUP").is_selected():
               wd.find_element_by_id("i-blogerPOPUP").click()
        wd.find_element_by_id("NAME").click()
        wd.find_element_by_id("NAME").clear()
        wd.find_element_by_id("NAME").send_keys("Мария")
        wd.find_element_by_id("EMAIL").click()
        wd.find_element_by_id("EMAIL").clear()
        wd.find_element_by_id("EMAIL").send_keys("maria14@toprussianbloger.ru")
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
        wd.find_element_by_xpath("//div[@class='live-sourse']/label[2]").click()
        if not wd.find_element_by_xpath("//div[@class='live-sourse']/label[2]/input").is_selected():
               wd.find_element_by_xpath("//div[@class='live-sourse']/label[2]/input").click()
        wd.find_element_by_xpath("//div[@class='live-sourse']/label[3]").click()
        if not wd.find_element_by_xpath("//div[@class='live-sourse']/label[3]/input").is_selected():
               wd.find_element_by_xpath("//div[@class='live-sourse']/label[3]/input").click()
        wd.find_element_by_xpath("//div[@class='live-sourse']/label[4]").click()
        if not wd.find_element_by_xpath("//div[@class='live-sourse']/label[4]/input").is_selected():
               wd.find_element_by_xpath("//div[@class='live-sourse']/label[4]/input").click()
        self.assertTrue(success)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()