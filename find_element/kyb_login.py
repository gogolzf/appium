from find_element.capabilit import drive, NoSuchElementException

def login():
    drive.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    drive.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("gogolzfgogo")
    drive.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("12580fan")
    drive.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

try:
    drive.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
except NoSuchElementException:
    login()
else:
    drive.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
    drive.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_username").click()
    login()