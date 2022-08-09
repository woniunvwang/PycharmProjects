from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from common.baseLog import logger


def android_driver():
    desired_caps = {
        "platformName": "Android",
        "appium:platformVersion": "10",
        "appium:deviceName": "MBJVB20707004299",
        "appium:appPackage": "com.atp.demo2",
        "appium:appActivity": "com.atp.activity.AppActivity",
        # "appium:resetKeyboard": true
    }
    try:
        caps = AppiumOptions().load_capabilities(desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=caps)
        time.sleep(2)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(688, 1872)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(706, 900)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        el1 = driver.find_element(by=AppiumBy.XPATH,
                                  value="//android.view.View[@content-desc=\"十二、其他\"]/android.widget.TextView[3]")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ID, value="com.atp.demo2:id/agree")
        el2.click()

        # app下载之后只有第一次登录时执行21-26行代码。
        # TouchAction(driver).press(x=530, y=1967).move_to(x=516, y=810).release().perform()
        # # el1 = driver.findElementByXPath("//android.view.View[@content-desc=\"十二、其他\"]/android.widget.TextView[2]")
        # el1 = driver.find_element("//android.view.View[@content-desc=\"十二、其他\"]/android.widget.TextView[2]")
        # # el1 = driver.find_element_(
        # #     )
        # el1.click()
        # el2 = driver.find_element("com.atp.demo2:id/agree")
        # # el2 = driver.find_element_by_id("com.atp.demo2:id/agree")
        # el2.click()
        # logger.info("APP启动成功...")
        # driver.implicitly_wait(5)
        return driver
    except Exception as e:
        logger.error("APP启动失败，原因是：{}".format(e))


if __name__ == '__main__':
    android_driver()

# try:
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#     logger.info("APP启动成功...")
#     driver.implicitly_wait(5)
#     return driver
# except Exception as e:
#     logger.error("APP启动失败，原因是：{}".format(e))

