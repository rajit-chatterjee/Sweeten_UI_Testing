'''
This page contains all the user activity
'''
import Pages.login_page as lp
import Pages.signup_page as sp
import Pages.editprofile_page as ep
import Pages.edit_project_page as epp
import Pages.validate_opened_pages as vp
import Pages.Locators as locator
import Pages.owner_homepage as oh
import Pages.contractor_homepage as ch
import Pages.create_contractor_page as cc
import Pages.edit_contractor_page as ecp
import Pages.create_project_page as cp
import time
import common_functions as cf
import logger_file as logger
import Pages.page_validator_element as pe

log=logger.set_log("user activity")

#Login functionality
def login(browser,email,password):
    lp.set_username(browser, email)
    lp.set_password(browser, password)
    lp.click_login(browser)
    time.sleep(2)
    vp.validate_home_page(browser)
    
#Create new account functionality
def create_account(browser,name,email,password,confirmpassword,usertype_index):
    lp.click_signup(browser)
    time.sleep(2)
    vp.validate_signup_page(browser)
    sp.set_name(browser, name)
    sp.set_email(browser, email)
    sp.set_password(browser, password)
    sp.set_confirm_password(browser, confirmpassword)
    sp.set_usertype(browser, usertype_index)
    sp.click_signup(browser)
    time.sleep(2)
    vp.validate_new_signedup_homepage(browser)

#Edit profile
def update_email(browser,email,currentpassword):
    navigate_editprofile(browser)
    log.info("Going to change email")
    ep.change_email(browser, email)
    ep.enter_currentpassword(browser, currentpassword)
    ep.click_update(browser)
    log.info("Email is updated")
    time.sleep(2)
    vp.validate_updated_profile(browser)

#Update password
def update_password(browser,newpassword,confirmnewpassword,currentpassword):
    navigate_editprofile(browser)
    log.info("Going to change password")
    ep.change_password(browser, newpassword, confirmnewpassword)
    ep.enter_currentpassword(browser, currentpassword)
    ep.click_update(browser)
    time.sleep(2)
    vp.validate_updated_profile(browser)

#Navigate to edit profile
def navigate_editprofile(browser):
    log.info("Going to edit profile")
    editprofile_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.editprofile_btn_xpath)
    cf.click_element(editprofile_btn)
    log.info("Edit profile button is clicked")
    time.sleep(2)
    vp.validate_edit_profile(browser)

#cancel my account
def cancel_account(browser):
    navigate_editprofile(browser)
    ep.cancel_account(browser)
    time.sleep(2)
    vp.validate_cancelaccount(browser)

#Create a new project
def create_project(browser,longitude,latitude,min_budget,max_budget,design_service,build_service):
    oh.click_new_project(browser)
    time.sleep(5)
    vp.validate_new_project(browser)
    cp.set_longitude(browser, longitude)
    cp.set_latitude(browser, latitude)
    cp.set_min_budget(browser, min_budget)
    cp.set_max_budget(browser, max_budget)
    if design_service=='yes':
        cp.select_design_service(browser)
    if build_service=='yes':
        cp.select_build_service(browser)
    cp.click_submit(browser)
    log.info("New project is created")
    time.sleep(2)
    vp.validate_created_project(browser)

#Edit created project
def edit_project(browser,longitude,latitude,min_budget,max_budget,design_service,build_service,edit_btn_xpath):
    oh.click_edit_project(browser, edit_btn_xpath)
    time.sleep(2)
    vp.validate_edit_project(browser)
    if longitude is not '':
        epp.edit_longitude(browser, longitude)
    if latitude is not '':
        epp.edit_latitude(browser, latitude)
    if min_budget is not '':
        epp.edit_min_budget(browser, min_budget)
    if max_budget is not '':
        epp.edit_max_budget(browser, max_budget)
    epp.edit_design_service(browser, design_service)
    epp.edit_build_service(browser, build_service)
    epp.click_submit(browser)
    log.info("Project has been edited")
    time.sleep(2)
    vp.validate_edited_project(browser)


#Create a new contractor
def create_contractor(browser,longitude,latitude,min_budget,max_budget,design_service,build_service):
    ch.click_new_contractor(browser)
    time.sleep(5)
    vp.validate_new_contractor(browser)
    cc.set_longitude(browser, longitude)
    cc.set_latitude(browser, latitude)
    cc.set_min_budget(browser, min_budget)
    cc.set_max_budget(browser, max_budget)
    if design_service=='yes':
        cc.select_design_service(browser)
    if build_service=='yes':
        cc.select_build_service(browser)
    cc.click_submit(browser)
    log.info("New contractor is created")
    time.sleep(2)
    vp.validate_created_contractor(browser)

#Edit created contractor
def edit_contractor(browser,longitude,latitude,min_budget,max_budget,design_service,build_service,edit_btn_xpath):
    ch.click_edit_contractor(browser, edit_btn_xpath)
    time.sleep(2)
    vp.validate_edit_contractor(browser)
    if longitude is not '':
        ecp.edit_longitude(browser, longitude)
    if latitude is not '':
        ecp.edit_latitude(browser, latitude)
    if min_budget is not '':
        ecp.edit_min_budget(browser, min_budget)
    if max_budget is not '':
        ecp.edit_max_budget(browser, max_budget)
    ecp.edit_design_service(browser, design_service)
    ecp.edit_build_service(browser, build_service)
    ecp.click_submit(browser)
    log.info("Contractor has been edited")
    time.sleep(2)
    vp.validate_edited_contractor(browser)

#Show Matches
def show_contractor_matches(browser,show_match_xpath,status,yes_btn_xpath,no_btn_xpath):
    oh.show_matches(browser, show_match_xpath)
    time.sleep(2)
    vp.validate_show_contractor(browser)
    if pe.show_contractor_page in browser.page_source:
        log.info("Contractor matches found for the Project")
        if status=='yes':
            yes_btn=cf.find_an_element(browser, locator.find_by_xpath, yes_btn_xpath)
            cf.click_element(yes_btn)
            time.sleep(2)
            log.info("The contractor is accepted")
        elif status=='no':
            no_btn=cf.find_an_element(browser, locator.find_by_xpath, no_btn_xpath)
            cf.click_element(no_btn)
            time.sleep(2)
            log.info("The contractor is rejected")
        else:
            log.info("No action performed")
    else:
        log.info("No Matched Contractor found")

#Show Projects
def show_project_matches(browser,show_project_xpath,status,yes_btn_xpath,no_btn_xpath):
    ch.show_projects(browser, show_project_xpath)
    time.sleep(2)
    vp.validate_show_project(browser)
    if pe.show_project_page in browser.page_source:
        log.info("Project matches found for the Contractor")
        if status=='yes':
            yes_btn=cf.find_an_element(browser, locator.find_by_xpath, yes_btn_xpath)
            cf.click_element(yes_btn)
            time.sleep(2)
            log.info("The Project is accepted")
        elif status=='no':
            no_btn=cf.find_an_element(browser, locator.find_by_xpath, no_btn_xpath)
            cf.click_element(no_btn)
            time.sleep(2)
            log.info("The project is rejected")
        else:
            log.info("No action performed")
    else:
        log.info("No Matched Project found")
    
    
#Logout
def logout(browser):
    logout_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.logout_btn_xpath)
    cf.click_element(logout_btn)
    time.sleep(2)
    vp.validate_logout(browser)


