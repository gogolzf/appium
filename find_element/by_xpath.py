from find_element.capabilit import driver

driver.find_element_by_xpath("//android.widget.EditText[@text = '请输入用户名']").send_keys("gogolzfgogo")
driver.find_element_by_xpath("//*[@class = 'android.widget.EditText' and @index = '3']").send_keys("12580fan")
driver.find_element_by_xpath("//android.widget.Button").click()