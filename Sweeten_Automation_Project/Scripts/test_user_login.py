import Scripts.feature_config as fc
import common_functions as cf
import user_activities as ua
import Pages.validate_opened_pages as vp
import Pages.login_page as lp
import Pages.signup_page as sp
import Pages.editprofile_page as ep
import time
#Setting up browser
browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))

#Go to URL
cf.go_to_url(browser, fc.browser_details.get("url"))
time.sleep(2)

#Validate login page is opened
vp.validate_login_page(browser)

#Checking remember me
lp.check_remember_me(browser)

time.sleep(2)
#Login as an Owner
#ua.login(browser, fc.user_login_details.get('username'),fc.user_login_details.get('password'))

#Sign up as an owner
ua.create_account(browser, fc.user_signup_details.get('name'), fc.user_signup_details.get('email'), fc.user_signup_details.get('password'), fc.user_signup_details.get('confirm_password'), fc.user_signup_details.get('usertype_index'))

#update email
#ua.update_email(browser, fc.user_update_email.get("email"), fc.user_update_email.get("password"))

#cancel account
#ua.cancel_account(browser)

#create new project
#ua.create_project(browser, fc.create_project_values.get("longitude"), fc.create_project_values.get("latitude"), fc.create_project_values.get("minbudget"), fc.create_project_values.get("maxbudget"), fc.create_project_values.get("designservice",'No'), fc.create_project_values.get("buidservice",'No'))

#Edit created project
#ua.edit_project(browser, fc.edit_project_values.get("longitude",''), fc.edit_project_values.get("latitude",''), fc.edit_project_values.get("minbudget",''), fc.edit_project_values.get("maxbudget",''), fc.edit_project_values.get("designservice",False), fc.edit_project_values.get("buidservice",False), fc.edit_project_values.get("editbtnxpath"))

#Create new contractor
#ua.create_contractor(browser,fc.create_contractor_values.get("longitude"), fc.create_contractor_values.get("latitude"), fc.create_contractor_values.get("minbudget"), fc.create_contractor_values.get("maxbudget"), fc.create_contractor_values.get("designservice",'No'), fc.create_contractor_values.get("buidservice",'No'))

#Edit created contractor
#ua.edit_contractor(browser, fc.edit_contractor_values.get("longitude",''), fc.edit_contractor_values.get("latitude",''), fc.edit_contractor_values.get("minbudget",''), fc.edit_contractor_values.get("maxbudget",''), fc.edit_contractor_values.get("designservice",False), fc.edit_contractor_values.get("buidservice",False), fc.edit_contractor_values.get("editbtnxpath"))

#Show project
#ua.show_project_matches(browser, fc.show_project_match.get("show_project_xpath"), fc.show_project_match.get("status",''), fc.show_project_match.get("yes_btn_xpath",''), fc.show_project_match.get("no_btn_xpath",''))

#Show matched contractor
#ua.show_contractor_matches(browser, fc.show_contractor_match.get("show_match_xpath"), fc.show_contractor_match.get("status",''), fc.show_contractor_match.get("yes_btn_xpath",''), fc.show_contractor_match.get("no_btn_xpath",''))

#logout
ua.logout(browser)
time.sleep(3)
browser.quit()
