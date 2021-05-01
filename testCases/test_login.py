import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from utilities.readProperties import readConfig
from utilities.customlogger import logGen
from utilities import XLUtilities



class Test_001_login:
    URL = readConfig.readURL()
    username = readConfig.readUsername()
    password = readConfig.readPassword()

    logger = logGen.logGeneration()

    @pytest.mark.sanity
    def test_titleCheck(self,setup):
        self.logger.info("**************test_titleCheck_testCase**************")
        self.logger.info("**************Verify Title Page**************")
        self.driver = setup
        self.driver.get(self.URL)
        actualTitle = self.driver.title
        if actualTitle == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.logger.error("**************titleCheck Failed**************")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_loginCheck(self, setup):
        self.logger.info("**************test_loginCheck_testCase**************")
        self.logger.info("**************Verify Login Page**************")
        self.driver =setup
        self.driver.get(self.URL)
        self.lp = loginPage(self.driver)
        self.lp.Usrname(self.username)
        self.lp.Password(self.password)
        self.lp.Login()
        loginTitle = self.driver.title
        #if loginTitle =="Dashboard / nopCommerce administration":
        if "Dashboard" in loginTitle:
            assert True
            self.driver.save_screenshot(".\\screenshots\\titleLogin1.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\titleLogin1.png")
            self.driver.close()
            assert False

