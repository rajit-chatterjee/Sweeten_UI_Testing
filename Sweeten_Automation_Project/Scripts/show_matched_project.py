'''
Test steps
1. Open Browser
2. Login
3. Click on edit for a contractor to see the matched project
4. Accept or reject the project
5. Log out
'''
import Scripts.feature_config as fc
import common_functions as cf
import unittest
import time
import user_activities as ua
import Pages.validate_opened_pages as vp

class test_matched_project(unittest.TestCase):
    
    def test_project_matched(self):
    
        #Setting up 
        browser=cf.open_browser(fc.browser_details.get('browser_name'), fc.browser_details.get('browser_path'))
        cf.go_to_url(browser, fc.browser_details.get("url"))
        time.sleep(2)
        vp.validate_login_page(browser)
        
        #Login as an Owner
        ua.login(browser, fc.contractor_login_details.get('username'),fc.contractor_login_details.get('password'))
        
        #Show project
        ua.show_project_matches(browser, fc.show_project_match.get("show_project_xpath"), fc.show_project_match.get("status",''), fc.show_project_match.get("yes_btn_xpath",''), fc.show_project_match.get("no_btn_xpath",''))
        
        #User logout
        ua.logout(browser)
        time.sleep(3)
        browser.quit()