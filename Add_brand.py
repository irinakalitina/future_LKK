# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

from selenium.webdriver.support.select import Select


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Add_brand(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Add_brand(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_link_text("войти").click()
        wd.find_element_by_id("system-auth-form-login").click()
        wd.find_element_by_id("system-auth-form-login").clear()
        wd.find_element_by_id("system-auth-form-login").send_keys("coolcat89@mail.ru")
        wd.find_element_by_id("system-auth-form-password").click()
        wd.find_element_by_id("system-auth-form-password").clear()
        wd.find_element_by_id("system-auth-form-password").send_keys("11043212")
        wd.find_element_by_xpath("//div[@class='modal-body']/form/div[4]/input").click()
        wd.find_element_by_link_text("Ирина").click()
        wd.find_element_by_link_text("Личная страница").click()
        wd.find_element_by_link_text("Добавить").click()
        wd.find_element_by_xpath("//span[@class='select2-selection__arrow']/b").click()
        #select = Select(wd.find_element_by_xpath("//span[@class='select2-selection__arrow']/b"))
        #select.select_by_visible_text("MAX")
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Готово']").click()
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Сохранить изменения']").click()
        wd.find_element_by_link_text("Ирина").click()
        wd.find_element_by_xpath("//div[@class='auth-user__personal-overflow']/div[1]/a").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
