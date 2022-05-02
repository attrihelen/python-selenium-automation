from selenium import webdriver

# init driver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#by ID
driver.find_element(By.ID, "twotabsearchtextbox")

#by XPATH
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo")

#by using only tag
driver.find_element(By.XPATH, "//a")   #  ==  driver.find_element(By.TAG_NAME, "a")

#by using only attribute
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo")

#by using multiple attributes
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo' and @aria-label='Amazon']")

#by using partial attribute
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")

#by using multiple nodes, 1 by 1, /
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']/div/a[contains(@href, 'bestsellers')]")

#by using multiple nodes, skipping nodes with //
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[contains(@href, 'bestsellers')]")

