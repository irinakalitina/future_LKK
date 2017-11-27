# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest

from Auth_facebook_TRB import myWait


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Advertisers(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Advertisers(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        self.assertIn("TOP RUSSIAN BLOGGERS",wd.title)
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Рекламодателям").click()
        wd.find_element_by_link_text("Тарифы на услуги").click()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.get("https://toprussianbloggers.ru/upload/docs/prices.pdf")
        wd.find_element_by_id("download").click()
        alert = wd.switch_to.alert()
        alert.accept()

        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.get("https://toprussianbloggers.ru/adv/")
        wd.find_element_by_link_text("Технические требования").click()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.find_element_by_id("download").click()
        myWait()
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
        wd.get("https://toprussianbloggers.ru/adv/")
        wd.find_element_by_link_text("заполните форму").click()
        wd.find_element_by_id("form-1-NAME").click()
        wd.find_element_by_id("form-1-NAME").clear()
        wd.find_element_by_id("form-1-NAME").send_keys("Мария")
        wd.find_element_by_id("form-1-PHONE").click()
        wd.find_element_by_id("form-1-PHONE").clear()
        wd.find_element_by_id("form-1-PHONE").send_keys("+79154563282")
        wd.find_element_by_id("form-1-EMAIL").click()
        wd.find_element_by_id("form-1-EMAIL").clear()
        wd.find_element_by_id("form-1-EMAIL").send_keys("coolcat2017@mail.ru")
        wd.find_element_by_id("form-1-MESSAGE").click()
        wd.find_element_by_id("form-1-MESSAGE").clear()
        wd.find_element_by_id("form-1-MESSAGE").send_keys("Добрый день")
        wd.find_element_by_id("form-1-NAME").click()
        wd.find_element_by_id("form-1-NAME").clear()
        wd.find_element_by_id("form-1-NAME").send_keys("Мария (тест)")
        wd.find_element_by_id("form-1-MESSAGE").click()
        wd.find_element_by_xpath("//div[@class='form-body']//button[normalize-space(.)='Отправить']").click()
        wd.find_element_by_css_selector("button.close").click()
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Главная").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
