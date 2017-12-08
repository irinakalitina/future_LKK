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

class Response(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_Response(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("войти").click()
        wd.find_element_by_xpath("//a[@id='bx_auth_href_reg5a2a7c94cf2bfFacebook']/i").click()
        wd.find_element_by_css_selector("a.bx-ss-button.facebook-button").click()
        wd.find_element_by_link_text("Павлова Анна").click()
        wd.find_element_by_link_text("Мои PR-кампании").click()
        wd.find_element_by_link_text("Хочу принять участие").click()
        wd.find_element_by_link_text("Хочу принять участие").click()
        wd.find_element_by_link_text("Вы откликнулись (2)").click()
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
