import time
import unittest

from PycharmProjects.ProjectAuto.common.baseDriver import android_driver
from PycharmProjects.ProjectAuto.pageObject.login_page import LoginPage
from PycharmProjects.ProjectAuto.pageObject.normalOrder_page import NormalOrderPage


class CaseNormalOrder(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = android_driver()
        self.normal_order_page = None

    def setUp(self) -> None:
        loginPage1 = LoginPage(self.driver)
        loginPage1.input_username("wangxin")
        loginPage1.input_password("1")
        loginPage1.press_login_button()
        el1 = self.driver.find_element_by_id("com.atp.demo2:id/agree")
        el1.click()
        time.sleep(1)
        el2 = self.driver.find_element_by_id("com.atp.demo2:id/agree")
        el2.click()

        self.normal_order_page = NormalOrderPage(self.driver)
        # # alert_title, alert_content, group_name = cls.NormalOrderPage.login_successful()
        # group_name = self.normalOrderPage.login_successful()
        # assert alert_title == '登录失败'
        # assert alert_content == '请勾选勾选框来同意搜集必需的信息'
        # assert group_name == '金属'
        # page_title, contract_name, k_line = cls.NormalOrderPage.slide_contract_group_and_go_to_new_order_page()
        # assert page_title == '新单'
        # assert contract_name == 'BRN2209-ICE'
        # assert k_line is True
        # time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    #     cls.driver.close_app()

    def test_01_normalOrder_successful(self):
        self.driver.find_element_by_id("com.atp.demo2:id/bottom_value").click()
        el3 = self.driver.find_element_by_id("com.atp.demo2:id/confirm")
        el3.click()
        time.sleep(0.5)
        el4 = self.driver.find_element_by_id("com.atp.demo2:id/confirm")
        el4.click()
        time.sleep(1)
        alert_title = self.driver.find_element_by_id('com.atp.demo2:id/title').text
        # alert_title = self.normal_order_page.get_visible_element(self.normal_order_page.send_successfully_alert_title).text
        self.assertEquals(alert_title, "下单请求发送成功!")

    def test_02_normalOrder_fail(self):
        self.driver.find_element_by_id("com.atp.demo2:id/bottom_value").click()
        self.normal_order_page.clear_action(self.normal_order_page.input_lots)
        el5 = self.driver.find_element_by_id("com.atp.demo2:id/confirm")
        el5.click()
        time.sleep(1)
        alert_title = self.normal_order_page.is_toast_exist("请输入手数")
        self.assertEquals(True, alert_title)
