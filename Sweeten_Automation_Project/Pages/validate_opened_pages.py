import Pages.page_validator_element as pe
import logger_file as logger

log=logger.set_log("page validation")

#Validate login page is opened
def validate_login_page(browser):
    if(pe.login_page in browser.page_source):
        log.info("Log in page validation is successful")
    else:
        log.error("Log in page validation is not successful")
        browser.quit()


#Validate home page is opened
def validate_home_page(browser):

    if(pe.home_page in browser.page_source):
        log.info("Home page validation is successful")
    else:
        log.error("Home page validation is not successful")
        browser.quit()


#Validate signup page is opened
def validate_signup_page(browser):

    if(pe.signup_page in browser.page_source):
        log.info("Sign up page validation is successful")
    else:
        log.error("Sign up page validation is not successful")
        browser.quit()

#Validate new signed up home page
def validate_new_signedup_homepage(browser):
    if(pe.new_sign_in in browser.page_source):
        log.info("New Sign up home page validation is successful")
    else:
        log.error("New Sign up home page validation is not successful")
        browser.quit()
        
#Validate edit profile page
def validate_edit_profile(browser):
    if(pe.editprofile_page in browser.page_source):
        log.info("Edit profile page validation is successful")
    else:
        log.error("Edit profile page validation is not successful")
        browser.quit()

#Validate updated profile
def validate_updated_profile(browser):
    if pe.update_profile in browser.page_source:
        log.info("Update profile validation is successful")
    else:
        log.error("Update profile validation is not successful")
        browser.quit()

#Validate Cancel account
def validate_cancelaccount(browser):
    if(pe.cancel_account in browser.page_source):
        log.info("Cancel account validation is successful")
    else:
        log.error("Cancel account validation is not successful")
        browser.quit()

#Validate new project page
def validate_new_project(browser):
    if(pe.newproject_page in browser.page_source):
        log.info("New project page validation is successful")
    else:
        log.error("New project page validation is not successful")
        browser.quit()

#Validate created project page
def validate_created_project(browser):
    if(pe.created_project_page in browser.page_source):
        log.info("Created project page validation is successful")
    else:
        log.error("Created project page validation is not successful")
        browser.quit()

#Validate edit project
def validate_edit_project(browser):
    if(pe.editproject_page in browser.page_source):
        log.info("Edit project page validation is successful")
    else:
        log.error("Edit project page validation is not successful")
        browser.quit()

#Validate edited project
def validate_edited_project(browser):
    if(pe.edited_project_page in browser.page_source):
        log.info("Edited project page validation is successful")
    else:
        log.error("Edited project page validation is not successful")
        browser.quit()
        
#Validate new contractor page
def validate_new_contractor(browser):
    if(pe.newcontractor_page in browser.page_source):
        log.info("New contractor page validation is successful")
    else:
        log.error("New contractor page validation is not successful")
        browser.quit()

#Validate created contractor page
def validate_created_contractor(browser):
    if(pe.created_contractor_page in browser.page_source):
        log.info("Created contractor page validation is successful")
    else:
        log.error("Created contractor page validation is not successful")
        browser.quit()

#Validate edit contractor
def validate_edit_contractor(browser):
    if(pe.editcontractor_page in browser.page_source):
        log.info("Edit contractor page validation is successful")
    else:
        log.error("Edit contractor page validation is not successful")
        browser.quit()

#Validate edited contractor
def validate_edited_contractor(browser):
    if(pe.edited_contractor_page in browser.page_source):
        log.info("Edited contractor page validation is successful")
    else:
        log.error("Edited contractor page validation is not successful")
        browser.quit()

#Validate show contractor page
def validate_show_contractor(browser):
    if(pe.show_contractor_page in browser.page_source):
        log.info("Show contractor page validation is successful")
    else:
        log.error("Show contractor page validation is not successful")
        browser.quit()
        
#Validate show project page
def validate_show_project(browser):
    if(pe.show_project_page in browser.page_source):
        log.info("Show project page validation is successful")
    else:
        log.error("Show project page validation is not successful")
        browser.quit()
        
#Validate logout
def validate_logout(browser):
    if(pe.logout_page in browser.page_source):
        log.info("Log out page validation is successful")
    else:
        log.error("Log out page validation is not successful")
        browser.quit()
