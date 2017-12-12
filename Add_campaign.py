# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from settings import *
import time, unittest

from selenium.webdriver.support.select import Select


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Add_campaign(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Add_campaign(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("войти").click()
        wd.find_element_by_id("system-auth-form-login").click()
        wd.find_element_by_id("system-auth-form-login").clear()
        wd.find_element_by_id("system-auth-form-login").send_keys("maria9@toprussianbloggers.ru")
        wd.find_element_by_id("system-auth-form-password").click()
        wd.find_element_by_id("system-auth-form-password").clear()
        wd.find_element_by_id("system-auth-form-password").send_keys("123456")
        wd.find_element_by_xpath("//div[@class='modal-body']/form/div[4]/input").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Мои PR-кампании").click()
        wd.find_element_by_link_text("Добавить новую кампанию").click()
        wd.find_element_by_id("NAME").click()
        wd.find_element_by_id("NAME").clear()
        wd.find_element_by_id("NAME").send_keys("maria way")
        wd.find_element_by_id("DATE_START").click()
        wd.find_element_by_id("DATE_START").clear()
        wd.find_element_by_id("DATE_START").send_keys("27.12.2017")
        wd.find_element_by_id("DATE_END").click()
        wd.find_element_by_id("DATE_END").click()
        wd.find_element_by_id("DATE_END").clear()
        wd.find_element_by_id("DATE_END").send_keys("29.12.2017")
        wd.find_element_by_id("SET_TO").click()
        wd.find_element_by_id("SET_TO").clear()
        wd.find_element_by_id("SET_TO").send_keys("26.12.2017")
        wd.find_element_by_css_selector("input.select2-search__field").click()
        wd.find_element_by_xpath("//span[contains(@aria-activedescedant,'select2-DIRECTION-result')]").click()
        wd.find_element_by_id("select2-DIRECTION-result-t40z-23").click()
        wd.find_element_by_id("select2-CITY-container").click()
        wd.find_element_by_id("select2-BRAND-container").click()
        wd.find_element_by_id("PR_DESCRIPTION").click()
        wd.find_element_by_id("PR_DESCRIPTION").clear()
        wd.find_element_by_id("PR_DESCRIPTION").send_keys("maria way")
        wd.find_element_by_id("MEDIAPERSONS").click()
        wd.find_element_by_id("MEDIAPERSONS").clear()
        wd.find_element_by_id("MEDIAPERSONS").send_keys("12")
        wd.find_element_by_id("DEMANDS").click()
        wd.find_element_by_id("DEMANDS").clear()
        wd.find_element_by_id("DEMANDS").send_keys("100%")
        wd.find_element_by_id("STYLISTICS").click()
        wd.find_element_by_id("STYLISTICS").clear()
        wd.find_element_by_id("STYLISTICS").send_keys("123")
        wd.find_element_by_css_selector("button.btn.margin-bottom-10").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
