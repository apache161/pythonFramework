import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from utilities.readProperties import readConfig
from utilities.customlogger import logGen
from utilities import XLUtilities


class Test_002_DDT_login:
    URL = readConfig.readURL()
    path = "..//testData/loginData.xlsx"
    # username = readConfig.readUsername()
    # password = readConfig.readPassword()
    logger = logGen.logGeneration()

    #@pytest.mark.regression
    def test_loginCheck_ddt(self, setup):
        self.logger.info("**************test_002DDT_testCase**************")
        self.logger.info("**************Verify Login Page**************")
        self.driver = setup
        self.driver.get(self.URL)

        self.lp = loginPage(self.driver)

        self.rows = XLUtilities.getRowCount(self.path, "Sheet1")
        print(self.rows)
        self.cols = XLUtilities.getColCount(self.path, "Sheet1")
        print(self.cols)

        lst_sts = []

        for i in range(2, self.rows + 1):
            self.User = XLUtilities.readXL(self.path, 'Sheet1', i, 1)
            self.Pass = XLUtilities.readXL(self.path, 'Sheet1', i, 2)
            self.exp = XLUtilities.readXL(self.path, 'Sheet1', i, 3)

            self.lp.Usrname(self.User)
            self.lp.Password(self.Pass)
            self.lp.Login();
            time.sleep(5)

            act_Title = self.driver.title
            exp_Title = "Dashboard / nopCommerce administration"
            if act_Title == "Dashboard / nopCommerce administration":
                output = 'Pass'
                XLUtilities.writeXL(self.path, 'Sheet1', i ,4, output)
                time.sleep(5)
                self.lp.Logout();

            else:
                output ='Fail'
                XLUtilities.writeXL(self.path, 'Sheet1', i, 4, output)


'''    if act_Title == exp_Title:
                if self.exp == 'Pass':
                    self.lp.Logout();
                    lst_sts.append("Pass")
                elif self.exp == 'Fail':
                    self.lp.Logout();
                    lst_sts.append("Fail")

            elif act_Title != exp_Title:
                if self.exp == 'Pass':
                    #self.lp.Logout();
                    lst_sts.append("Fail")
                elif self.exp == 'Fail':
                    #self.lp.Logout();
                    lst_sts.append("Pass")

            if "Fail" not in lst_sts:
             self.logger.info("****************DDT PASSED****************")
             self.driver.close()
                #assert True
        else:
            self.logger.info("****************DDT FAILED****************")
            self.driver.close()
                #assert False
'''
