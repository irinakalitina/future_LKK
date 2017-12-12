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

class Campaign_response(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Campaign_response(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("войти").click()
        wd.find_element_by_xpath("//a[contains(@onclick,'Facebook')]").click()
        wd.find_element_by_css_selector("a.bx-ss-button.facebook-button").click()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_id("email").click()
        wd.find_element_by_id("email").clear()
        wd.find_element_by_id("email").send_keys("apavlova@toprussianbloggers.ru")
        wd.find_element_by_id("pass").click()
        wd.find_element_by_id("pass").clear()
        wd.find_element_by_id("pass").send_keys("Lastchance")
        wd.find_element_by_id("u_0_0").click()
        self.assertTrue(success)
        myWait()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_link_text("Павлова Анна").click()
        wd.find_element_by_link_text("Мои PR-кампании").click()
        wd.find_element_by_link_text("Хочу принять участие").click()
        wd.find_element_by_link_text("Вы откликнулись (1)").click()
        wd.find_element_by_link_text("Отменить заявку").click()
        wd.find_element_by_link_text("Вы откликнулись (1)").click()
        wd.find_element_by_xpath("//div[@id='tab3']//a[.='Отменить заявку']").click()
        wd.find_element_by_link_text("Кампании").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
