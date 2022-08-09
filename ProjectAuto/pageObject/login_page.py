from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from common.baseDriver import android_driver
from common.basePage import BasePage


class LoginPage(BasePage):
    usernameID = (AppiumBy.ID, 'com.atp.demo2:id/username')
    passwordID = (By.ID, 'com.atp.demo2:id/password')
    login_button_ID = (By.ID, 'com.atp.demo2:id/sign_in_button')
    error_alert_title_ID = (By.ID, "com.atp.demo2:id/title")
    error_alert_content_ID = (By.ID, "com.atp.demo2:id/content_view")
    alert_title_ID = (By.ID, "com.atp.demo2:id/disclaimer_title")

    def __init__(self, driver):
        super().__init__(driver)

    def get_alert_title_UI_element(self):
        return self.get_visible_element(self.error_alert_title_ID)

    def get_login_button(self):
        return self.get_visible_element(self.login_button_ID)

    def get_alert_content_UI_element(self):
        return self.get_visible_element(self.error_alert_content_ID)

    def get_alert_title_ID(self):
        return self.get_visible_element(self.alert_title_ID)

    def input_username(self, text):
        self.input_action(self.usernameID, text)

    def input_password(self, text):
        self.input_action(self.passwordID, text)

    def press_login_button(self):
        login_button = self.get_visible_element(self.login_button_ID)
        login_button.click()

    def login_action(self, username, password):
        # self.username = username
        # self.password = password
        self.input_username(username)
        self.input_password(password)
        self.press_login_button()

    def press_change_password(self):
        self.click_action()

    def press_change_server(self):
        pass

    # # 页面核心业务流
    # def login_action(self, username, password):
    #     self.input_action(self.username_loc, username)
    #     self.input_action(self.password_loc, password)
    #     self.click_action(self.login_button_loc)
    #
    # def login_failed_alert_handle(self):
    #     alert_title = self.get_visible_element(self.alert_title).text
    #     alert_content = self.get_visible_element(self.alert_content).text
    #     self.click_action(self.alert_cancel)
    #     return alert_title, alert_content
    #
    # def agree_information_collection(self):
    #     self.click_action(self.information_collection_allow)
    #     try:
    #         self.click_action(self.allow_position)
    #         self.click_action(self.allow_reading_messages)
    #         self.click_action(self.allow_reading_messages)
    #         self.click_action(self.login_button_loc)
    #     except:
    #         self.click_action(self.login_button_loc)
    #
    # def allow_root(self):
    #     try:
    #         self.click_action(self.allow_position)
    #         self.click_action(self.allow_reading_messages)
    #         self.click_action(self.allow_reading_messages)
    #     except:
    #         pass
    #
    def agree_disclaimers_and_get_group_name(self):
        try:
            self.click_action(self.agree_disclaimer)
            self.click_action(self.agree_disclaimer)
            group_name = self.get_visible_element(self.group_title_name).text
            return group_name
        except:
            group_name = self.get_visible_element(self.group_title_name).text
            return group_name


# alert_title = (By.ID, "com.atp.demo2:id/title")
# alert_content = (By.ID, "com.atp.demo2:id/content_view")
# alert_cancel = (By.ID, "com.atp.demo2:id/cancel")
# information_collection_allow = (By.ID, "com.atp.demo2:id/checkBox_allow_collect_system_information")
#
# allow_position = (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
# allow_reading_messages = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
#
# agree_disclaimer = (By.ID, "com.atp.demo2:id/agree")
# group_title_name = (By.ID, "com.atp.demo2:id/group_title_name")

# if __name__ == '__main__':

    # driver = android_driver()
    # user = 'atpwangx'
    # pwd = '1'
    # a = LoginPage(driver)
    # a.login_action(user, pwd)
