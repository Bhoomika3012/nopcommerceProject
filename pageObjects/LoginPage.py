from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    button_login_css="button[type='submit']"
    link_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_css).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()



