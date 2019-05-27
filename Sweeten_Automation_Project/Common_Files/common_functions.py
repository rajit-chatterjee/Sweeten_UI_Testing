'''
This file contains the common functions that should be used to run any automation script on Callhub website.
New generic functions should be added here for future use
'''
from selenium import webdriver
import logger_file as logger
from selenium.webdriver.support.ui import Select
import time
import sys


log=logger.set_log("common functions")

#This function is for setting up the browser
def open_browser(browser_name, browser_path):
    try:
        
        if browser_name=="Chrome":
            try:
                browser=webdriver.Chrome(executable_path=browser_path)
                log.info("Found the browser.")
            except Exception as e:
                log.error("Browser path is incorrect. Please give correct path and try again.\n"+str(e))
                sys.exit()
    
        return browser
    except:
        log.error("Browser name does not match. Please use 'Chrome' as 'browser_name.'")
        sys.exit()
        
#This function is for going to the mentioned URL
def go_to_url(browser, url):
    try:
        browser.get(url)
        browser.maximize_window()
        time.sleep(5)
        log.info("Webpage has been opened")
    except Exception as e:
        log.error("Not able to open the URL")
        log.error(str(e))
        sys.exit()
        
#This function is for finding an element in the web page
def find_an_element(browser, find_by,element):
    try:
        
        if find_by=="ByXpath":
            element_1 = browser.find_element_by_xpath(element)
        elif find_by=="ByLinkText":
            element_1 = browser.find_element_by_link_text(element)
        elif find_by=="ByPartialLinkText":
            element_1=browser.find_element_by_partial_link_text(element)
        elif find_by=="ByCssSelector":
            element_1=browser.find_element_by_css_selector(element)
        elif find_by=="ById":
            element_1=browser.find_element_by_id(element)
        elif find_by=="ByClassName":
            element_1=browser.find_element_by_class_name(element)
        else:
            log.error("Find element with xpath, linktext, id etc.")
            sys.exit()
    except Exception as e:
        log.error("Element not found {}".format(element))
        log.error(str(e))
        sys.exit()
    return element_1

#this function is used when clicking is not done using click()
def execute_script_element(browser, element):
    try:
        browser.execute_script("arguments[0].click();", element)
        log.info("Element has been clicked.")
    except Exception as e:
        log.error("Element is not found.")
        log.error(str(e))
        sys.exit()

#This function is for clicking on the found element
def click_element(element):
    try:
        element.click()
    except Exception as e:
        log.error("Item is not clickable "+str(e))
        log.error("Try to click with execute_script()")
        sys.exit()
        
#This function is for sending user inputs to the UI
def send_inputs(element,value):
    try:
        element.send_keys(value)
    except Exception as e:
        log.error("Element is not valid")
        log.error(str(e))
        sys.exit()

#For accessing drop down
def drop_down(element,index):
    try:
        dropdown=Select(element)
        dropdown.select_by_index(index)
        log.info("Drop down is selected")
    except Exception as e:
        log.error("Drop down is not selected")
        log.error(str(e))
        sys.exit()
        
#For check box selection
def checkbox_select(browser,element,status,find_by):
    try:
        if status==False:
            checkbox_element=find_an_element(browser, find_by, element)
            click_element(checkbox_element)
            log.info("Checkbox is selected")
        else:
            log.info("Checkbox is already selected")
    except Exception as e:
        log.error("Checkbox is not selected")
        log.error(str(e))
        sys.exit()

#For check box deselection
def checkbox_deselect(browser,element,status,find_by):
    try:
        if status==True:
            checkbox_element=find_an_element(browser, find_by, element)
            click_element(checkbox_element)
            log.info("Checkbox is deselected")
        else:
            log.info("Checkbox is already deselected")
    except Exception as e:
        log.error("Checkbox is not deselected")
        log.error(str(e))
        sys.exit()
        
#Accept alert
def accept_alert(browser):
    try:
        alert=browser.switch_to.alert
        log.info(alert.text)
        alert.accept()
        log.info("Alert is accepted")
    except Exception as e:
        log.error("Alert is not accepted")
        log.error(str(e))
       
    
#Close the current browser or all the browsers
def close_browser(browser,option):
    try:
        if option=="Current":
            browser.close()
        if option=="All":
            browser.quit()
        log.info("Browser has been closed")
    except Exception as e:
        log.error("Please give proper option- 1. Current, 2. All")
        log.error(str(e))
        sys.exit()