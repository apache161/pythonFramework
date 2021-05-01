class searchAutomation:
   lnktxt_Customers_xpath = "//a[@href='#'] //p[contains(text(), 'Customers')]"
   lnktxt_Customermenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),' Customers')]"
   txt_Email_xpath = "//input[@id='SearchEmail']"
   btn_Search_xpath =  "//button[@id='search-customers']"
   table_scan_xpath = "//table[@id='customers-grid']"
   table_rows_xpath=  "//table[@id='customers-grid']//tbody/tr"
   table_cols_xpath = "//table[@id='customers-grid']//tbody/tr/td"

   def __init__(self, driver):
       self.driver = driver

   def getCustomerlink(self):
      self.driver.find_element_by_xpath(self.lnktxt_Customers_xpath).click()

   def getCustomermenulink(self):
      self.driver.find_element_by_xpath(self.lnktxt_Customermenu_xpath).click()

   def getEmail(self, email):
       self.driver.find_element_by_xpath(self.txt_Email_xpath).clear()
       self.driver.find_element_by_xpath(self.txt_Email_xpath).send_keys(email)

   def clickSearchBtn(self):
       self.driver.find_element_by_xpath(self.btn_Search_xpath).click()

   def getSearchEmail(self, email):
       self.driver.find_element_by_xpath(self.table_scan_xpath)
       rowTable = len(self.driver.find_elements_by_xpath(self.table_rows_xpath))
       colTable = len(self.driver.find_elements_by_xpath(self.table_cols_xpath))
       print(rowTable)
       print(colTable)
       for i in range(1, rowTable + 1):
           email_output = self.driver.find_element_by_xpath(self.table_rows_xpath + str([i]) + "//td[2]").text
           print(email, email_output, end="|")
           if (email == email_output):
                print(email_output)
                print(email)
                break
                assert True
           else:
                assert False
