from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Contacts(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver

    def contacts(self):
        #self.wait_for(By.CSS_SELECTOR,".ww_operationBar .js_add_member")

        def wait_for_addmem(x):
            elements_len=len(self.finds(By.CSS_SELECTOR,"#username"))
            if elements_len<=0:
                self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            return elements_len>0
        self.wait_for_click(wait_for_addmem)
        return AddMember(self._driver)
