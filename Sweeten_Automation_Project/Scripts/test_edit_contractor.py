'''
Test steps
1. Open Browser
2. Login
3. Click on edit for a created contractor
4. Edit the details with updated value
5. Validate edited contractor
6. log out
'''
import Scripts.feature_config as fc
import common_functions as cf
import unittest
import time
import user_activities as ua
import Pages.validate_opened_pages as vp

class test_edit_contractor(unittest.TestCase):
    
    def test_contractor_edit(self):
    
        #Setting up 
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        cf.go_to_url(browser, fc.browser_details.get("url"))
        time.sleep(2)
        vp.validate_login_page(browser)
        
        #Login as an Owner
        ua.login(browser, fc.contractor_login_details.get('username'),fc.contractor_login_details.get('password'))
        
        #Edit contractor
        ua.edit_contractor(browser, fc.edit_contractor_values.get("longitude",''), fc.edit_contractor_values.get("latitude",''), fc.edit_contractor_values.get("minbudget",''), fc.edit_contractor_values.get("maxbudget",''), fc.edit_contractor_values.get("designservice",False), fc.edit_contractor_values.get("buidservice",False), fc.edit_contractor_values.get("editbtnxpath"))
        
        #User logout
        ua.logout(browser)
        time.sleep(3)
        browser.quit()