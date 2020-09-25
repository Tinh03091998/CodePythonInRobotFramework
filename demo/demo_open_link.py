# import webbrowser

# webbrowser.open_new_tab("testtinh1998.myshopify.com/admin/apps/super-reports-qa")
# open_google = webbrowser.open('testtinh1998.myshopify.com/admin/apps/super-reports-qa')

#pip install selenium
#pip3 install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.get("https://testtinh1998.myshopify.com/admin/apps/super-reports-qa")
inputEmail = driver.find_element_by_id("account_email")
inputEmail.send_keys('development@2-b.io')
buttonNext = driver.find_element_by_xpath("//*[contains(@name,'commit')]")
buttonNext.click();
inputPassword = driver.find_element_by_id("account_password")
inputPassword.send_keys('Testing@2b')
buttonLogin = driver.find_element_by_xpath("//*[contains(@name,'commit')]")
time.sleep(5)
buttonLogin.click();
appFrame = Select(driver.find_element_by_xpath("//iframe[@title='Super-Reports-QA']"))
menuReports = driver.find_element_by_xpath("//li[.='Reports']")
if not menuReports:
    print("Ton tai element")
else:
    print("Khong ton tai element")