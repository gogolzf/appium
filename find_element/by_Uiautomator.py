from find_element.capabilit import driver

# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys("gogolzfgogo")
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().className("android.widget.EditText")').send_keys("gogolzfgogo")
driver.find_element_by_android_uiautomator\
    ('new UiSelector().text("请输入用户名")').send_keys("gogolzfgogo")
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys("12580fan")
driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()

