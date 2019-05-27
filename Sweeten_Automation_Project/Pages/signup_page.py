'''
Functionalities of Signup Page
'''
import logger_file as logger
import common_functions as cf
import Pages.Locators as locator
import time
import sys

log=logger.set_log("Sign up page")

#Setting name
def set_name(browser,name):
    username=cf.find_an_element(browser, locator.find_by_id, locator.signup_name_id)
    cf.send_inputs(username, name)
    log.info("User's name is set")

#Set Email
def set_email(browser,email):
    username=cf.find_an_element(browser, locator.find_by_id, locator.signup_email_id)
    cf.send_inputs(username, email)
    log.info("User's email is set")

#Set Password
def set_password(browser,password):
    userpassword=cf.find_an_element(browser, locator.find_by_id, locator.signup_password_id)
    cf.send_inputs(userpassword, password)
    log.info("User's password is set")
    
#Set Confirm Password
def set_confirm_password(browser,confirmpassword):
    userconfirmpassword=cf.find_an_element(browser, locator.find_by_id, locator.signup_password_confirm_id)
    cf.send_inputs(userconfirmpassword, confirmpassword)
    log.info("User's confirm password is set")

#Set User Type
def set_usertype(browser,usertype_index):
    usertype=cf.find_an_element(browser, locator.find_by_id, locator.signup_usertype_id)
    cf.drop_down(usertype, usertype_index)
    log.info("User type is set")

#Click signup
def click_signup(browser):

    signup_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.signup_btn_xpath)
    cf.click_element(signup_btn)
    log.info("Sign up button is clicked")