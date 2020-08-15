from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""
    def __init__(self,driver:WebDriver=None):

        if driver is None:
            #浏览器复用
            options=Options()
            options.debugger_address="127.0.0.1:9222"
            self._driver=webdriver.Chrome(options=options)
            #self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self._driver=driver
        if self._base_url!="":
            self._driver.get(self._base_url)


#为了将driver分离
    def find(self,by,locator):
        return self._driver.find_element(by,locator)
    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)
    #显示等待
    def wait_for(self,locator,time=10):
        return WebDriverWait(self._driver,time).until(expected_conditions.element_to_be_clickable(locator))
    def wait_for_click(self,conditions,time=10):
        return WebDriverWait(self._driver,time).until(conditions)