from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
email_id = "account_email"
environment_url = "https://testtinh1998.myshopify.com/admin/apps/super-reports-qa"
email_value = 'development@2-b.io'
next_xpath = "//*[contains(@name,'commit')]"
password_id = "account_password"
password_value = 'Testing@2b'
login_xpath = "//*[contains(@name,'commit')]"

def openWebsite(url):
    global driver;
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(5)
    driver.get(url)

def inputElementbyXpath(xpath, value):
    element_xpath = driver.find_element_by_xpath(xpath)
    element_xpath.send_keys(value)

def inputElementbyId(id, value):
    element_id = driver.find_element_by_id(id)
    element_id.send_keys(value)

def clickElementbyXpath(xpath):
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click();

def closeBrowser():
    driver.quit()

openWebsite(environment_url)
inputElementbyId(email_id, email_value)
clickElementbyXpath(next_xpath)
inputElementbyId(password_id, password_value)
clickElementbyXpath(login_xpath)
closeBrowser()

