'''
Functionalities of Contractor Home Page
'''

import logger_file as logger
import common_functions as cf
import Pages.Locators as locator

log=logger.set_log("Contractor home page")

#Create new General Contractor
def click_new_contractor(browser):
    log.info("Going to click new contractor button")
    new_contractor_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.createcontractor_btn_xpath)
    cf.click_element(new_contractor_btn)
    log.info("New contractor button is clicked")

#Edit existing project
def click_edit_contractor(browser,edit_btn_xpath):
    edit_btn=cf.find_an_element(browser, locator.find_by_xpath, edit_btn_xpath)
    cf.click_element(edit_btn)
    log.info("Edit button is clicked")

#Show matches
def show_projects(browser,show_projects_xpath):
    show_project_btn=cf.find_an_element(browser, locator.find_by_xpath, show_projects_xpath)
    cf.click_element(show_project_btn)
    log.info("Show project button is clicked")



