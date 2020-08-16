from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver

    def add_member(self):
        #self.wait_for((By.ID,"username"))
        self.find(By.ID,"username").send_keys("abcde")
        self.find(By.ID,"memberAdd_acctid").send_keys("abcdefadbco")
        self.find(By.ID,"memberAdd_phone").send_keys("18122222222")
        self.wait_for((By.CSS_SELECTOR,'.js_btn_save'))
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        #self._driver.find_element(By.CSS_SELECTOR,".qui_btn ww_btn js_btn_save").click()
        #self._driver.quit()#用完要关掉driver

    def find_member(self):
        self.wait_for((By.CSS_SELECTOR,".ww_checkbox"))
        elements=self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        list=[]
        for element in elements:
            list.append(element.get_attribute("title"))
        return list
