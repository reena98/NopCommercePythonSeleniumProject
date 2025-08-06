from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_AddCustomer:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen().loggen()
    logger.info("Login test started.")

    def test_addCustomer(self, setup):
        self.logger.info("********************Test__001_Login****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.login = LoginPage(self.driver)
        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()

        self.addCust = AddCustomer(self.driver)

        self.addCust.clickOnCustomersMenu()

        self.addCust.clickOnCustomersMenuItem()

        self.addCust.clickOnAddNew()


