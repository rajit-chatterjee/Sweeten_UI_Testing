import logger_file as logger
import common_functions as cf
import Pages.Locators as locator
import time
import sys

log=logger.set_log("create contractor page")

#Setting longitude
def set_longitude(browser,longitude):
    longitude_elem=cf.find_an_element(browser, locator.find_by_id, locator.contractor_longitude_id)
    cf.send_inputs(longitude_elem, longitude)
    log.info("Longitude is set")

#Setting latitude
def set_latitude(browser,latitude):
    latitude_elem=cf.find_an_element(browser, locator.find_by_id, locator.contractor_latitude_id)
    cf.send_inputs(latitude_elem, latitude)
    log.info("latitude is set")

#Setting minimum budget
def set_min_budget(browser,min_budget):
    min_budget_elem=cf.find_an_element(browser, locator.find_by_id, locator.contractor_minbudget_id)
    cf.send_inputs(min_budget_elem, min_budget)
    log.info("minimum budget is set")

#Setting maximum budget
def set_max_budget(browser,max_budget):
    max_budget_elem=cf.find_an_element(browser, locator.find_by_id, locator.contractor_maxbudget_id)
    cf.send_inputs(max_budget_elem, max_budget)
    log.info("maximum budget is set")

#Selecting design services check box
def select_design_service(browser):
    design_service_status=cf.find_an_element(browser, locator.find_by_id, locator.contractor_designservice_id).is_selected()
    cf.checkbox_select(browser, locator.contractor_designservice_id, design_service_status, locator.find_by_id)
    log.info("design service is checked")

#selecting build service check box
def select_build_service(browser):
    build_service_status=cf.find_an_element(browser, locator.find_by_id, locator.contractor_buildservice_id).is_selected()
    cf.checkbox_select(browser, locator.contractor_buildservice_id, build_service_status, locator.find_by_id)
    log.info("build service is checked")

#Submit project
def click_submit(browser):
    submit_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.contractor_submitproject_btn_xpath)
    cf.click_element(submit_btn)
    log.info("Created Project is submitted")