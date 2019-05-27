'''
Functionalities of Edit Profile Page
'''
import logger_file as logger
import common_functions as cf
import Pages.Locators as locator
import time
import sys

log=logger.set_log("Edit Profile page")

#Change Email
def change_email(browser,email):
    changed_email=cf.find_an_element(browser, locator.find_by_id, locator.edit_email_id)
    changed_email.clear()
    cf.send_inputs(changed_email, email)
    log.info("User's email is changed")

#Change Password
def change_password(browser,password,confirmpassword):
    changed_password=cf.find_an_element(browser, locator.find_by_id, locator.edit_password_id)
    changed_confirmpassword=cf.find_an_element(browser, locator.find_by_id, locator.edit_password_confirm_id)
    cf.send_inputs(changed_password,password)
    cf.send_inputs(changed_confirmpassword,confirmpassword)
    log.info("New password and confirm password is set")

#Enter current password
def enter_currentpassword(browser,currentpassword):
    password=cf.find_an_element(browser, locator.find_by_id, locator.edit_current_password_id)
    cf.send_inputs(password,currentpassword)
    log.info("Current password is set")

#Update account
def click_update(browser):
    update_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.update_btn_xpath)
    cf.click_element(update_btn)
    log.info("Update button is clicked")

#Cancel account
def cancel_account(browser):
    cancel_account_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.cancelaccount_btn_xpath)
    cf.click_element(cancel_account_btn)
    time.sleep(2)
    cf.accept_alert(browser)
    log.info("User account has been cancelled")
    