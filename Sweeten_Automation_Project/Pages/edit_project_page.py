'''
Functionalities of Edit Project Page
'''
import logger_file as logger
import common_functions as cf
import Pages.Locators as locator
import time
import sys

log=logger.set_log("edit project page")

#Setting longitude
def edit_longitude(browser,longitude):
    longitude_elem=cf.find_an_element(browser, locator.find_by_id, locator.project_longitude_id)
    longitude_elem.clear()
    cf.send_inputs(longitude_elem, longitude)
    log.info("Longitude is set")

#Setting latitude
def edit_latitude(browser,latitude):
    latitude_elem=cf.find_an_element(browser, locator.find_by_id, locator.project_latitude_id)
    latitude_elem.clear()
    cf.send_inputs(latitude_elem, latitude)
    log.info("latitude is set")

#Setting minimum budget
def edit_min_budget(browser,min_budget):
    min_budget_elem=cf.find_an_element(browser, locator.find_by_id, locator.project_minbudget_id)
    min_budget_elem.clear()
    cf.send_inputs(min_budget_elem, min_budget)
    log.info("minimum budget is set")

#Setting maximum budget
def edit_max_budget(browser,max_budget):
    max_budget_elem=cf.find_an_element(browser, locator.find_by_id, locator.project_maxbudget_id)
    max_budget_elem.clear()
    cf.send_inputs(max_budget_elem, max_budget)
    log.info("maximum budget is set")

#Selecting design services check box
def edit_design_service(browser,status):
    design_service_status=cf.find_an_element(browser, locator.find_by_id, locator.project_designservice_id).is_selected()
    if status=="yes":
        cf.checkbox_select(browser, locator.project_designservice_id, design_service_status, locator.find_by_id)
        log.info("design service is checked")
    else:
        cf.checkbox_deselect(browser, locator.project_designservice_id, design_service_status, locator.find_by_id)
        log.info("design service is unchecked")

#selecting build service check box
def edit_build_service(browser,status):
    build_service_status=cf.find_an_element(browser, locator.find_by_id, locator.project_buildservice_id).is_selected()
    if status=="yes":
        cf.checkbox_select(browser, locator.project_buildservice_id, build_service_status, locator.find_by_id)
        log.info("build service is checked")
    else:
        cf.checkbox_deselect(browser, locator.project_buildservice_id, build_service_status, locator.find_by_id)
        log.info("build service is unchecked")

#Submit project
def click_submit(browser):
    submit_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.editproject_submitproject_xpath)
    cf.click_element(submit_btn)
    log.info("edited Project is submitted")