from Utilities.customLogger import Log_Generate
from Utilities.readConfig import ReadConfigData
from basePages.admin_login_page import AdminLoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from testCases.conftest import setup


class Test_01_Admin_Login():
    loginPage_url = ReadConfigData.read_url_from_config()
    admin_username = ReadConfigData.read_username_from_config()
    admin_password = ReadConfigData.read_password_from_config()
    logger = Log_Generate.generate_log()

    def test_verify_admin_page_title(self,setup):
        self.logger.info("------- Landed on the Admin Login Page --------")

        self.driver = setup
        self.driver.get(self.loginPage_url)

        actual_title = self.driver.title
        expected_title = "OrangeHRM"

        if expected_title == actual_title:
            self.logger.info("------ Title Matched -------")
            assert True
            self.driver.close()

        else:
            self.logger.info("------ Title Not Matched -------")
            self.driver.close()
            assert False

    def test_valid_login(self,setup):
        self.driver = setup
        self.driver.get(self.loginPage_url)
        self.driver.implicitly_wait(10)

        self.lp = AdminLoginPageLocators(self.driver)
        self.lp.setEmail(self.admin_username)
        self.lp.setPassword(self.admin_password)
        self.lp.clickLoginButton()

        actual_title = self.driver.title
        expected_title = "OrangeHRM"

        if actual_title ==  expected_title:
            self.logger.info("------ Text Matched -------")
            assert True
            self.driver.close()

        else:
            self.logger.info("------ Text Not Matched -------")
            self.driver.close()
            assert False


