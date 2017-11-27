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

class how_it_works(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_how_it_works(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/how-it-works/")
        self.assertIn("Как это работает", wd.title)
        wd.find_element_by_css_selector("img.icon-desc__img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[1]/div[2]/div[1]/div[2]/a/img").click()
        self.assertIn("Регистрация нового пользователя", wd.title)
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[1]/div[2]/div[1]/div[3]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[2]/div[2]/div[1]/div[1]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[2]/div[2]/div[1]/div[2]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[2]/div[2]/div[1]/div[3]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[3]/div[2]/div[1]/div[1]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[3]/div[2]/div[1]/div[2]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[3]/div[2]/div[1]/div[3]/a").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[4]/div[2]/div[1]/div[1]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[4]/div[2]/div[1]/div[2]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//div[@id='tab1']/div[4]/div[2]/div[1]/div[3]/a/img").click()
        wd.back()
        wd.find_element_by_xpath("//ul[@class='list-inline']//a[normalize-space(.)='Как это работает']").click()
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Главная").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
