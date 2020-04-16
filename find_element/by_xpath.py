from find_element.capabilit import drive

drive.find_element_by_xpath("//android.widget.EditText[@text = '请输入用户名']").send_keys("gogolzfgogo")
drive.find_element_by_xpath("//*[@class = 'android.widget.EditText' and @index = '3']").send_keys("12580fan")
drive.find_element_by_xpath("//android.widget.Button").click()