# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

from Auth_facebook_TRB import myWait


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Personal_profile(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Personal_profile_2(self):
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
        myWait()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Личная страница").click()
        wd.find_element_by_id("WORK_WWW").click()
        wd.find_element_by_id("WORK_WWW").clear()
        wd.find_element_by_id("WORK_WWW").send_keys()
        wd.find_element_by_id("WORK_WWW").click()
        wd.find_element_by_id("WORK_WWW").clear()
        wd.find_element_by_id("WORK_WWW").send_keys("toprussianbloggers.ru")
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Сохранить изменения']").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Друзья").click()
        wd.find_element_by_link_text("Вы подписаны (0)").click()

        wd.find_element_by_link_text("Вы отправили заявку (0)").click()
        wd.find_element_by_name("EMAIL").click()
        wd.find_element_by_name("EMAIL").clear()
        wd.find_element_by_name("EMAIL").send_keys("irina2@toprussianbloggers.ru")
        wd.find_element_by_xpath("//div[@class='js-container-child']//button[.='Отправить']").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Сообщения").click()
        wd.find_element_by_css_selector("span.bx-messenger-input-search-create").click()
        wd.find_element_by_css_selector("a.popup-window-close-icon.popup-window-titlebar-close-icon").click()

        wd.find_element_by_link_text("Мои PR-кампании").click()
        self.assertIn("Мои кампании", wd.title)
        wd.find_element_by_link_text("Добавить новую кампанию").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Подписка").click()
        self.assertIn("Настройка уведомлений", wd.title)
        wd.find_element_by_css_selector("label.js-notify-messages").click()
        if wd.find_element_by_id("personal").is_selected():
            wd.find_element_by_id("personal").click()
        wd.find_element_by_css_selector("button.btn").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Платные услуги").click()
        wd.find_element_by_link_text("История платежей").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_xpath("//div[@class='auth-user__personal-overflow']/div[1]/a").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
