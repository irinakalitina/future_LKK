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

class Main_page_2(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Main_page_2(self):
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
        wd.find_element_by_link_text("Главная").click()
        wd.find_element_by_link_text("В работе (0)").click()
        wd.find_element_by_link_text("Завершенные (2)").click()
        wd.find_element_by_link_text("Все новости").click()
        wd.find_element_by_name("EMAIL").click()
        wd.find_element_by_name("EMAIL").clear()
        wd.find_element_by_name("EMAIL").send_keys("mari22@toprussianbloggers.ru")
        wd.find_element_by_xpath("//form[@id='subscribtion-form']//button[.='Подписаться']").click()
        wd.find_element_by_css_selector("div.alert.alert-success").click()
        wd.find_element_by_css_selector("div.alert.alert-success").click()
        wd.find_element_by_css_selector("div.alert-success-icon.js-alert-success").click()
        wd.find_element_by_link_text("Кампании").click()
        self.assertIn("Кампании", wd.title)
        wd.find_element_by_xpath("//label[@for='directions10']").click()
        if not wd.find_element_by_id("directions10").is_selected():
            wd.find_element_by_id("directions10").click()
        wd.find_element_by_xpath("//label[@for='directions14']").click()
        if not wd.find_element_by_id("directions14").is_selected():
            wd.find_element_by_id("directions14").click()
        wd.find_element_by_xpath("//label[@for='directions6']").click()
        if not wd.find_element_by_id("directions6").is_selected():
            wd.find_element_by_id("directions6").click()
        wd.find_element_by_xpath("//label[@for='directions7']").click()
        if not wd.find_element_by_id("directions7").is_selected():
            wd.find_element_by_id("directions7").click()
        wd.find_element_by_xpath("//label[@for='directions13']").click()
        if not wd.find_element_by_id("directions13").is_selected():
            wd.find_element_by_id("directions13").click()
        wd.find_element_by_xpath("//label[@for='directions11']").click()
        if not wd.find_element_by_id("directions11").is_selected():
            wd.find_element_by_id("directions11").click()
        wd.find_element_by_xpath("//label[@for='directions9']").click()
        if not wd.find_element_by_id("directions9").is_selected():
            wd.find_element_by_id("directions9").click()
        wd.find_element_by_xpath("//label[@for='directions8']").click()
        if not wd.find_element_by_id("directions8").is_selected():
            wd.find_element_by_id("directions8").click()
        wd.find_element_by_xpath("//label[@for='directions15']").click()
        if not wd.find_element_by_id("directions15").is_selected():
            wd.find_element_by_id("directions15").click()
        wd.find_element_by_xpath("//label[@for='directions20']").click()
        if not wd.find_element_by_id("directions20").is_selected():
            wd.find_element_by_id("directions20").click()
        wd.find_element_by_xpath("//label[@for='directions21']").click()
        if not wd.find_element_by_id("directions21").is_selected():
            wd.find_element_by_id("directions21").click()
        wd.find_element_by_xpath("//label[@for='directions22']").click()
        if not wd.find_element_by_id("directions22").is_selected():
            wd.find_element_by_id("directions22").click()
        wd.find_element_by_xpath("//label[@for='directions23']").click()
        if not wd.find_element_by_id("directions23").is_selected():
            wd.find_element_by_id("directions23").click()
        wd.find_element_by_css_selector("label").click()
        if not wd.find_element_by_id("directions24").is_selected():
            wd.find_element_by_id("directions24").click()
        wd.find_element_by_link_text("Просмотреть всех PR-агентов").click()
        wd.find_element_by_name("pr_search").click()
        wd.find_element_by_name("pr_search").clear()
        wd.find_element_by_name("pr_search").send_keys("Алина")
        wd.find_element_by_xpath("//div[@class='blogers-filter']//button[.='Найти']").click()
        wd.find_element_by_link_text("Блогеры").click()
        wd.find_element_by_link_text("Дополнительные параметры").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
