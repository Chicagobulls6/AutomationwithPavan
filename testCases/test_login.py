import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

# passing setup from conftest file and saving
# for reusability , call the fixture from different file

    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info( "******Test_001_Login***********")
        self.logger.info("******** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(7)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info( "*********Home page title test PASSED*********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********Home page title test FAILED*********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info( "******Verifying Login teste***********")
        self.driver = setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        time.sleep(7)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title


        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******Verifying Login test PASSED***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("******Verifying Login test FAILED***********")
            assert False







