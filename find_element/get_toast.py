# coding = utf-8
from  find_element.capabilit import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("555555")
driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("12580fan")
driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

error_message = "用户名或密码错误，你还可以尝试4次"
limit_message = "验证失败次数过多，请15分钟后再试"

# message = '//*[@text = \'{0}\']'.format(error_message)
message = '//*[@text = "{0}"]'.format(limit_message)

toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))

print(toast_element.text)