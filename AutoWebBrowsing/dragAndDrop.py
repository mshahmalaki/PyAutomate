from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
for i in range(1, 8):
    source = driver.find_element_by_xpath('//*[@id="box' + str(i) + '"]')
    destination = driver.find_element_by_xpath('//*[@id="box10' + str(i) + '"]')
    action = ActionChains(driver)
    action.drag_and_drop(source,destination).perform()
