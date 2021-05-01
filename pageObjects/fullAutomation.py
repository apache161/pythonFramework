class fullAutomation:

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
   btn_save_xpath = "//button[@name='save']"

   def __init__(self, driver):
      self.driver = driver

   def getCustomerlink(self):
      self.driver.find_element_by_xpath(self.lnktxt_Customers_xpath).click()

   def getCustomermenulink(self):
      self.driver.find_element_by_xpath(self.lnktxt_Customermenu_xpath).click()

   def getAddNew(self):
      self.driver.find_element_by_xpath(self.lnktxt_Addnew_xpath).click()

   def getEmail(self, Email):
      self.driver.find_element_by_xpath(self.txtbox_Email_xpath).send_keys(Email)

   def getPassword(self, Password):
      self.driver.find_element_by_xpath(self.txtbox_Password_xpath).send_keys(Password)

   def getFirstName(self,fName):
      self.driver.find_element_by_xpath(self.txtbox_FirstName_xpath).send_keys(fName)

   def getLastName(self, lName):
      self.driver.find_element_by_xpath(self.txtbox_LastName_xpath).send_keys(lName)

   def getGender(self, Gender):
      self.driver.find_element_by_xpath(self.Radio_Gender_xpath).click()

   def getDOB(self, DOB):
      self.driver.find_element_by_xpath(self.txtbox_DOB_xpath).send_keys(DOB)

   def getCustomerRoles(self):
      self.driver.find_element_by_xpath(self.txtbox_CustomerRoles_xpath).click()

   def getRoleRegistered(self):
      self.driver.find_element_by_xpath(self.drpdown_Registered_xpath).click()

   def getRoleAdministrator(self):
      self.driver.find_element_by_xpath(self.drpdown_Administrators_xpath).click()

   def getUnselectRoleRegistered(self):
      self.driver.find_element_by_xpath(self.drpdown_Registered_delete_xpath).click()

   def getNewsletter(self):
      self.driver.find_element_by_xpath(self.txtbox_NewsLetter_xpath).click()

   def getNewsletterStoreName(self):
      self.driver.find_element_by_xpath(self.drpdown_YourStoreName_xpath).click()

   def getNewsletterStore2(self):
      self.driver.find_element_by_xpath(self.drpdown_TextStore2_xpath).click()

   def saveAddBtn(self):
      self.driver.find_element_by_xpath(self.btn_save_xpath).click()