import time
from appium import webdriver  # appium 的特色就是将安卓、IOS的底层封装成了 webdriver 类型的语句
from appium.webdriver.common.touch_action import TouchAction

from PycharmProjects.ProjectAuto.common.baseLog import logger


def android_driver():
    desired_caps = {
        "platformName": "android",
        "deviceName": "MXW_AN00",
        "appPackage": "com.atp.demo2",
        "appActivity": "com.atp.newarchitecture.activity.AppActivity",
        "noReset": "True",
        "unicodeKeyboard": "True",
        # "resetKeyboard": "True",
    }
    try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # time.sleep(2)
        # app下载之后只有第一次登录时执行21-26行代码。
        # TouchAction(driver).press(x=530, y=1967).move_to(x=516, y=810).release().perform()
        # el1 = driver.find_element_by_xpath(
        #     "//android.view.View[@content-desc=\"十二、其他\"]/android.widget.TextView[2]")
        # el1.click()
        # el2 = driver.find_element_by_id("com.atp.demo2:id/agree")
        # el2.click()
        logger.info("APP启动成功...")
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
