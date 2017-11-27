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

class Add_brands(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_Add_brands(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/lk/")
        wd.find_element_by_link_text("Присоединиться к сообществу").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[1]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[1]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[1]/input").send_keys("Maria")
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[2]/input").send_keys("m")
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[2]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[2]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[2]/input").send_keys("maria15@toprussianbloggers.ru")
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[3]/input").click()
        wd.find_element_by_xpath("//label[@for='i-prPOPUP']").click()
        if not wd.find_element_by_id("i-prPOPUP").is_selected():
            wd.find_element_by_id("i-prPOPUP").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[3]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[3]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[3]/input").send_keys("123456")
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[4]").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[4]/input").click()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[4]/input").clear()
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[4]/input").send_keys("123456")
        wd.find_element_by_xpath("//label[@for='iaccessPOPUP']").click()
        if not wd.find_element_by_id("iaccessPOPUP").is_selected():
            wd.find_element_by_id("iaccessPOPUP").click()
        wd.find_element_by_id("register-submitPOPUP").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Личная страница").click()
        wd.find_element_by_link_text("Добавить").click()
        wd.find_element_by_id("select2-BRAND_NAME-ao-container").click()
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Готово']").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
