from selenium.webdriver.common.by import By

class AdminLoginPageLocators:

    emailFieldXpath = "//input[@placeholder='Username']"
    passwordFieldXpath = "//input[@placeholder='Password']"
    loginButtonXpath = "//button[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver


    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.emailFieldXpath).clear()
        self.driver.find_element(By.XPATH,self.emailFieldXpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.passwordFieldXpath).clear()
        self.driver.find_element(By.XPATH,self.passwordFieldXpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,self.loginButtonXpath).click()




