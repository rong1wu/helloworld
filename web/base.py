from selenium import webdriver
import os
class Base():

    def setup(self):
        # browser=os.getenv("browser")
        # if browser=="firefox":
        #     self.driver=webdriver.Firefox()
        # elif browser=="headless":
        #     self.driver=webdriver.PhantomJS()
        # else:
        #     self.driver=webdriver.Chrome()


        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()