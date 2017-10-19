# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import  unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class authorization_future(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_authorization_future(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "149-027-332 58", "11043212")
        self.edit_profile_info(success, wd)

    def open_home_page(self, wd):
        wd.get("https://futurenpf.ru/personal/")

    def edit_profile_info(self, success, wd):
        wd.find_element_by_xpath("//main[@class='main']/section[2]/div/div[2]/div/div/div[2]/a").click()
        wd.find_element_by_link_text("Калитина Ирина").click()
        wd.find_element_by_link_text("Изменить контактные данные").click()
        wd.find_element_by_link_text("Образование и работа").click()
        wd.find_element_by_xpath("//div[@class='profile-steps']/div[2]/div/div/div[1]/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@class='profile-steps']//li[.='Неполное среднее']").click()
        wd.find_element_by_xpath("//div[@class='profile-steps']/div[2]/div/div/div[2]/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@class='profile-steps']//li[.='Административный персонал']").click()
        wd.find_element_by_xpath("//div[@class='profile-steps']/div[2]/div/div/div[3]/div[2]/div/div").click()
        wd.find_element_by_xpath("//div[@class='profile-steps']/div[2]/div/div/div[3]/div[2]/div/ul/li[4]").click()
        wd.find_element_by_xpath("//div[@class='lc-bottomnav__center']/input").click()
        wd.find_element_by_link_text("Образование и работа").click()
        wd.find_element_by_link_text("Калитина Ирина").click()
        wd.find_element_by_css_selector("a.top-bar__arrow.js-lcopen").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)

    def login(self, wd, snils, password):
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").click()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").clear()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[2]/input").send_keys("%s" % snils)
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").click()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").clear()
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[3]/div[2]/input").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@class='lc-auth-form-component']/div[4]/input").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
