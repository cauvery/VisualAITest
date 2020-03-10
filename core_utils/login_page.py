#/usr/bin/env python
from selenium.webdriver.common.by import By

logger = log.getLogger(__name__)

class LoginPageLocators(object):
    USER_ID_INPUT=(By.ID, "username")
    PASSWORD_INPUT=(By.ID, "password")
    LOGIN_BUTTON=(By.ID,"log-in")


class LoginPage(BasePage):
    def __init__(self,Mgr):
        self.driver=Mgr["driver"]
        self.base_url=Mgr["conf"]

    def goto(self):
        self.driver.get(self.base_url+LoginPageLocators.PATH) 
        
    def login(self,username,password):
        logger.info("****** Login to Agency UI ********")
        self.goto()
        self.driver.find_element(*LoginPageLocators.USER_ID_INPUT).click()
        self.driver.find_element(*LoginPageLocators.USER_ID_INPUT).clear()
        self.driver.find_element(*LoginPageLocators.USER_ID_INPUT).send_keys(username)
        
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).click()
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).clear()
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()