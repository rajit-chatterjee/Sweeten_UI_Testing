'''
Test steps
1. Open Browser
2. Log in
3. Click on add project
4. Fill the details
5. Submit
6. Check the new project is created
7. log out
'''
import Scripts.feature_config as fc
import common_functions as cf
import unittest
import time
import user_activities as ua
import Pages.validate_opened_pages as vp

class test_add_project(unittest.TestCase):
    
    def test_project_add(self):
    
        #Setting up 
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        cf.go_to_url(browser, fc.browser_details.get("url"))
        time.sleep(2)
        vp.validate_login_page(browser)
        
        #Login as an Owner
        ua.login(browser, fc.owner_login_details.get('username'),fc.owner_login_details.get('password'))
        
        #Add new project
        ua.create_project(browser, fc.create_project_values.get("longitude"), fc.create_project_values.get("latitude"), fc.create_project_values.get("minbudget"), fc.create_project_values.get("maxbudget"), fc.create_project_values.get("designservice",'No'), fc.create_project_values.get("buidservice",'No'))
        
        #User logout
        ua.logout(browser)
        time.sleep(3)
        browser.quit()