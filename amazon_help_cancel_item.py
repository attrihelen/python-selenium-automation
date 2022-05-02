
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()
driver.maximize_window()


driver.get('https://www.amazon.com/gp/help/customer/display.html')

search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order', Keys.ENTER)


expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//div[@class='cs-help-content']//h1").text
assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"

print('Test case passed')
driver.quit()
