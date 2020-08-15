from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage
from selenium_wework_main.page.contact import Contacts


class Main(BasePage):
    # def __init__(self):
    #     #浏览器复用
    #     options=Options()
    #     options.debugger_address="127.0.0.1:9222"
    #     self._driver=webdriver.Chrome(options=options)
    #     self._driver.get("https://work.weixin.qq.com/wework_admin/frame")

    _base_url="https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        #click add member
        self.wait_for(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)")
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self._driver)

    def goto_contacts(self):
        #self.wait_for(By.ID,"menu_index")
        #WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable)
        self.find(By.ID,"menu_index").click()
        return Contacts(self._driver)