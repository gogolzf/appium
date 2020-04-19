from find_element.capabilit import driver, NoSuchElementException

def login():
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("gogolzfgogo")
    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("12580fan")
    driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

try:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
    driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()
    login()