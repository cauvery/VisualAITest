from selenium import webdriver
from applitools.selenium import Eyes, Target
from delayed_assert import expect, assert_expectations
import os
import pytest
from applitools.common.config import BatchInfo

''' Create the batch object and set the ID '''
b = BatchInfo("VISUAL_AI_EB")
b.id_ = "EB_BATCH"


nixle_URL = "https://agency-stage.nixle.com/login/"

# Login Page UI Elements Test
@pytest.mark.skip
def test_AI_login_page_UI(setup, eyes_setup):
    driver = setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open(driver, "EBTest", "EBUITest", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True
    
    driver.get(nixle_URL)

    eyes.check("Login Window test", Target.window())
    
#params for data driven test with marks
login_data = [ 
    pytest.param("cguda", "cgnixtest12")
    ] 


# Data-Driven Test
@pytest.mark.parametrize("username, password", login_data)
def test_data_driven_AI_test(setup, username, password, eyes_setup):
    driver = setup
    eyes = eyes_setup
    eyes.batch = b 
    eyes.open(driver, "EBTest", "EBUITest", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True
    driver.get(nixle_URL)
    
    driver.find_element_by_id("id_username").send_keys(username)
    
    driver.find_element_by_id("id_password").send_keys(password)
    
    eyes.check("EB test", Target.window())
    
    driver.find_element_by_xpath("//button[@type='submit']").submit()
    
    eyes.check("EB test", Target.window())