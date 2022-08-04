# encoding = 'utf-8'
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time

from PycharmProjects.ProjectAuto.common.baseDriver import android_driver
from PycharmProjects.ProjectAuto.common.basePage import BasePage
from PycharmProjects.ProjectAuto.pageObject.login_page import LoginPage


class NormalOrderPage(BasePage):
    # com.atp.demo2: id / contract_name BRN2208-ICE    com.atp.demo2:id/title 订单详情  发送成交 请输入手数 请输入价格 请输入Stop price  Stop price需大于等于价格

    # 页面核心元素
    # page_title = (By.ID, 'com.atp.demo2:id/toolbar_title')  # 新单
    page_title = (By.XPATH, "//*[@resource-id='com.atp.demo2:id/toolbar']/child::android.widget.TextView")  # 新单
    # contract_name = (By.ID, 'com.atp.demo2:id/contract_name') #BRN2203-ICE
    # contract_name = (By.XPATH, "//*[@resource-id='com.atp.demo2:id/total_trade_lots']/preceding-sibling::android.widget.TextView")
    contract_name = (By.ID, 'com.atp.demo2:id/contract_name_or_code')
    k_line = (By.ID, 'com.atp.demo2:id/k_line_thumbnail')  # enabled=true

    # offer_price = (By.ID, 'com.atp.demo2:id/offer_price')
    offer_price = (By.XPATH,
                   "//*[@resource-id='com.atp.demo2:id/right_bottom_list']/child::android.view.ViewGroup[2]/android.widget.TextView[1]")
    button_change_account = (By.XPATH,
                             "//*[@resource-id='com.atp.demo2:id/account_spinner']/child::android.widget.LinearLayout/android.widget.Spinner")
    button_type = (By.ID, 'com.atp.demo2:id/type')
    button_time_option = (By.XPATH,
                          "//*[@resource-id='com.atp.demo2:id/time_option']/child::android.widget.LinearLayout/android.widget.Spinner")
    button_buy = (By.ID, 'com.atp.demo2:id/buy')
    button_sell = (By.ID, 'com.atp.demo2:id/sell')
    order_details_title = (By.ID, 'com.atp.demo2:id/title')  # 订单详情
    order_details_price = (By.XPATH,
                           "//*[@resource-id='com.atp.demo2:id/content_root']/child::android.view.ViewGroup[5]/android.widget.TextView[2]")
    button_confirm = (By.ID, 'com.atp.demo2:id/confirm')
    send_successfully_alert_title = (By.ID, 'com.atp.demo2:id/title')  # 下单请求发送成功!
    send_successfully_alert_contract_code = (By.ID, 'com.atp.demo2:id/contract_code')  # BRN2203-ICE
    send_successfully_alert_order_id = (By.ID, 'com.atp.demo2:id/order_id')  # 单编号：
    button_view_details = (By.ID, 'com.atp.demo2: id/positive_button')
    button_close = (By.ID, 'com.atp.demo2:id/close_button')

    input_lots = (
    By.XPATH, "//*[@resource-id='com.atp.demo2:id/lots']/child::android.view.ViewGroup/android.widget.EditText")
    input_price = (
    By.XPATH, "//*[@resource-id='com.atp.demo2:id/price']/child::android.view.ViewGroup/android.widget.EditText")
    input_stop_price = (
    By.XPATH, "//*[@resource-id='com.atp.demo2:id/stop_price']/child::android.view.ViewGroup/android.widget.EditText")
    # last_price_and_lots = (By.ID, 'com.atp.demo2:id/last_price_and_lots')
    last_price_and_lots = (By.ID, 'com.atp.demo2:id/lots_at_price')
    input_fak_min_quantity = (
    By.XPATH, "//*[@resource-id='com.atp.demo2:id/min_quantity']/child::android.view.ViewGroup/android.widget.EditText")
    input_iceberg_chunk_size = (By.XPATH,
                                "//*[@resource-id='com.atp.demo2:id/max_iceberg_chunk_size']/child::android.view"
                                ".ViewGroup/android.widget.EditText")

    order_type_Market = (By.XPATH,
                         '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView'
                         '/android.widget.CheckedTextView[1]')
    order_type_Lim = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')
    order_type_STP = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]')
    order_type_STL = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]')
    order_type_ICE = (By.XPATH,
                      '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]')

    order_time_option_DAY = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]')
    order_time_option_GTC = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]')
    order_time_option_GTD = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]')
    order_time_option_FAK = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[4]')
    order_time_option_FOK = (By.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[5]')

    def __init__(self, driver):
        super().__init__(driver)
        self.LoginPage = LoginPage(self.driver)

    def login_successful(self):
        self.LoginPage.login_action('wangxin', '1')
        # 处理信息采集弹窗，若测试账户不需采集信息，则可注释掉65、66、71，并启用72
        # alert_title, alert_content = self.LoginPage.login_failed_alert_handle()
        # self.LoginPage.agree_information_collection()
        # 安装后首次登录会弹出授权系统权限的弹窗，若非首次则可注释掉
        # self.lp.allow_root()
        group_name = self.LoginPage.agree_disclaimers_and_get_group_name()
        time.sleep(1)
        # return alert_title, alert_content, group_name
        return group_name

    # 页面核心业务流
    # 滑动合约组，点击第一个自定义合约组,点击第三个合约'BRN2209-ICE'
    def slide_contract_group_and_go_to_new_order_page(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        TouchAction(self.driver).move_to(x=868, y=366)
        TouchAction(self.driver).long_press(x=width * 18 / 25, y=height * 4 / 25).move_to(x=width * 6 / 25,
                                                                                          y=height * 4 / 25).release().perform()
        time.sleep(2)
        TouchAction(self.driver).tap(x=width * 2 / 3, y=height * 4 / 25).perform()
        TouchAction(self.driver).move_to(x=width * 17 / 25, y=height * 19 / 50)
        time.sleep(2)
        TouchAction(self.driver).tap(x=width * 17 / 25, y=height * 19 / 50).perform()
        page_title = self.get_visible_element(self.page_title).text
        contract_name = self.get_visible_element(self.contract_name).text
        k_line = self.get_element_clickable(self.k_line)
        return page_title, contract_name, k_line

    def change_order_type_market(self):
        self.click_action(self.button_type)
        type_market = self.get_visible_element(self.order_type_Market).text
        self.click_action(self.order_type_Market)
        return type_market

    def change_order_type_stp(self):
        self.click_action(self.button_type)
        type_stp = self.get_visible_element(self.order_type_STP).text
        self.click_action(self.order_type_STP)
        return type_stp

    def change_order_type_stl(self):
        self.click_action(self.button_type)
        type_stl = self.get_visible_element(self.order_type_STL).text
        self.click_action(self.order_type_STL)
        return type_stl

    def change_order_type_ice(self):
        self.click_action(self.button_type)
        type_ice = self.get_visible_element(self.order_type_ICE).text
        self.click_action(self.order_type_ICE)
        return type_ice

    def clear_lots_and_buy(self):
        self.click_action(self.offer_price)
        self.clear_action(self.input_lots)
        self.click_action(self.button_buy)

    def clear_lots_and_sell(self):
        self.click_action(self.offer_price)
        self.clear_action(self.input_lots)
        self.click_action(self.button_sell)

    def clear_price_and_buy(self):
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        self.click_action(self.button_buy)

    def clear_price_and_sell(self):
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        self.click_action(self.button_sell)

    def clear_fak_min_quantity_and_buy(self):
        self.click_action(self.offer_price)
        self.click_action(self.button_time_option)
        self.click_action(self.order_time_option_FAK)
        self.clear_action(self.input_fak_min_quantity)
        self.click_action(self.button_buy)

    def clear_fak_min_quantity_and_sell(self):
        self.click_action(self.offer_price)
        self.click_action(self.button_time_option)
        self.click_action(self.order_time_option_FAK)
        self.clear_action(self.input_fak_min_quantity)
        self.click_action(self.button_sell)

    def fak_min_quantity_input_above_lots_and_buy(self, lots, fak_min_quantity):
        self.click_action(self.offer_price)
        self.clear_action(self.input_lots)
        self.input_action(self.input_lots, lots)
        self.click_action(self.button_time_option)
        self.click_action(self.order_time_option_FAK)
        self.clear_action(self.input_fak_min_quantity)
        self.input_action(self.input_fak_min_quantity, fak_min_quantity)
        fak_min_quantity = self.get_visible_element(self.input_fak_min_quantity).text
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)
        return fak_min_quantity

    def fak_min_quantity_input_above_lots_and_sell(self, lots, fak_min_quantity):
        self.click_action(self.offer_price)
        self.clear_action(self.input_lots)
        self.input_action(self.input_lots, lots)
        self.click_action(self.button_time_option)
        self.click_action(self.order_time_option_FAK)
        self.clear_action(self.input_fak_min_quantity)
        self.input_action(self.input_fak_min_quantity, fak_min_quantity)
        fak_min_quantity = self.get_visible_element(self.input_fak_min_quantity).text
        self.click_action(self.button_sell)
        self.click_action(self.button_confirm)
        return fak_min_quantity

    def fill_price_lots_and_buy(self):
        self.click_action(self.offer_price)
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)

    def fill_price_lots_and_sell(self):
        self.click_action(self.offer_price)
        self.click_action(self.button_sell)
        self.click_action(self.button_confirm)

    def input_lots_price_and_buy(self, lots, price):
        self.clear_action(self.input_lots)
        self.input_action(self.input_lots, lots)
        self.clear_action(self.input_price)
        self.input_action(self.input_price, price)
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)

    def input_lots_price_and_sell(self, lots, price):
        self.clear_action(self.input_lots)
        self.input_action(self.input_lots, lots)
        self.clear_action(self.input_price)
        self.input_action(self.input_price, price)
        self.click_action(self.button_sell)
        self.click_action(self.button_confirm)

    def get_element_from_send_successfully_alert_and_close_alert(self):
        alert_title = self.get_visible_element(self.send_successfully_alert_title).text
        alert_contract_code = self.get_visible_element(self.send_successfully_alert_contract_code).text
        alert_order_id = self.get_visible_element(self.send_successfully_alert_order_id).text
        self.click_action(self.button_close)
        return alert_title, alert_contract_code, alert_order_id

    def stp_clear_stop_price_and_buy(self):
        self.change_order_type_stp()
        self.click_action(self.offer_price)
        self.clear_action(self.input_stop_price)
        self.click_action(self.button_buy)

    def stp_clear_stop_price_and_sell(self):
        self.change_order_type_stp()
        self.click_action(self.offer_price)
        self.clear_action(self.input_stop_price)
        self.click_action(self.button_sell)

    def stp_input_stop_price_and_buy(self):
        self.change_order_type_stp()
        stp_price = self.get_visible_element(self.input_price).text
        self.click_action(self.offer_price)
        self.clear_action(self.input_stop_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        # 买单stop price的值不能小于最后成交价，否则下单失败，目前此校验由服务器完成，暂未在手机端校验，但若需保证金额下单成功故需遵守此规则。
        stop_price = float(last_price_and_lots_txt.split('@')[1]) + 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)
        return stp_price

    def stp_input_stop_price_and_sell(self):
        self.change_order_type_stp()
        stp_price = self.get_visible_element(self.input_price).text
        self.click_action(self.offer_price)
        self.clear_action(self.input_stop_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        # 卖单stop price的值不能大于最后成交价，否则下单失败，目前此校验由服务器完成，暂未在手机端校验，但若需保证金额下单成功故需遵守此规则。
        stop_price = float(last_price_and_lots_txt.split('@')[1]) - 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_sell)
        self.click_action(self.button_confirm)
        return stp_price

    def stl_clear_stop_price_and_buy(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_stop_price)
        self.click_action(self.button_buy)

    def stl_clear_stop_price_and_sell(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_stop_price)
        self.click_action(self.button_sell)

    def stl_input_stop_price_and_buy(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) + 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) + 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)

    def stl_input_stop_price_and_sell(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) - 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) - 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_sell)
        self.click_action(self.button_confirm)

    def stl_stop_price_above_price_and_buy(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) + 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) + 3
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_buy)

    def stl_stop_price_less_than_price_and_sell(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) - 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) - 3
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_sell)

    def stl_buy_price_must_above_stop_price(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) + 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) + 3
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_buy)
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) + 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)

    def stl_price_less_than_stop_price_buy_then_sell(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) - 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) - 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_buy)
        self.click_action(self.button_sell)
        self.click_action(self.button_confirm)

    def stl_sell_price_must_less_than_stop_price(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) - 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) - 3
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_sell)
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) - 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_sell)
        self.click_action(self.button_confirm)

    def stl_price_above_stop_price_sell_then_buy(self):
        self.change_order_type_stl()
        self.click_action(self.offer_price)
        self.clear_action(self.input_price)
        last_price_and_lots = self.get_visible_element(self.last_price_and_lots)
        last_price_and_lots_txt = last_price_and_lots.text
        price = float(last_price_and_lots_txt.split('@')[1]) + 2
        self.input_action(self.input_price, str(price))
        self.clear_action(self.input_stop_price)
        stop_price = float(last_price_and_lots_txt.split('@')[1]) + 1
        self.input_action(self.input_stop_price, str(stop_price))
        self.click_action(self.button_sell)
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)

    def ice_clear_iceberg_chunk_size_and_buy(self):
        self.change_order_type_ice()
        self.click_action(self.offer_price)
        self.clear_action(self.input_iceberg_chunk_size)
        self.click_action(self.button_buy)

    def ice_clear_iceberg_chunk_size_and_sell(self):
        self.change_order_type_ice()
        self.click_action(self.offer_price)
        self.clear_action(self.input_iceberg_chunk_size)
        self.click_action(self.button_sell)

    def ice_iceberg_chunk_size_input_above_lots_and_buy(self, lots, iceberg_chunk_size):
        self.change_order_type_ice()
        self.click_action(self.offer_price)
        self.clear_action(self.input_lots)
        self.input_action(self.input_lots, lots)
        self.clear_action(self.input_iceberg_chunk_size)
        self.input_action(self.input_iceberg_chunk_size, iceberg_chunk_size)
        iceberg_chunk_size = self.get_visible_element(self.input_iceberg_chunk_size).text
        self.click_action(self.button_buy)
        self.click_action(self.button_confirm)
        return iceberg_chunk_size

    def market_input_lots_and_sell(self):
        self.change_order_type_market()
        self.click_action(self.offer_price)
        price_text = self.get_visible_element(self.input_price).text
        self.click_action(self.button_sell)
        order_details_title = self.get_visible_element(self.order_details_title).text
        order_details_price = self.get_visible_element(self.order_details_price).text
        self.click_action(self.button_confirm)
        return price_text, order_details_title, order_details_price

    def market_input_lots_and_buy(self):
        self.change_order_type_market()
        self.click_action(self.offer_price)
        price_text = self.get_visible_element(self.input_price).text
        self.click_action(self.button_buy)
        order_details_title = self.get_visible_element(self.order_details_title).text
        order_details_price = self.get_visible_element(self.order_details_price).text
        self.click_action(self.button_confirm)
        return price_text, order_details_title, order_details_price


if __name__ == '__main__':
    driver = android_driver()
    # a = NewOrderPage(driver)
    # a.login_successful()
    # a.slide_contract_group_and_go_to_new_order_page()
