import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from selenium.webdriver.common.alert import Alert

class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen() #Logger

# passing setup from conftest file and saving
# for reusability , call the fixture from different file

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*******Test_002_DDT_Login***********")
        self.logger.info( "******Verifying Login test***********")
        self.driver = setup
        #self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        #self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.maximize_window()
        time.sleep(5)
        self.lp = LoginPage(self.driver)
        self.logger.info("Test")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows: ",self.rows)

        lst_status = []  #Empty List variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(10)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*****Passed*****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("*****Failed*****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("*****failed*****")

                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("*****Passed*****")

                    lst_status.append("Pass")

        if 'Fail' not in lst_status:
            self.logger.info("*****Login DDT test passed*****")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login DDT test failed*****")
            self.driver.close()
            assert False

        self.logger.info("****End of Login DDT Test")
        self.logger.info("***********Completed TC_LoginDDT_002*************")












