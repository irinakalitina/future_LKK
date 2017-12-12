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


class Contacts_TRB(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def test_Contacts_TRB(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Контакты").click()
        wd.find_element_by_xpath("//div[@class='form-body']/div").click()
        wd.find_element_by_id("form-1-NAME").click()
        wd.find_element_by_id("form-1-NAME").clear()
        wd.find_element_by_id("form-1-NAME").send_keys("Ирина")
        wd.find_element_by_id("form-1-PHONE").click()
        wd.find_element_by_id("form-1-PHONE").clear()
        wd.find_element_by_id("form-1-PHONE").send_keys("89167418525")
        wd.find_element_by_id("form-1-EMAIL").click()
        wd.find_element_by_id("form-1-EMAIL").clear()
        wd.find_element_by_id("form-1-EMAIL").send_keys("coolcat89@mail.ru")
        wd.find_element_by_id("form-1-MESSAGE").click()
        wd.find_element_by_id("form-1-MESSAGE").clear()
        wd.find_element_by_id("form-1-MESSAGE").send_keys("Добрый день! ")
        wd.find_element_by_xpath("//div[@class='form-body']//button[normalize-space(.)='Отправить']").click()
        wd.find_element_by_link_text("Вопрос — ответ").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()