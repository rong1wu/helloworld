from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
import pytest
import time

from selenium.webdriver.common.keys import Keys


class TestActionChains:

    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(options=option) #使用时要将chromedriver配置到环境变量中
        self.driver.maximize_window()
        #self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def testcaseclick(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click=self.driver.find_element_by_xpath("//input[@value='click me']")
        element_dbclick=self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick=self.driver.find_element_by_xpath("//input[@value='right click me']")
        action=ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_dbclick)
        action.context_click(element_rightclick)
        time.sleep(3)
        action.perform()
        time.sleep(3)
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        clicks=self.driver.find_element_by_xpath("//span[@id='s-usersetting-top']")
        action=ActionChains(self.driver)
        action.move_to_element(clicks)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_dragtoelement(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element=self.driver.find_element_by_id("dragger")
        drop_element=self.driver.find_element_by_xpath("//div[@class='item'][1]")
        action=ActionChains(self.driver)
        action.drag_and_drop(drag_element,drop_element).perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        clc=self.driver.find_element_by_xpath("//input[@type='textbox']")
        action=ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)
    @pytest.mark.skip
    def test_touchAction_scollbottom(self):
        self.driver.get("https://www.baidu.com/")
        clc=self.driver.find_element_by_id("kw")
        clc.send_keys("selenium测试")
        clc2=self.driver.find_element_by_id("su")
        action= TouchActions(self.driver)
        action.tap(clc2).perform()

        action.scroll_from_element(clc2,0,10000).perform()
        time.sleep(5)

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("18023037341")
        self.driver.find_element_by_id("user_password").send_keys("1234567l")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[4]/input")
        time.sleep(3)



if __name__=='__main__':
    pytest.main(['-v','-s','selenium_event.py'])
