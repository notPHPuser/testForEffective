from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_purchase():
    browser = webdriver.Chrome()

    try:
        browser.get("https://www.saucedemo.com/")
        username = browser.find_element(By.ID, 'user-name')
        password = browser.find_element(By.ID, 'password')
        login_button = browser.find_element(By.ID, 'login-button')

        username.send_keys('standard_user')
        password.send_keys('secret_sauce')
        login_button.click()

        item = browser.find_element(By.CSS_SELECTOR, '.inventory_list>div:nth-child(1) .inventory_item_name ')
        item.click()

        add = browser.find_element(By.ID, 'add-to-cart')
        add.click()

        search = browser.find_element(By.CLASS_NAME, 'shopping_cart_link')
        search.click()

        check = browser.find_element(By.ID, 'checkout')
        check.click()

        first_name = browser.find_element(By.ID, 'first-name')
        second_name = browser.find_element(By.ID, 'last-name')
        code = browser.find_element(By.ID, 'postal-code')
        first_name.send_keys('1')
        second_name.send_keys('2')
        code.send_keys('3')

        buy = browser.find_element(By.ID, 'continue')
        buy.click()

        finish = browser.find_element(By.ID, 'finish')
        finish.click()

        complete = browser.find_element(By.CLASS_NAME, 'complete-header')
        text = complete.text
        if text == 'Thank you for your order!':
            return True
        else:
            return False
    finally:
        time.sleep(3)
        browser.quit()


assert test_purchase() == True, "Ошибка, транзакция не прошла"


