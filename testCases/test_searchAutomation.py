import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from pageObjects.fullAutomation import fullAutomation
from utilities.readProperties import readConfig
from utilities.customlogger import logGen
from pageObjects.searchAutomation import searchAutomation
from utilities import XLUtilities
import string


class Test_searchAutomation_001_login:
    URL = readConfig.readURL()
    username = readConfig.readUsername()
    password = readConfig.readPassword()
    logger = logGen.logGeneration()

    #@pytest.mark.regression
    def test_addNewCustomer(self, setup):
        self.logger.info("**************test_login**************")
        self.logger.info("**************Verify test_login Page**************")
        self.driver = setup
        self.driver.get(self.URL)
        self.lp = loginPage(self.driver)
        self.lp.Usrname(self.username)
        self.lp.Password(self.password)
        self.lp.Login()
        loginTitle = self.driver.title
        # if loginTitle =="Dashboard / nopCommerce administration":
        if "Dashboard" in loginTitle:
            assert True
            # self.driver.save_screenshot(".\\screenshots\\titleLogin1.png")
            # self.driver.close()
        else:
            # self.driver.save_screenshot(".\\screenshots\\titleLogin1.png")
            # self.driver.close()
            assert False

        self.logger.info("**************Test_fullAutomation_001_login**************")
        self.logger.info("**************Verify test_addNewCustomer Page**************")
        self.fa = fullAutomation(self.driver)
        self.fa.getCustomerlink()
        self.fa.getCustomermenulink()
        self.fa.getAddNew()
        self.fa.EmailID = self.fa.getEmail("test112_12345q2@g.com")
        self.fa.getPassword("test112_1234")
        self.fa.getFirstName("fname1")
        self.fa.getLastName("lname1")
        self.fa.getGender("Male")
        self.fa.getDOB("05/20/21")
        self.fa.getNewsletter()
        time.sleep(2)
        self.fa.getNewsletterStore2()
        self.fa.getCustomerRoles()
        time.sleep(1)
        self.fa.getUnselectRoleRegistered()
        # self.fa.getRoleAdministrator()
        # self.fa.getUnselectRoleRegistered()
        self.fa.saveAddBtn()
        self.logger.info("**************Test_searchAutomation_001_login**************")
        self.logger.info("**************Verify searchAutomationuser details page**************")

        self.sa = searchAutomation(self.driver)
        self.sa.getCustomerlink
        self.sa.getCustomermenulink()
        self.sa.getEmail("test112_123@g.com")
        self.sa.clickSearchBtn()
        self.sa.getSearchEmail("test112_123@g.com")

        self.logger.info("**************Verify searchAutomationuser completed page**************")
