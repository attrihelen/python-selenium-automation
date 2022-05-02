from selenium.webdriver.common.by import By
from behave import given, when, then



RETURNS_ORDERS = (By.ID, 'nav-orders')
SIGN_IN = (By.XPATH, '//div[@class="a-box"]//h1')


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')



@when('Click on Returns&Orders icon')
def click_returns_and_orders_icon(context):
    context.driver.find_element(*RETURNS_ORDERS).click()



@then('Verify Sign-In text is present')
def verify_sign_in_text(context):
    expected_result = 'Sign-In'
    actual_result = context.driver.find_element(*SIGN_IN).text
    assert expected_result == actual_result , f'Expected result: {expected_result} is not the same as actual: {actual_result}'

