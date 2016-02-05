from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.get("https://www.ecod.com.ua/App/Pages/Login.aspx")

    def test_Login(self):
        driver = self.driver

        user_name        = "............"
        user_pass        = "......."

        emailFieldXpath        = '//input[@id="MainLogin_UserName"]'
        passFieldXpath         = '//input[@id="MainLogin_Password"]'
        loginButtonXpath       = '//input[@id="MainLogin_CtrlLoginButton"]'
        
        emailFieldElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(emailFieldXpath))
        passFieldElement    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passFieldXpath))
        loginButtonElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        
        emailFieldElement.clear()
        emailFieldElement.send_keys(user_name)
        passFieldElement.clear()
        passFieldElement.send_keys(user_pass)
        loginButtonElement.click()
        
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
