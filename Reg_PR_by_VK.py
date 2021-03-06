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

class Reg_PR_by_VK(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Reg_PR_by_VK(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("Присоединиться к сообществу").click()
        wd.find_element_by_xpath("//label[@for='i-prPOPUP']").click()
        if not wd.find_element_by_id("i-prPOPUP").is_selected():
            wd.find_element_by_id("i-prPOPUP").click()
        wd.find_element_by_xpath("//a[contains(@onclick,'VKontakte')]").click()
        wd.find_element_by_css_selector("a.bx-ss-button.vkontakte-button").click()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("login")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("password")
        wd.find_element_by_id("install_allow").click()
        self.assertTrue(success)
        myWait()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_xpath("//div[@class='live-sourse']/label[2]").click()
        if not wd.find_element_by_xpath("//div[@class='live-sourse']/label[2]/input").is_selected():
            wd.find_element_by_xpath("//div[@class='live-sourse']/label[2]/input").click()
        wd.find_element_by_xpath("//div[@class='live-sourse']/label[3]").click()
        if not wd.find_element_by_xpath("//div[@class='live-sourse']/label[3]/input").is_selected():
            wd.find_element_by_xpath("//div[@class='live-sourse']/label[3]/input").click()
        wd.find_element_by_link_text("Вся лента новостей").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
