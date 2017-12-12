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

class Main_page_1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Main_page_1(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("войти").click()
        wd.find_element_by_id("system-auth-form-login").click()
        wd.find_element_by_id("system-auth-form-login").clear()
        wd.find_element_by_id("system-auth-form-login").send_keys("maria12@toprussianbloggers.ru")
        wd.find_element_by_id("system-auth-form-password").click()
        wd.find_element_by_id("system-auth-form-password").clear()
        wd.find_element_by_id("system-auth-form-password").send_keys("123456")
        wd.find_element_by_xpath("//div[@class='modal-body']/form/div[4]/input").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Личная страница").click()
        wd.find_element_by_id("BIRTHDAY").click()
        wd.find_element_by_id("BIRTHDAY").clear()
        wd.find_element_by_id("BIRTHDAY").send_keys("01.01.2000")
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Сохранить изменения']").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Главная").click()
        wd.find_element_by_link_text("Добавить новую кампанию").click()
        self.assertIn("Добавить новую кампанию", wd.title)
        wd.find_element_by_link_text("Главная").click()
        wd.find_element_by_link_text("найти блогеров").click()
        wd.find_element_by_link_text("Дополнительные параметры").click()
        wd.find_element_by_link_text("Главная").click()
        wd.find_element_by_link_text("Все кампании").click()
        wd.find_element_by_link_text("Просмотреть всех PR-агентов").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
