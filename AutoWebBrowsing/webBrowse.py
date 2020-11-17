from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
message_field = driver.find_element_by_xpath('//*[@id="user-message"]')
message_field.send_keys('Hello World')
show_message_button = driver.find_element_by_xpath('//*[@id="get-input"]/button')
show_message_button.click()


addition_field1 = driver.find_element_by_xpath('//*[@id="sum1"]')
addition_field1.send_keys('10')
addition_field2 = driver.find_element_by_xpath('//*[@id="sum2"]')
addition_field2.send_keys('15')
get_total_button = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
get_total_button.click()