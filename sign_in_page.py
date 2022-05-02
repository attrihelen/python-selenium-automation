
from selenium import webdriver
from selenium.webdriver.common.by import By


# initialize driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


# click orders
driver.find_element(By.ID, 'nav-orders').click()


# verify sign in page is opened
driver.find_element(By.XPATH, '//div[@class="a-box"]//h1')


print('Test passed')
driver.quit()


