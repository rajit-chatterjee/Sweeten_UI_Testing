'''
Web page elements are listed in this file
'''
#Login page object
login_email_id="user_email"
login_password_id="user_password"
rememberme_id="user_remember_me"
login_btn_xpath="//*[@id='new_user']/div[4]/div[2]/div/div/button"
createaccount_btn_xpath="//*[@id='new_user']/div[4]/div[2]/div/div/a"

#Owner homepage object
createproject_btn_xpath="/html/body/div/a"


#Project creation and editing page objects
project_longitude_id="renovation_project_longitude"
project_latitude_id="renovation_project_latitude"
project_minbudget_id="renovation_project_min_budget"
project_maxbudget_id="renovation_project_max_budget"
project_designservice_id="renovation_project_is_design_service_req"
project_buildservice_id="renovation_project_is_build_service_req"
project_submitproject_btn_xpath="//*[@id='new_renovation_project']/div[7]/div/button"                                ""
project_backproject_btn_xpath="//*[@id='new_renovation_project']/div[7]/div/a"

#Submit button for edit project
editproject_submitproject_xpath="//*[@class='btn btn-success']"

#Created project page
project_edit_btn_xpath="/html/body/div/div/a[1]"
project_back_btn_xpath="/html/body/div/div/a[2]"

#Contractor homepage object
createcontractor_btn_xpath="/html/body/div/a"

#Contractor creation page
contractor_longitude_id="general_contractor_longitude"
contractor_latitude_id="general_contractor_latitude"
contractor_minbudget_id="general_contractor_min_project_budget"
contractor_maxbudget_id="general_contractor_max_project_budget"
contractor_designservice_id="general_contractor_is_offering_design_service"
contractor_buildservice_id="general_contractor_is_offering_build_service"
contractor_submitproject_btn_xpath="//*[@id='new_general_contractor']/div[7]/div/button"
contractor_backcontractor_btn_xpath="//*[@id='new_general_contractor']/div[7]/div/a"

#Submit button for edit contractor
editcontractor_submitcontractor_xpath="//*[@class='btn btn-success']"

#Created Contractor Page
contractor_edit_btn_xpath="/html/body/div/a[1]"
contractor_back_btn_xpath="/html/body/div/a[2]"
#Edit Profile button
editprofile_btn_xpath="//*[@id='bs-example-navbar-collapse-1']/p/a[1]"

#Edit profile page
edit_email_id="user_email"
edit_password_id="user_password"
edit_password_confirm_id="user_password_confirmation"
edit_current_password_id="user_current_password"
update_btn_xpath="//*[@id='edit_user']/div[5]/input"
cancelaccount_btn_xpath="/html/body/div/form[2]/input[2]"

#Signup page
signup_name_id="user_name"
signup_email_id="user_email"
signup_password_id="user_password"
signup_password_confirm_id="user_password_confirmation"
signup_usertype_id="user_user_type"
signup_btn_xpath="//*[@id='new_user']/div[6]/button/span"

#Logout button
logout_btn_xpath="//*[@id='bs-example-navbar-collapse-1']/p/a[2]"


#Find element by
find_by_id="ById"
find_by_xpath="ByXpath"
find_by_css="ByCssSelector"
find_by_link_text="ByLinkText"
find_by_class_name="ByClassName"