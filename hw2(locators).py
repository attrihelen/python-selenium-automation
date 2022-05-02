from selenium import webdriver

# init driver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#by ID  ---- EMAIL FIELD
driver.find_element(By.ID, "ap_email")

#by XPATH  ----- HELP BUTTON
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")


#by using only attribute ---- LOGO
driver.find_element(By.XPATH, "//*[@role='img']")

#by using multiple attributes  ---- CONTINUE BUTTON
driver.find_element(By.XPATH, "//*[@id='continue' and @class='a-button-input']")

#by using partial attribute  ---- CREATE ACCOUNT ---- PRIVACY NOTICE ---- CONDITIONS OF USE
driver.find_element(By.XPATH, "//a[contains(@href, 'register')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'signin_notification_privacy_notice')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")


#by using multiple nodes, skipping nodes with //   ---- FORGOT PASSWORD ---- OTHER ISSUES
driver.find_element(By.XPATH, "//div[@class='a-box']//a[contains(@href, 'forgotpassword')]")
driver.find_element(By.XPATH, "//div[@class='a-box']//a[contains(@href, 'account-issues')]")
