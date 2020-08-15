from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self._driver=driver
    def register(self):
        #send content
        #click
        sleep(2)
        #self._driver.find_element(By.ID,"corp_name").click()
        self._driver.find_element(By.ID, "corp_name").send_keys("HEllo")
        #self._driver.find_element(By.ID,"manager_name").click()
        self._driver.find_element(By.ID,"manager_name").send_keys("hello11111")
        sleep(5)
        self._driver.quit()
        return True

