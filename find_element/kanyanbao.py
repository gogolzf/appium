from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = "vivo x9"
desired_caps['platformVersion'] = "8.1.0"
desired_caps["udid"] = "5b19c02e"

desired_caps['app'] = r"F:\BaiduNetdiskDownload\kaoyan3.1.0.apk"
desired_caps['appPackage'] = "com.tal.kaoyan"
desired_caps['appActivity'] = "com.tal.kaoyan.ui.activity.SplashActivity"

# 启动服务
drive = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)



