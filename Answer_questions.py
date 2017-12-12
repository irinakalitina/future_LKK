# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from settings import *
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class News_questions(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_News_questions(self):
        success = True
        wd = self.wd
        wd.get("https://toprussianbloggers.ru/")
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Пользовательское соглашение").click()
        wd.find_element_by_link_text("http://toprussianbloggers.ru/terms.php").click()
        wd.find_element_by_link_text("info@toprussianbloggers.ru").click()
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Отзывы").click()
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Новости").click()
        wd.find_element_by_link_text("Взгляд инсайдера | Популярный Instagram lifestyle-фотографа Анны Салынской").click()
        wd.find_element_by_link_text("Вернуться к списку новостей").click()
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Вопрос-ответ").click()
        wd.find_element_by_link_text("Зачем мне это, если я блогер?").click()
        wd.find_element_by_link_text("Что делать, если я случайно создал несколько аккаунтов?").click()
        wd.find_element_by_link_text("Зачем мне это, если у меня свой бренд?").click()
        wd.find_element_by_link_text("Как часто обновляется база?").click()
        wd.find_element_by_link_text("Какие категории блогеров охватывает ресурс?").click()
        wd.find_element_by_link_text("Что означает статус «Одобрено TRB» у блогера?").click()
        wd.find_element_by_link_text("Что делать, если я случайно создал несколько аккаунтов?").click()
        wd.find_element_by_link_text("PR-агенту: Как добавить свой бренд?").click()
        wd.find_element_by_link_text("Показать все ответы").click()
        wd.find_element_by_link_text("Свернуть все ответы").click()
        wd.find_element_by_css_selector("button.navbar-toggle.collapsed").click()
        wd.find_element_by_link_text("Главная").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
