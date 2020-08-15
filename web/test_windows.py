from selenium.webdriver import ActionChains

from web.base import Base
from time import sleep
import pytest
class TestWindow(Base):
    @pytest.mark.skip
    def test_windows(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)#当前窗口句柄
        print(self.driver.window_handles)#所有窗口句柄
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)  # 当前窗口句柄
        print(self.driver.window_handles)  # 所有窗口句柄
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1]) #切换到新窗口句柄

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        sleep(3)

        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()

        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
    @pytest.mark.skip
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame()#切换到父节点
        #self.driver.switch_to.default_content()  默认Frame
        print(self.driver.find_element_by_id("submitBTN").text)
    @pytest.mark.skip
    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        #self.driver.find_element_by_id("su")
        ele=self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        sleep(3)
        self.driver.execute_script("document.documentElement.scrollTop=10000")#用JS的方式滑动页面到最底端
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'#性能数据指标分析
        ]:
            print(self.driver.execute_script(code))
    @pytest.mark.skip
    def test_js12306(self):
        self.driver.get("https://www.12306.cn/index/")
        time_ele=self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-31'")
        sleep(3)
        print(self.driver.execute_script("document.getElementById('train_date').value='2020-12-31'"))
    @pytest.mark.skip
    def test_uploadimage(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_id("sttb").click()
        self.driver.find_element_by_id("uploadImg").send_keys("D:\pydj\hogwards\/testpython\web\icon.png")
        sleep(3)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag_ele=self.driver.find_element_by_id("draggable")
        drop_ele=self.driver.find_element_by_id("droppable")
        action=ActionChains(self.driver)
        action.drag_and_drop(drag_ele,drop_ele).perform()#开始拖拽

        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()

        self.driver.find_element_by_id("submitBTN").click()
        sleep(3) 



