import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy

from common.AlertError import AlertError
from common.baseDriver import android_driver
from pageObject.normal_order_page import NormalOrderPage


class CaseNormalOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = android_driver()
        self.normal_order_page = NormalOrderPage(self.driver)
        self.normal_order_page.login_successful()

    def tearDown(self) -> None:
        self.driver.quit()

    # 买卖盘及涨跌幅有数据时根据交易方向相反数据填充
    def test_01_press_bid_and_side_should_sell(self):
        self.normal_order_page.press_bid()
        isSellChecked = self.normal_order_page.is_side_sell_checked()
        isBuyChecked = self.normal_order_page.is_side_buy_checked()
        self.assertEqual("true", isSellChecked)
        self.assertEqual("false", isBuyChecked)

    def test_02_press_bid_and_lots_should_offer_value(self):
        result = self.normal_order_page.press_bid_and_check_lots()
        self.assertEqual(result[0], result[1])

    def test_03_press_bid_and_price_should_offer_value(self):
        result = self.normal_order_page.press_bid_and_check_price()
        self.assertEqual(result[0], result[1])

    def test_04_press_offer_and_side_should_buy(self):
        self.normal_order_page.press_offer()
        isBuyChecked = self.normal_order_page.is_side_buy_checked()
        isSellChecked = self.normal_order_page.is_side_sell_checked()
        self.assertEqual("true", isBuyChecked)
        self.assertEqual("false", isSellChecked)

    def test_05_press_offer_and_lots_should_bid_value(self):
        result = self.normal_order_page.press_offer_and_check_lots()
        self.assertEqual(result[0], result[1])

    def test_06_press_offer_and_price_should_bid_value(self):
        result = self.normal_order_page.press_offer_and_check_price()
        self.assertEqual(result[0], result[1])

    def test_07_press_chg_and_side_should_buy(self):
        self.normal_order_page.slide_and_press_chg()
        isBuyChecked = self.normal_order_page.is_side_buy_checked()
        isSellChecked = self.normal_order_page.is_side_sell_checked()
        self.assertEqual("true", isBuyChecked)
        self.assertEqual("false", isSellChecked)

    def test_08_press_chg_and_lots_should_offer_value(self):
        result = self.normal_order_page.press_chg_and_check_lots()
        self.assertEqual(result[0], result[1])

    def test_09_press_chg_and_price_should_offer_value(self):
        result = self.normal_order_page.press_chg_and_check_price()
        self.assertEqual(result[0], result[1])

    # 买卖盘及涨跌幅没有数据时手数和价格按照"1"，"0"填充。
    def test_10_press_no_data_bid_and_lots_should_fix_num(self):
        # 合约TCU1906-SH在第二个的时候执行67代码
        self.normal_order_page.drag_first_contract_to_second_location()
        result = self.normal_order_page.press_bid_and_check_lots()
        self.assertEqual(result, "1")

    def test_11_press_no_data_bid_and_price_should_fix_num(self):
        result = self.normal_order_page.press_bid_and_check_price()
        self.assertEqual(result, "0")

    def test_12_press_no_data_offer_and_lots_should_fix_num(self):
        result = self.normal_order_page.press_offer_and_check_lots()
        self.assertEqual(result, "1")

    def test_13_press_no_data_offer_and_price_should_fix_num(self):
        result = self.normal_order_page.press_offer_and_check_price()
        self.assertEqual(result, "0")

    def test_14_press_no_data_chg_and_lots_should_fix_num(self):
        result = self.normal_order_page.press_chg_and_check_lots()
        self.assertEqual(result, "1")

    def test_15_press_no_data_chg_and_price_should_fix_num(self):
        result = self.normal_order_page.press_chg_and_check_price()
        self.assertEqual(result, "0")

    def test_16_no_change_and_order_should_success(self):
        self.normal_order_page.drag_first_contract_to_second_location()
        self.normal_order_page.press_bid()
        time.sleep(1)
        self.normal_order_page.press_confirm_button()
        self.normal_order_page.press_confirm_button()
        time.sleep(1)
        result = self.normal_order_page.alert_order_details_title()
        txt = AlertError.alert_message_order_succeed
        self.assertEqual(result, txt)

    def test_17_change_trade_account_should_success(self):
        result = self.normal_order_page.change_trade_account()
        self.assertEqual(result[0], result[1])

    def test_18_change_side_should_success(self):
        self.normal_order_page.change_buy_side()
        isSellChecked = self.normal_order_page.is_side_sell_checked()
        isBuyChecked = self.normal_order_page.is_side_buy_checked()
        self.assertEqual("true", isSellChecked)
        self.assertEqual("false", isBuyChecked)

    def test_19_clear_lots_and_order_should_fail(self):
        self.normal_order_page.clear_lots_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_lots)
        self.assertEqual(True, result)

    def test_20_input_illegal_lots_and_order_should_fail(self):
        self.normal_order_page.input_illegal_lots_and_order("1.")
        result = self.normal_order_page.alert_illegal_lots_title()
        self.assertEqual(result, AlertError.illegal_lots)

    def test_21_clear_price_and_order_should_fail(self):
        self.normal_order_page.clear_price_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_price)
        self.assertEqual(True, result)

    def test_22_input_illegal_price1_and_order_should_fail(self):
        self.normal_order_page.input_illegal_price_and_order(".")
        result = self.normal_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_23_input_illegal_price2_and_order_should_fail(self):
        self.normal_order_page.input_illegal_price_and_order("+")
        result = self.normal_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_24_input_illegal_price3_and_order_should_fail(self):
        self.normal_order_page.input_illegal_price_and_order("-")
        result = self.normal_order_page.is_toast_exist(AlertError.alert_illegal_price)
        self.assertEqual(True, result)

    def test_25_input_lots_and_price_and_order_should_success(self):
        self.normal_order_page.input_lots_and_price_and_order(1, 80)
        result = self.normal_order_page.alert_order_details_title()
        txt = AlertError.alert_message_order_succeed
        self.assertEqual(result, txt)

    def test_26_changed_Market_type_and_price_should_Market(self):
        self.normal_order_page.change_type_market()
        result = self.normal_order_page.input_price_enabled_and_value()
        self.assertEqual(result[0], "false")
        self.assertEqual(result[1], "Market")

    def test_27_changed_Market_type_and_order_should_success(self):
        self.normal_order_page.Market_type_and_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_28_changed_Market_Limit_type_and_price_should_Market(self):
        self.normal_order_page.change_type_market_Limit()
        result = self.normal_order_page.input_price_enabled_and_value()
        self.assertEqual(result[0], "false")
        self.assertEqual(result[1], "Market")

    def test_29_changed_Market_Limit_type_and_order_should_success(self):
        self.normal_order_page.Market_Limit_type_and_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_30_buy_side_and_Market_type_changed_LIM_type_and_price_should_offer_value(self):
        result = self.normal_order_page.Market_type_changed_LIM_type()
        self.assertEqual(result[0], result[1])

    def test_31_changed_stp_type_and_price_should_Market(self):
        self.normal_order_page.drag_third_contract_to_second_location()
        self.normal_order_page.drag_first_contract_to_second_location()
        self.normal_order_page.change_type_stp()
        result = self.normal_order_page.input_price_enabled_and_value()
        self.assertEqual(result[0], "false")
        self.assertEqual(result[1], "Market")

    def test_32_changed_stp_type_and_buy_side_and_StPx_should_offer_value(self):
        result = self.normal_order_page.change_type_stp()
        self.assertEqual(result[0], result[1])

    def test_33_stp_type_clear_StPx_and_order_should_fail(self):
        self.normal_order_page.stp_clear_StPx_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_StPx)
        self.assertEqual(True, result)

    def test_34_changed_stp_type_and_order_should_success(self):
        self.normal_order_page.stp_type_and_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_35_stp_type_and_buy_side_and_input_StPx_above_last_price_should_success(self):
        self.normal_order_page.stp_type_input_StPx_above_last_price_and_buy_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_36_stp_type_and_buy_side_and_input_StPx_below_last_price_should_fail(self):
        self.normal_order_page.stp_type_input_StPx_below_last_price_and_buy_order()
        result = self.normal_order_page.alert_message()
        self.assertEqual(AlertError.alert_message_buy_order_rejected, result)

    def test_37_stp_type_and_sell_side_and_input_StPx_above_last_price_should_fail(self):
        self.normal_order_page.stp_type_input_StPx_above_last_price_and_sell_order()
        result = self.normal_order_page.alert_message()
        self.assertEqual(AlertError.alert_message_sell_order_rejected, result)

    def test_38_stp_type_and_sell_side_and_input_StPx_below_last_price_should_success(self):
        self.normal_order_page.stp_type_input_StPx_below_last_price_and_sell_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_39_stl_type_and_buy_side_and_price_should_offer_value(self):
        result = self.normal_order_page.change_type_stl()
        self.assertEqual(result[0], result[2])

    def test_40_stl_type_and_buy_side_and_StPx_should_offer_value(self):
        result = self.normal_order_page.change_type_stl()
        self.assertEqual(result[0], result[1])

    def test_41_stl_type_and_clear_StPx_and_order_should_fail(self):
        self.normal_order_page.stl_clear_StPx_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_StPx)
        self.assertEqual(True, result)

    def test_42_stl_type_and_buy_side_and_input_price_equal_StPx_above_last_price_should_success(self):
        self.normal_order_page.stl_type_input_StPx_above_last_price_and_buy_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_43_stl_type_and_buy_side_and_input_price_equal_StPx_below_last_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_below_last_price_and_buy_order()
        result = self.normal_order_page.alert_message()
        self.assertEqual(AlertError.alert_message_buy_order_rejected, result)

    def test_44_stl_type_and_sell_side_and_input_price_equal_StPx_above_last_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_above_last_price_and_sell_order()
        result = self.normal_order_page.alert_message()
        self.assertEqual(AlertError.alert_message_sell_order_rejected, result)

    def test_45_stl_type_and_sell_side_and_input_price_equal_StPx_below_last_price_should_success(self):
        self.normal_order_page.stl_type_input_StPx_below_last_price_and_sell_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_46_stl_type_and_buy_side_and_above_last_price_and_StPx_below_price_should_success(self):
        self.normal_order_page.stl_type_input_StPx_below_price_and_buy_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_47_stl_type_and_buy_side_and_above_last_price_and_StPx_above_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_above_price_and_buy_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_buy_order_illegal_StPx)
        self.assertEqual(result, True)

    def test_46_stl_type_and_sell_side_and_above_last_price_and_StPx_below_price_should_fail(self):
        self.normal_order_page.stl_type_input_StPx_below_price_and_sell_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_sell_order_illegal_StPx)
        self.assertEqual(result, True)

    def test_47_stl_type_and_sell_side_and_above_last_price_and_StPx_above_price_should_success(self):
        self.normal_order_page.stl_type_input_StPx_above_price_and_sell_order()
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_40_ice_type_and_chunk_size_should_fix_value(self):
        result = self.normal_order_page.change_type_ice()
        self.assertEqual("1", result)

    def test_40_ice_type_and_input_chunk_size_illegal_value_should_fix_value(self):
        result = self.normal_order_page.ice_type_and_input_chunk_size("0")
        self.assertEqual("1", result)

    def test_40_ice_type_and_input_chunk_size_less_than_lots_should_legal(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("10", "5")
        self.assertEqual("10", result[0])
        self.assertEqual("5", result[1])

    def test_40_ice_type_and_input_chunk_size_equal_lots_should_legal(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("5", "5")
        self.assertEqual("5", result[0])
        self.assertEqual("5", result[1])

    def test_40_ice_type_and_input_chunk_size_above_lots_should_lots_value(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("5", "10")
        self.assertEqual("5", result[0])
        self.assertEqual("5", result[1])

    def test_40_ice_type_and_input_chunk_size_above_50_should_50(self):
        result = self.normal_order_page.ice_type_and_input_lots_and_chunk_size("51", "51")
        self.assertEqual("51", result[0])
        self.assertEqual("50", result[1])

    def test_40_ice_type_and_clear_chunk_size_and_order_should_fail(self):
        self.normal_order_page.ice_type_clear_chunk_size_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_chunk_size)
        self.assertEqual(True, result)










    def test_41_clear_fak_min_quantity_should_fail(self):
        self.normal_order_page.clear_fak_min_quantity_and_order()
        result = self.normal_order_page.is_toast_exist(AlertError.alert_message_min_quantity)
        self.assertEqual(True, result)

    def test_42_fak_min_quantity_input_below_lots_and_order_should_success(self):
        self.normal_order_page.fak_min_quantity_input_below_lots_and_order(4, 3)
        result = self.normal_order_page.alert_order_details_title()
        self.assertEqual(result, AlertError.alert_message_order_succeed)

    def test_43_fak_min_quantity_input_above_lots_and_order_should_(self):
        fak_min_quantity = self.normal_order_page.fak_min_quantity_input_above_lots_and_order(3, 4)
        time.sleep(2)
        self.assertEqual(fak_min_quantity, '3')

    # def test_32_ice_iceberg_chunk_size_input_above_lots_and_buy_should_succeed(self):
    #     iceberg_chunk_size = self.normal_order_page.ice_iceberg_chunk_size_input_above_lots_and_buy(3, 4)
    #     assert iceberg_chunk_size == '3'
    #     result = self.normal_order_page.is_toast_exist('发送成功')
    #     assert result is True
    #     self.assert_send_successfully_alert_element()
    #
    # def test_33_Market_input_lots_and_sell_should_succeed(self):
    #     price_text, order_details_title, order_details_price = self.normal_order_page.market_input_lots_and_sell()
    #     assert price_text == 'Market'
    #     assert order_details_title == '订单详情'
    #     assert order_details_price == 'Market'
    #     result = self.normal_order_page.is_toast_exist('发送成功')
    #     assert result is True
    #     self.assert_send_successfully_alert_element()
    #
    # def test_34_Market_input_lots_and_buy_should_succeed(self):
    #     price_text, order_details_title, order_details_price = self.normal_order_page.market_input_lots_and_buy()
    #     assert price_text == 'Market'
    #     assert order_details_title == '订单详情'
    #     assert order_details_price == 'Market'
    #     result = self.normal_order_page.is_toast_exist('发送成功')
    #     assert result is True
    #     self.assert_send_successfully_alert_element()


if __name__ == '__main__':
    unittest.main()
