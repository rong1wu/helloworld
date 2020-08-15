
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testhogwarts:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.find_element(By.CSS_SELECTOR,'[id=kw]').send_keys("霍格沃兹测试学院")
        #self.driver.get("http://www.testerhome.com")
        self.driver.find_element(By.ID,'su').click()
        self.driver.find_element(By.XPATH,'//*[@id="1"]//h3[1]').click()
        # self.driver.find_element_by_link_text("社团").click()
        # self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        # self.driver.find_element_by_css_selector(".topic-24883 .title > a").click()


