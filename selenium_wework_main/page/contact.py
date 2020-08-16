from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Contacts(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self._driver=driver

    def contacts(self):
        #self.wait_for((By.CSS_SELECTOR,".ww_operationBar .js_add_member"))
        #sleep(3)
        # locator=(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # WebDriverWait(self._driver,10).until(expected_conditions.element_to_be_clickable(locator))
        #self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()

        def wait_for_addmem(x):  #通过下一个页面的元素来反馈上一个页面点击行为
            elements_len=len(self.finds(By.CSS_SELECTOR,"#username"))
            if elements_len<=0:
                self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            return elements_len>0
        self.wait_for_click(wait_for_addmem)
        return AddMember(self._driver)
