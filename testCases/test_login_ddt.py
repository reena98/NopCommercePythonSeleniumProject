import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

class Test_001_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = "..\\TestData\\LoginData.xlsx"

    logger = LogGen().loggen()
    logger.info("Login test started.")

    def test_ddt_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        lst_status = []
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("No of rows: ", self.rows)

        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1',r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1',r, 2)
            self.expected = XLUtils.readData(self.path, 'Sheet1',r, 3)
            self.login.setUsername(self.username)
            self.login.setPassword(self.password)
            self.login.clickLogin()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("*******PASSED*********")
                    self.login.clickLogout()
                    lst_status.append('Pass')
                elif self.expected == "Fail":
                    self.logger.info("*******FAILED*********")
                    self.login.clickLogout()
                    lst_status.append('Fail')
            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("*******FAILED*********")
                    lst_status.append('Fail')
                elif self.expected == "Fail":
                    self.logger.info("*******PASSED*********")
                    lst_status.append('Pass')

        if "Fail" not in lst_status:
            self.logger.info("******test_ddt_login Passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("******test_ddt_login Failed*********")
            self.driver.close()
            assert False

