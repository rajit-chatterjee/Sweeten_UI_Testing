import logger_file as logger
import common_functions as cf
import Pages.Locators as locator
import time
import sys

log=logger.set_log("login page")

#Setting email
def set_username(browser,email):
    username=cf.find_an_element(browser, locator.find_by_id, locator.login_email_id)
    cf.send_inputs(username, email)
    log.info("User name is set")

#Setting password
def set_password(browser,password):
    password_elem=cf.find_an_element(browser, locator.find_by_id, locator.login_password_id)
    cf.send_inputs(password_elem, password)
    log.info("Password is set")

#Check remember me check box        
def check_remember_me(browser):
    
    remember_me_status=cf.find_an_element(browser, locator.find_by_id, locator.rememberme_id).is_selected()
    cf.checkbox_select(browser, locator.rememberme_id, remember_me_status, locator.find_by_id)
    log.info("remember me is set")
    

#Click login button
def click_login(browser):

    login_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.login_btn_xpath)
    cf.click_element(login_btn)
    log.info("Login button is clicked")


#Click Signup button
def click_signup(browser):
    
    signup_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.createaccount_btn_xpath)
    cf.click_element(signup_btn)
    log.info("Sign up button is clicked")
