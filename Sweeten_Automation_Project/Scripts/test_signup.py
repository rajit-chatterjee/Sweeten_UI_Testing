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

class test_signup(unittest.TestCase):
    
    def test_user_signup(self):
    
        #Setting up 
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        cf.go_to_url(browser, fc.browser_details.get("url"))
        time.sleep(2)
        vp.validate_login_page(browser)
        
        #User Signup
        ua.create_account(browser, fc.user_signup_details.get('name'), fc.user_signup_details.get('email'), fc.user_signup_details.get('password'), fc.user_signup_details.get('confirm_password'), fc.user_signup_details.get('usertype_index'))
        
        #User logout
        ua.logout(browser)
        time.sleep(3)
        browser.quit()
