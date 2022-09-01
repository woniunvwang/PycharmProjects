# encoding = 'utf-8'

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from common.baseDriver import android_driver
from common.basePage import BasePage
from pageObject.login_page import LoginPage


class NormalOrderPage(BasePage):
    confirm_button_id = (AppiumBy.ID, "com.atp.demo2:id/confirm")
    allow_button_id = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    agree_button_id = (AppiumBy.ID, "com.atp.demo2:id/agree")
    sell_side_id = (AppiumBy.ID, "com.atp.demo2:id/order_direction_sell")
    buy_side_id = (AppiumBy.ID, "com.atp.demo2:id/order_direction_buy")
    # 合约组 "自动化测试合约"的path
    contract_group_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("自动化测试合约")')

    # 页面核心元素
    page_title = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".LinearLayout/android.view.ViewGroup["
                                  "1]/android.view.ViewGroup/android.widget.TextView")  # 新单
    contract_name = (AppiumBy.ID, 'com.atp.demo2:id/contract_name_or_code')
    K_line = (AppiumBy.ID, 'com.atp.demo2:id/k_line_thumbnail')  # enabled=true
    # 合约组中第一个合约的买卖盘及涨跌幅path
    bid_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                                ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                ".HorizontalScrollView["
                                "2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                "1]/android.widget.TextView[1]")

    offer_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget"
                                  ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget"
                                  ".HorizontalScrollView["
                                  "2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                  "2]/android.widget.TextView[1]")

    Chg_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android"
                                ".widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android"
                                ".view.ViewGroup/android.view.ViewGroup/android.widget"
                                ".HorizontalScrollView["
                                "2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                "4]/android.widget.TextView[1]")

    bid_price_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                      ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                      ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                                      ".view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view"
                                      ".ViewGroup/android.widget.HorizontalScrollView["
                                      "2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                      "1]/android.widget.TextView[1]")
    bid_lots_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                     ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                     "/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout"
                                     "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
                                     "/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
                                     "/android.widget.HorizontalScrollView["
                                     "2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                     "1]/android.widget.TextView[2]")
    offer_price_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                        "/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                        ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                                        ".view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android"
                                        ".view.ViewGroup/android.widget.HorizontalScrollView["
                                        "2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                        "2]/android.widget.TextView[1]")
    offer_lots_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                       ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                                       ".view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android"
                                       ".view.ViewGroup/android.widget.HorizontalScrollView["
                                       "2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                       "2]/android.widget.TextView[2]")

    button_change_account = (AppiumBy.ID, "com.atp.demo2:id/account")
    # 选择账户中的第二个账户
    trade_account = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                     ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                     "/android.widget.LinearLayout/android.view.ViewGroup["
                                     "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView"
                                     "/android.view.ViewGroup[2]/android.widget.CheckBox")

    trade_account_text_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.widget.LinearLayout/android.view"
                                               ".ViewGroup["
                                               "2]/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                               ".widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                               ".widget.RecyclerView/android.view.ViewGroup["
                                               "2]/android.widget.TextView")
    change_account = (AppiumBy.ID, "com.atp.demo2:id/action_change")

    change_type_button = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.Button")
    type_Market_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Market")')
    type_Market_Limit_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Market Limit")')
    type_Market_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView")
    type_MarketLimit_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView")
    type_Lim_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView")
    type_STP_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.TextView")
    type_STL_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.TextView")
    type_ICE_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.TextView")

    button_time_option = (AppiumBy.XPATH,
                          "//*[@resource-id='com.atp.demo2:id/time_option']/child::android.widget.LinearLayout"
                          "/android.widget.Spinner")

    order_details_title = (AppiumBy.ID, 'com.atp.demo2:id/title')  # 订单详情

    order_details_price = (AppiumBy.XPATH,
                           "//*[@resource-id='com.atp.demo2:id/content_root']/child::android.view.ViewGroup["
                           "5]/android.widget.TextView[2]")

    button_confirm = (AppiumBy.ID, 'com.atp.demo2:id/confirm')
    alert_title = (AppiumBy.ID, 'com.atp.demo2:id/title')  # 下单请求发送成功!
    alert_contract_code = (AppiumBy.ID, 'com.atp.demo2:id/contract_code')
    alert_order_id = (AppiumBy.ID, 'com.atp.demo2:id/order_id')  # 单编号：
    alert_message_ID = (AppiumBy.ID, "com.atp.demo2:id/message")
    button_view_details = (AppiumBy.ID, 'com.atp.demo2: id/positive_button')
    button_close = (AppiumBy.ID, 'com.atp.demo2:id/close_button')

    lots_xpath = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".LinearLayout/android.view.ViewGroup["
                                  "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget"
                                  ".LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget"
                                  ".LinearLayout/android.view.ViewGroup["
                                  "2]/android.view.ViewGroup/android.widget.EditText")
    price_xpath = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.LinearLayout/android.view.ViewGroup["
                                   "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                   ".FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget"
                                   ".LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget"
                                   ".LinearLayout/android.view.ViewGroup["
                                   "3]/android.view.ViewGroup/android.widget.EditText")

    last_price_and_lots = (AppiumBy.ID, 'com.atp.demo2:id/lots_at_price')

    input_fak_min_quantity = (
        AppiumBy.XPATH,
        "//*[@resource-id='com.atp.demo2:id/min_quantity']/child::android.view.ViewGroup/android.widget.EditText")

    chunk_size_xpath = (AppiumBy.XPATH,
                                "//*[@resource-id='com.atp.demo2:id/max_iceberg_chunk_size']/child::android.view"
                                ".ViewGroup/android.widget.EditText")
    input_StPx_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.LinearLayout/android.view.ViewGroup["
                                       "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                       ".FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android"
                                       ".widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView"
                                       "/android.widget.LinearLayout/android.view.ViewGroup["
                                       "4]/android.view.ViewGroup/android.widget.EditText")

    order_time_option_DAY = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.ListView/android.widget.CheckedTextView[1]')
    order_time_option_GTC = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.ListView/android.widget.CheckedTextView[2]')
    order_time_option_GTD = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.ListView/android.widget.CheckedTextView[3]')
    order_time_option_FAK = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.ListView/android.widget.CheckedTextView[4]')
    order_time_option_FOK = (AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                             '.ListView/android.widget.CheckedTextView[5]')

    contract_management_ID = (AppiumBy.ID, "com.atp.demo2:id/manage_contract")
    # 自动化测试合约的合约管理中第一个合约的位置 TCU1907-SH （主测试合约，买卖盘有涨跌幅没有有数据）
    first_contract_drag_path = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.widget.LinearLayout/android.view"
                                                ".ViewGroup["
                                                "2]/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                                ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                ".FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view"
                                                ".ViewGroup[1]/android.widget.ImageView")
    # 自动化测试合约的合约管理中第二个合约的位置 BRN-2210-ICE（STL和STP类型下单测试合约，买卖盘及涨跌幅都有数据）
    second_contract_drag_path = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                 ".widget.FrameLayout/android.widget.LinearLayout/android.view"
                                                 ".ViewGroup["
                                                 "2]/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                                 ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                 ".FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view"
                                                 ".ViewGroup[2]/android.widget.ImageView")
    # 自动化测试合约的合约管理中第三个合约的位置 TCU1906-SH（没有数据时手数价格的填充时的测试合约，买卖盘及涨跌幅没有数据）
    third_contract_drag_path = ("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.widget.LinearLayout/android.view"
                                                ".ViewGroup["
                                                "2]/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                                ".widget.FrameLayout/android.view.ViewGroup/android.widget"
                                                ".FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view"
                                                ".ViewGroup[3]/android.widget.ImageView")
    back_button = (AppiumBy.ACCESSIBILITY_ID, "转到上一层级")
    illegal_lots_title_path = (AppiumBy.XPATH,
                               "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]")

    # 找到合约组"自动化测试合约"，
    def login_successful(self):
        loginPage = LoginPage(self.driver)
        loginPage.input_username("wangxin")
        loginPage.input_password("1")
        loginPage.press_login_button()
        loginPage.agree_disclaimers_and_get_group_name()
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(960, 325)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(700, 318)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.get_visible_element(self.contract_group_text).click()

    def press_confirm_button(self):
        confirm_button = self.get_visible_element(self.confirm_button_id)
        confirm_button.click()

    def allow_button(self):
        allow_button = self.get_visible_element(self.allow_button_id)
        allow_button.click()

    def agree_button(self):
        allow_button = self.get_visible_element(self.agree_button_id)
        allow_button.click()

    def press_bid(self):
        self.click_action(self.bid_path)

    def press_offer(self):
        self.click_action(self.offer_path)

    def change_trade_account(self):
        self.press_offer()
        self.click_action(self.button_change_account)
        trade_account_value = self.get_visible_element(self.trade_account_text_path).text
        self.click_action(self.trade_account)
        self.click_action(self.change_account)
        changed_trade_account_value = self.get_visible_element(self.button_change_account).text
        return trade_account_value, changed_trade_account_value

    def is_side_buy_checked(self):
        buy = self.get_visible_element(self.buy_side_id)
        return buy.get_attribute("checked")

    def is_side_sell_checked(self):
        return self.get_visible_element(self.sell_side_id).get_attribute("checked")

    def change_buy_side(self):
        self.press_offer()
        self.click_action(self.sell_side_id)

    def press_bid_and_check_lots(self):
        bid_lots_value = self.get_visible_element(self.bid_lots_path).text
        self.press_bid()
        lots_value = self.get_visible_element(self.lots_xpath).text
        if bid_lots_value == "-":
            return lots_value
        else:
            return bid_lots_value, lots_value

    def press_bid_and_check_price(self):
        bid_price_value = self.get_visible_element(self.bid_price_path).text
        self.press_bid()
        price_value = self.get_visible_element(self.price_xpath).text
        if bid_price_value == "-":
            return price_value
        else:
            return bid_price_value, price_value

    def press_offer_and_check_lots(self):
        offer_lots_value = self.get_visible_element(self.offer_lots_path).text
        self.press_offer()
        lots_value = self.get_visible_element(self.lots_xpath).text
        if offer_lots_value == "-":
            return lots_value
        else:
            return offer_lots_value, lots_value

    def press_offer_and_check_price(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        price_value = self.get_visible_element(self.price_xpath).text
        if offer_price_value == "-":
            return price_value
        else:
            return offer_price_value, price_value

    def slide_and_press_chg(self):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(967, 978)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(678, 978)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.click_action(self.Chg_path)
        time.sleep(1)

    def alert_illegal_lots_title(self):
        txt = self.get_visible_element(self.illegal_lots_title_path).text
        return txt

    def press_chg_and_check_lots(self):
        offer_lots_value = self.get_visible_element(self.offer_lots_path).text
        self.press_offer()
        lots_value = self.get_visible_element(self.lots_xpath).text
        if offer_lots_value == "-":
            return lots_value
        else:
            return offer_lots_value, lots_value

    def press_chg_and_check_price(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        price_value = self.get_visible_element(self.price_xpath).text
        if offer_price_value == "-":
            return price_value
        else:
            return offer_price_value, price_value

    def drag_first_contract_to_second_location(self):
        self.click_action(self.contract_management_ID)
        x = self.driver.find_element(AppiumBy.XPATH, self.third_contract_drag_path)
        y = self.driver.find_element(AppiumBy.XPATH, self.first_contract_drag_path)
        ActionChains(self.driver).drag_and_drop(y, x).pause(5).perform()
        self.click_action(self.back_button)

    def drag_third_contract_to_second_location(self):
        self.click_action(self.contract_management_ID)
        x = self.driver.find_element(AppiumBy.XPATH, self.third_contract_drag_path)
        y = self.driver.find_element(AppiumBy.XPATH, self.first_contract_drag_path)
        ActionChains(self.driver).drag_and_drop(x, y).pause(5).perform()
        self.click_action(self.back_button)

    def change_type_market(self):
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_Market_text)
        self.press_confirm_button()

    # 类型为STP/Market/Market Limit时价格处显示为置灰的Market

    def input_price_enabled_and_value(self):
        price_enabled = self.get_visible_element(self.price_xpath)
        price_value = self.get_visible_element(self.price_xpath).text
        return price_enabled.get_attribute("enabled"), price_value

    def Market_type_and_order(self):
        self.change_type_market()
        self.press_confirm_button()
        self.press_confirm_button()

    def change_type_market_Limit(self):
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_Market_Limit_text)
        self.press_confirm_button()

    def Market_Limit_type_and_order(self):
        self.change_type_market_Limit()
        self.press_confirm_button()
        self.press_confirm_button()

    def Market_type_changed_LIM_type(self):
        bid_price_value = self.get_visible_element(self.offer_price_path).text
        self.change_type_market()
        self.click_action(self.change_type_button)
        self.click_action(self.type_Lim_path)
        self.press_confirm_button()
        input_price_value = self.get_visible_element(self.price_xpath).text
        return bid_price_value, input_price_value

    def change_type_stp(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_STP_path)
        self.press_confirm_button()
        input_StPx = self.get_visible_element(self.input_StPx_path).text
        return offer_price_value, input_StPx

    def stp_clear_StPx_and_order(self):
        self.change_type_stp()
        self.clear_action(self.input_StPx_path)
        self.click_action(self.button_confirm)

    def stp_type_and_order(self):
        self.change_type_stp()
        self.press_confirm_button()
        self.press_confirm_button()

    def stp_type_input_difference_value(self, difference):
        self.change_type_stp()
        self.clear_action(self.input_StPx_path)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(difference)
        self.input_action(self.input_StPx_path, price_value)

    def stp_type_input_StPx_above_last_price_and_buy_order(self):
        self.stp_type_input_difference_value(+5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stp_type_input_StPx_below_last_price_and_buy_order(self):
        self.stp_type_input_difference_value(-5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stp_type_input_StPx_above_last_price_and_sell_order(self):
        self.stp_type_input_difference_value(+5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def stp_type_input_StPx_below_last_price_and_sell_order(self):
        self.stp_type_input_difference_value(-5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def change_type_stl(self):
        offer_price_value = self.get_visible_element(self.offer_price_path).text
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_STL_path)
        self.press_confirm_button()
        price = self.get_visible_element(self.price_xpath).text
        input_StPx = self.get_visible_element(self.input_StPx_path).text
        return offer_price_value, input_StPx, price

    def stl_type_and_order(self):
        self.change_type_stl()
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_clear_StPx_and_order(self):
        self.change_type_stl()
        self.clear_action(self.input_StPx_path)
        self.press_confirm_button()

    def stl_type_input_difference_value(self, difference):
        self.change_type_stl()
        self.clear_action(self.input_StPx_path)
        self.clear_action(self.price_xpath)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(difference)
        self.input_action(self.input_StPx_path, price_value)
        self.input_action(self.price_xpath, price_value)

    def stl_type_input_StPx_above_last_price_and_buy_order(self):
        self.stl_type_input_difference_value(+5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_below_last_price_and_buy_order(self):
        self.stl_type_input_difference_value(-5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_above_last_price_and_sell_order(self):
        self.stl_type_input_difference_value(+5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_below_last_price_and_sell_order(self):
        self.stl_type_input_difference_value(-5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_diff_and_price_diff(self, StPx_diff, price_diff):
        self.change_type_stl()
        self.clear_action(self.input_StPx_path)
        self.clear_action(self.price_xpath)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots).text
        last_trade_price = float(last_price_and_lots.split('@')[1])
        price_value = last_trade_price + int(price_diff)
        StPx_value = last_trade_price + int(StPx_diff)
        self.input_action(self.input_StPx_path, StPx_value)
        self.input_action(self.price_xpath, price_value)

    def stl_type_input_StPx_below_price_and_buy_order(self):
        self.stl_type_input_StPx_diff_and_price_diff(5, 10)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_above_price_and_buy_order(self):
        self.stl_type_input_StPx_diff_and_price_diff(10, 5)
        self.press_confirm_button()
        self.press_confirm_button()

    def stl_type_input_StPx_below_price_and_sell_order(self):
        self.stl_type_input_StPx_diff_and_price_diff(-10, -5)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()

    def stl_type_input_StPx_above_price_and_sell_order(self):
        self.stl_type_input_StPx_diff_and_price_diff(-5, -10)
        self.click_action(self.sell_side_id)
        self.press_confirm_button()
        self.press_confirm_button()

    def change_type_ice(self):
        self.press_offer()
        self.click_action(self.change_type_button)
        self.click_action(self.type_ICE_path)
        self.press_confirm_button()
        chunk_size_value = self.get_visible_element(self.chunk_size_xpath).text
        return chunk_size_value

    def ice_type_and_input_chunk_size(self, chunk_size_value):
        self.change_type_ice()
        self.clear_action(self.chunk_size_xpath)
        self.input_action(self.chunk_size_xpath, chunk_size_value)
        chunk_size_value = self.get_visible_element(self.chunk_size_xpath).text
        return chunk_size_value

    def ice_type_and_input_lots_and_chunk_size(self, lots, chunk_size_value):
        self.change_type_ice()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.clear_action(self.chunk_size_xpath)
        self.input_action(self.chunk_size_xpath, chunk_size_value)
        lots_value = self.get_visible_element(self.lots_xpath).text
        chunk_size_value = self.get_visible_element(self.chunk_size_xpath).text
        return lots_value, chunk_size_value

    def ice_type_clear_chunk_size_and_order(self):
        self.change_type_ice()
        self.clear_action(self.chunk_size_xpath)
        self.press_confirm_button()










    def ice_clear_iceberg_chunk_size_and_sell(self):
        self.change_type_ice()
        self.click_action(self.press_offer)
        self.clear_action(self.chunk_size_xpath)
        self.click_action(self.button_confirm)

    def ice_iceberg_chunk_size_input_above_lots_and_buy(self, lots, iceberg_chunk_size):
        self.change_type_ice()
        self.click_action(self.press_offer)
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.clear_action(self.chunk_size_xpath)
        self.input_action(self.chunk_size_xpath, iceberg_chunk_size)
        iceberg_chunk_size = self.get_visible_element(self.chunk_size_xpath).text
        self.click_action(self.button_confirm)
        self.click_action(self.button_confirm)
        return iceberg_chunk_size

    def clear_lots_and_order(self):
        self.press_bid()
        self.clear_action(self.lots_xpath)
        self.click_action(self.button_confirm)

    def clear_price_and_order(self):
        self.press_offer()
        self.clear_action(self.price_xpath)
        self.click_action(self.button_confirm)

    def clear_fak_min_quantity_and_order(self):
        self.press_offer()
        self.click_action(self.button_time_option)
        self.click_action(self.order_time_option_FAK)
        self.clear_action(self.input_fak_min_quantity)
        self.click_action(self.button_confirm)

    def fak_min_quantity_input_below_lots_and_order(self, lots, fak_min):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.click_action(self.button_time_option)
        self.click_action(self.order_time_option_FAK)
        self.clear_action(self.input_fak_min_quantity)
        self.input_action(self.input_fak_min_quantity, fak_min)
        fak_min_quantity = self.get_visible_element(self.input_fak_min_quantity).text
        self.click_action(self.button_confirm)
        self.click_action(self.button_confirm)
        return fak_min_quantity

    def fak_min_quantity_input_above_lots_and_order(self, lots, min_quantity):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.click_action(self.button_time_option)
        self.click_action(self.order_time_option_FAK)
        self.clear_action(self.input_fak_min_quantity)
        self.input_action(self.input_fak_min_quantity, min_quantity)
        new_fak_min_quantity = self.get_visible_element(self.input_fak_min_quantity).text
        return new_fak_min_quantity

    def input_illegal_lots_and_order(self, lots):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.click_action(self.button_confirm)

    def input_illegal_price_and_order(self, price):
        self.press_offer()
        self.clear_action(self.price_xpath)
        self.input_action(self.price_xpath, price)
        self.click_action(self.button_confirm)
        self.click_action(self.button_confirm)

    def input_lots_and_price_and_order(self, lots, price):
        self.press_offer()
        self.clear_action(self.lots_xpath)
        self.input_action(self.lots_xpath, lots)
        self.clear_action(self.price_xpath)
        self.input_action(self.price_xpath, price)
        self.click_action(self.button_confirm)
        self.click_action(self.button_confirm)

    def get_element_from_send_successfully_alert_and_close_alert(self):
        alert_title = self.get_visible_element(self.alert_title).text
        alert_contract_code = self.get_visible_element(self.alert_contract_code).text
        alert_order_id = self.get_visible_element(self.alert_order_id).text
        self.click_action(self.button_close)
        return alert_title, alert_contract_code, alert_order_id

    def market_input_lots_and_sell(self):
        self.change_type_market()
        self.click_action(self.press_offer)
        price_text = self.get_visible_element(self.price_xpath).text
        self.click_action(self.button_confirm)
        order_details_title = self.get_visible_element(self.order_details_title).text
        order_details_price = self.get_visible_element(self.order_details_price).text
        self.click_action(self.button_confirm)
        return price_text, order_details_title, order_details_price

    def market_input_lots_and_buy(self):
        self.change_type_market()
        self.click_action(self.press_offer)
        price_text = self.get_visible_element(self.price_xpath).text
        self.click_action(self.button_confirm)
        order_details_title = self.get_visible_element(self.order_details_title).text
        order_details_price = self.get_visible_element(self.order_details_price).text
        self.click_action(self.button_confirm)
        return price_text, order_details_title, order_details_price

    def alert_order_details_message(self):
        return self.get_visible_element(self.alert_message_ID).text

if __name__ == '__main__':
    driver = android_driver()
    # a = NewOrderPage(driver)
    # a.login_successful()
    # a.slide_contract_group_and_go_to_new_order_page()
