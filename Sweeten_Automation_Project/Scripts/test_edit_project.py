'''
Test steps
1. Open Browser
2. Click on Sign up
3. Fill all the fields
4. Sign up
'''
import Scripts.feature_config as fc
import common_functions as cf
import unittest
import time
import user_activities as ua
import Pages.validate_opened_pages as vp

class test_edit_project(unittest.TestCase):
    
    def test_project_edit(self):
    
        #Setting up 
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        cf.go_to_url(browser, fc.browser_details.get("url"))
        time.sleep(2)
        vp.validate_login_page(browser)
        
        #Login as an Owner
        ua.login(browser, fc.owner_login_details.get('username'),fc.owner_login_details.get('password'))
        
        #Edit new project
        ua.edit_project(browser, fc.edit_project_values.get("longitude"), fc.edit_project_values.get("latitude"), fc.edit_project_values.get("minbudget"), fc.edit_project_values.get("maxbudget"), fc.edit_project_values.get("designservice",'No'), fc.edit_project_values.get("buidservice",'No'))
        
        #User logout
        ua.logout(browser)
        time.sleep(3)
        browser.quit()