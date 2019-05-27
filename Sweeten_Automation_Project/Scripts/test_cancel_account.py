'''
Test steps
1. Open Browser
2. Login
3. Navigate to Edit profile
4. Click on Cancel my account
5. Verify account cancellation
'''
import Scripts.feature_config as fc
import common_functions as cf
import unittest
import time
import user_activities as ua
import Pages.validate_opened_pages as vp

class test_cancel_account(unittest.TestCase):
    
    def test_account_cancel(self):
    
        #Setting up 
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        cf.go_to_url(browser, fc.browser_details.get("url"))
        time.sleep(2)
        vp.validate_login_page(browser)
        
        #Login as an Owner
        ua.login(browser, fc.user_login_details.get('username'),fc.user_login_details.get('password'))
        
        #cancel account
        ua.cancel_account(browser)
        
        time.sleep(3)
        browser.quit()