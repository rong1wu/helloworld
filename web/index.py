from selenium import webdriver
from selenium.webdriver.common.by import By

from web.login import LoginPage
from web.register import RegisterPage



class Index:
    def __init__(self):
        self._driver=webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")
    def goto_login(self):
        self._driver.find_element(By.XPATH,'//a[@class="index_top_operation_loginBtn"]').click()
        #self._driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self._driver)

    def goto_register(self):
        self._driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self._driver)
