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
    
    def test_Personal_profile(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Главная").click()
        wd.find_element_by_link_text("Присоединиться к сообществу").click()
        wd.find_element_by_xpath("//label[@for='i-prPOPUP']").click()
        if not wd.find_element_by_id("i-prPOPUP").is_selected():
            wd.find_element_by_id("i-prPOPUP").click()
        wd.find_element_by_id("NAME").click()
        wd.find_element_by_id("NAME").clear()
        wd.find_element_by_id("NAME").send_keys("Maria")
        wd.find_element_by_xpath("//div[@class='modal-body']/div/form/div[3]/div[2]").click()
        wd.find_element_by_id("EMAIL").click()
        wd.find_element_by_id("EMAIL").clear()
        wd.find_element_by_id("EMAIL").send_keys("maria16@toprussianbloggers.ru")
        wd.find_element_by_id("PASSWORD").click()
        wd.find_element_by_id("PASSWORD").clear()
        wd.find_element_by_id("PASSWORD").send_keys("123456")
        wd.find_element_by_id("CONFIRM_PASSWORD").click()
        wd.find_element_by_id("CONFIRM_PASSWORD").clear()
        wd.find_element_by_id("CONFIRM_PASSWORD").send_keys("123456")
        wd.find_element_by_css_selector("label.form-register__label-personal").click()
        if not wd.find_element_by_id("iaccessPOPUP").is_selected():
            wd.find_element_by_id("iaccessPOPUP").click()
        wd.find_element_by_id("register-submitPOPUP").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Личная страница").click()
        myWait()
        wd.find_element_by_link_text("Добавить").click()
        wd.find_element_by_xpath("//form[@id='lk_form']/div/div[1]/div[2]/div/div/div[8]/div/div[2]/div[2]/div[1]/div[1]/span/span[1]/span/span[2]").click()
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Готово']").click()
        myWait()
        wd.find_element_by_id("WORK_COMPANY").click()
        wd.find_element_by_id("WORK_COMPANY").clear()
        wd.find_element_by_id("WORK_COMPANY").send_keys("Toprussianbloggers")
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Сохранить изменения']").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Контакты").click()
        wd.find_element_by_name("EMAIL").click()
        wd.find_element_by_name("EMAIL").clear()
        wd.find_element_by_name("EMAIL").send_keys("maria16@toprussianbloggers.ry")
        wd.find_element_by_xpath("//div[@class='js-container-child']//button[.='Отправить']").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Личная страница").click()
        wd.find_element_by_link_text("Добавить").click()
        wd.find_element_by_id("select2-BRAND_NAME-ao-container").click()
        wd.find_element_by_xpath("//form[@id='lk_form']//button[.='Готово']").click()
        wd.find_element_by_link_text("Сообщения").click()
        wd.find_element_by_css_selector("input.bx-messenger-input").click()
        wd.find_element_by_css_selector("input.bx-messenger-input").clear()
        wd.find_element_by_css_selector("input.bx-messenger-input").send_keys("maria")
        wd.find_element_by_css_selector("div.bx-messenger-cl-user-title").click()
        wd.find_element_by_css_selector("a.popup-window-close-icon.popup-window-titlebar-close-icon").click()
        wd.find_element_by_xpath("//div[@class='auth-user__personal-overflow']/div[1]/a").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Мои PR-кампании").click()
        wd.find_element_by_link_text("Добавить новую кампанию").click()
        wd.find_element_by_id("NAME").click()
        wd.find_element_by_id("NAME").clear()
        wd.find_element_by_id("NAME").send_keys("Maria Way")
        wd.find_element_by_id("DATE_START").click()
        wd.find_element_by_link_text("27").click()
        wd.find_element_by_id("DATE_END").click()
        wd.find_element_by_link_text("30").click()
        wd.find_element_by_id("SET_TO").click()
        wd.find_element_by_link_text("30").click()
        wd.find_element_by_css_selector("li.select2-search.select2-search--inline").click()
        wd.find_element_by_css_selector("span.select2-selection__arrow").click()
        wd.find_element_by_id("select2-CITY-container").click()
        wd.find_element_by_xpath("//div[@class='ms-options-wrap']//span[.='Выбрать']").click()
        if not wd.find_element_by_id("ms-opt-136").is_selected():
            wd.find_element_by_id("ms-opt-136").click()
        if not wd.find_element_by_id("ms-opt-139").is_selected():
            wd.find_element_by_id("ms-opt-139").click()
        wd.find_element_by_xpath("//div[@class='campaign-form']/div[10]").click()
        wd.find_element_by_id("PRODUCT_DESCRIPTION").click()
        wd.find_element_by_id("PR_DESCRIPTION").click()
        wd.find_element_by_id("PR_DESCRIPTION").clear()
        wd.find_element_by_id("PR_DESCRIPTION").send_keys("Maria Way")
        wd.find_element_by_id("PRODUCT_DESCRIPTION").click()
        wd.find_element_by_id("PRODUCT_DESCRIPTION").clear()
        wd.find_element_by_id("PRODUCT_DESCRIPTION").send_keys("fedfew")
        wd.find_element_by_id("MEDIAPERSONS").click()
        wd.find_element_by_id("MEDIAPERSONS").clear()
        wd.find_element_by_id("MEDIAPERSONS").send_keys("efewfdew")
        wd.find_element_by_id("DEMANDS").click()
        wd.find_element_by_id("DEMANDS").clear()
        wd.find_element_by_id("DEMANDS").send_keys("fedfew")
        wd.find_element_by_id("STYLISTICS").click()
        wd.find_element_by_id("STYLISTICS").clear()
        wd.find_element_by_id("STYLISTICS").send_keys("dfewdew")
        wd.find_element_by_xpath("//div[@class='campaign-form']/div[8]/span/span[1]/span/span[2]").click()
        wd.find_element_by_css_selector("button.btn.margin-bottom-10").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Сообщения").click()
        wd.find_element_by_css_selector("a.popup-window-close-icon.popup-window-titlebar-close-icon").click()
        wd.find_element_by_link_text("Подписка").click()
        wd.find_element_by_css_selector("label.js-notify-messages").click()
        if wd.find_element_by_id("personal").is_selected():
            wd.find_element_by_id("personal").click()
        wd.find_element_by_css_selector("label.js-notify-system").click()
        if wd.find_element_by_id("friends").is_selected():
            wd.find_element_by_id("friends").click()
        wd.find_element_by_xpath("//label[@for='requests']").click()
        if wd.find_element_by_id("requests").is_selected():
            wd.find_element_by_id("requests").click()
        wd.find_element_by_xpath("//label[@for='news']").click()
        if wd.find_element_by_id("news").is_selected():
            wd.find_element_by_id("news").click()
        wd.find_element_by_css_selector("button.btn").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Платные услуги").click()
        wd.find_element_by_link_text("История платежей").click()
        wd.find_element_by_link_text("Maria").click()
        wd.find_element_by_link_text("Личная страница").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
