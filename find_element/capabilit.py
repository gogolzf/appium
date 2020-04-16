from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = "vivo x9"
# desired_caps['deviceName'] = "meizu note8"
desired_caps['deviceName'] = "vivo x23"
# desired_caps['platformVersion'] = "8.1.0"
desired_caps['platformVersion'] = "9.0.0"
# desired_caps["udid"] = "5b19c02e"
# desired_caps["udid"] = "822QEDTK22RSQ"
desired_caps["udid"] = "9c644168"

desired_caps['app'] = r"F:\BaiduNetdiskDownload\kaoyan3.1.0.apk"
desired_caps['appPackage'] = "com.tal.kaoyan"
desired_caps['appActivity'] = "com.tal.kaoyan.ui.activity.SplashActivity"
desired_caps['noReset'] = "False"
# desired_caps['unicodeKeyboard'] = "True"
# desired_caps['resetKeyboard'] = "True"
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(2)

def check_cancleBtu():
    try:
        try1 = driver.find_element_by_id("android:id/button2")
    except NoSuchElementException:
        print("No cancelBtu")
    else:
        try1.click()

def check_skipBtu():
    try:
        try2 = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
        print("Success")
    except:
        print("No skipBtu")
    else:
        try2.click()

check_cancleBtu()
check_skipBtu()


