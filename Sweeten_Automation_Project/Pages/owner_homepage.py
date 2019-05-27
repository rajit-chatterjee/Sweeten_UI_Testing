import logger_file as logger
import common_functions as cf
import Pages.Locators as locator
import time
import sys

log=logger.set_log("Owner home page")

#Create new Project
def click_new_project(browser):
    new_project_btn=cf.find_an_element(browser, locator.find_by_xpath, locator.createproject_btn_xpath)
    cf.click_element(new_project_btn)
    log.info("New project button is clicked")

#Edit existing project
def click_edit_project(browser,edit_btn_xpath):
    edit_btn=cf.find_an_element(browser, locator.find_by_xpath, edit_btn_xpath)
    cf.click_element(edit_btn)
    log.info("Edit button is clicked")

#Show matches
def show_matches(browser,show_match_xpath):
    show_match_btn=cf.find_an_element(browser, locator.find_by_xpath, show_match_xpath)
    cf.click_element(show_match_btn)
    log.info("Show match button is clicked")



