from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.dominos.com")
delivery = driver.find_element_by_xpath(
    "//*[@id='__next']/main/section[1]/div/div[2]/a[1]")
delivery.click()
time.sleep(7)
stad = driver.find_element_by_id("Street")
stad.send_keys("ADDRESS HERE")
time.sleep(0.5)
zip = driver.find_element_by_id("Postal_Code_Sep")
zip.clear()
zip.send_keys("ZIPCODE HERE")
time.sleep(3)
button2 = driver.find_element_by_xpath(
    "//*[@id='locationSearchForm']/div/div[4]/button")
button2.click()
time.sleep(4)
build = driver.find_element_by_xpath("//*[@id='entree-BuildYourOwn']/a")
build.click()
time.sleep(2)
add = driver.find_element_by_xpath(
    "//*[@id='pageModal']/div/section/div/div/div/div/aside/section/div/button")
add.click()
time.sleep(2)
nocheese = driver.find_element_by_xpath("//*[@id='stepUpsell']/div/button[1]")
nocheese.click()
time.sleep(2)
driver.get("https://www.dominos.com/en/pages/order/#!/checkout/")
time.sleep(5)
x = driver.find_element_by_xpath(
    "//*[@id='genericOverlay']/section/header/button")
x.click()
time.sleep(5)
driver.get("https://www.dominos.com/en/pages/order/payment")
time.sleep(5)
name = driver.find_element_by_id("First_Name")
name.send_keys("FIRSTNAME HERE")
lname = driver.find_element_by_id("Last_Name")
lname.send_keys("LASTNAME HERE")
email = driver.find_element_by_id("Email")
email.send_keys("EMAIL HERE")
phone = driver.find_element_by_id("Callback_Phone")
time.sleep(0.3)
phone.send_keys("PHONE NUMBER HERE")
time.sleep(2)
paycash = driver.find_element_by_xpath("//*[@id='Cash']")
paycash.click()
time.sleep(1)
ORDER = driver.find_element_by_xpath(
    '//*[@id="payment-form"]/div[7]/div/div/div[5]/button')
ORDER.click()
time.sleep(5)
