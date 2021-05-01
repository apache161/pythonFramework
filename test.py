import os
import sys
import time

'''
basedir = os.path.dirname(os.path.dirname(__file__))+ "\\logs\\auto.log"
print(basedir)

inFileName = ".\\testData/loginData.xlsx"
inSheetName = "Sheet1"

print(inFileName)
'''

from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.Chrome(executable_path="C:\\Users\\syede\\Downloads\\Learning\\Drivers\\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/")


driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
driver.find_element_by_id("Password").clear()
driver.find_element_by_id("Password").send_keys("admin")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
#link_Customers_xpath = "//a[@class ='nav-link active']"
#link_Customersmenu_xpath = "//a[@class ='nav-link active'] // p[text()= ' Customers']"
#link_Addnew_xpath = "//a[@class ='btn btn-primary'] // i"

lnktxt_Customers_xpath = "//a[@href='#'] //p[contains(text(), 'Customers')]"
lnktxt_Customermenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),' Customers')]"
lnktxt_Addnew_xpath = "//a[@class ='btn btn-primary'] // i"
txtbox_Email_xpath = "//input[@id='Email']"
txtbox_Password_xpath = "//input[@id='Password']"
txtbox_FirstName_xpath = "//input[@id='FirstName']"
txtbox_LastName_xpath = "//input[@id='LastName']"
Radio_GenderM_xpath = "//input[@id='Gender_Male']"
Radio_GenderF_xpath = "//input[@id='Gender_Female']"
txtbox_DOB_xpath = "//input[@id='DateOfBirth']"
Radio_Gender_xpath = "//input[@id='Gender_Male']"
txtbox_CustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
txtbox_NewsLetter_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']//input[@class='k-input k-readonly']"
drpdown_Registered_xpath = "//li[contains(text(),'Registered')]"
drpdown_Administrators_xpath = "//li[contains(text(),'Administrators')]"
drpdown_Registered_delete_xpath = "//li[@class='k-button']//span[contains(text(),'Registered')]"
drpdown_Administrators_delete_xpath = "//li[@class='k-button']//span[contains(text(),'Administrators')]"
drpdown_YourStoreName_xpath = "//li[contains(text(),'store name')]"
drpdown_TextStore2_xpath = "//li[contains(text(),'store 2')]"
btn_save_xpath ="//button[@name='save']"

'''
driver.find_element(By.XPATH, "//a[@href='#'] //p[contains(text(), 'Customers')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List'] //p[contains(text(),' Customers')]").click()
driver.find_element(By.XPATH, "//a[@class ='btn btn-primary'] // i").click()
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("testSelenium112@g.com")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("test1")
driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Fname1")
driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Lname1")
driver.find_element(By.XPATH, "//input[@id='Gender_Male']").click()
driver.find_element(By.XPATH, "//input[@id='DateOfBirth']").send_keys("05/28/2021")
#driver.find_element(By.XPATH, "//div[@class='k-multiselect-wrap k-floatwrap']").click() # select multiselect
#driver.find_element(By.XPATH, "//li[@class='k-button']//span[contains(text(),'Registered')]").click() #
#driver.find_element(By.XPATH, "//li[contains(text(),'Administrators')]").click()
#driver.find_element(By.XPATH, "//li[@class='k-button']//span[contains(text(),'Registered')]/following-sibling::span").click()
#driver.find_element(By.XPATH, "//li[contains(text(),'Guests')]").click()
driver.find_element(By.XPATH,"//div[@class='k-multiselect-wrap k-floatwrap']//input[@class='k-input k-readonly']").click()
driver.find_element(By.XPATH, "//li[contains(text(),'store name')]").click()
driver.find_element(By.XPATH, "//li[contains(text(),'store 2')]").click()
driver.find_element(By.XPATH, "//button[@name='save']").click()
time.sleep(5)
'''

driver.find_element(By.XPATH, "//a[@href='#'] //p[contains(text(), 'Customers')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List'] //p[contains(text(),' Customers')]").click()
driver.find_element(By.XPATH,"//input[@id='SearchEmail']").clear()
emailID = driver.find_element(By.XPATH,"//input[@id='SearchEmail']").send_keys("testSelenium112@g.com")
email = "testSelenium112@g.com"
driver.find_element(By.XPATH, "//button[@id='search-customers']").click()
time.sleep(2)

entireTable = driver.find_element(By.XPATH, "//table[@id='customers-grid']")
rowsTable = len(driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr"))
colsTable = len(driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr/td"))
print(rowsTable)
print(colsTable)
for i in range(1,rowsTable + 1):
    email_output = driver.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr"+str([i])+"//td[2]").text
    print(email, email_output, end ="-")
    print(len(email), len(email_output), end="-")
    if (email == email_output):
        print(email_output)
        print(emailID)
        break
        assert True
    else:
        assert False




