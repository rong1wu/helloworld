from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.register import RegisterPage


class LoginPage:
    def __init__(self,driver: WebDriver):
        self._driver=driver
    def scanf(self):
        pass
    def goto_register(self):
        self._driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        self._driver.quit()#完成时要退出
        return RegisterPage(self._driver)