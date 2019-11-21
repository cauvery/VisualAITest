from selenium import webdriver
from applitools.selenium import Eyes, Target
from delayed_assert import expect, assert_expectations
import os
import pytest
from applitools.common.config import BatchInfo

''' Create the batch object and set the ID '''
b = BatchInfo("VISUAL_AI_BATCH")
b.id_ = "CGTEST_BATCH"


DEMO_APP_URL = "https://demo.applitools.com/hackathon.html"
#DEMO_APP_URL = "https://demo.applitools.com/hackathonV2.html"

# Login Page UI Elements Test
def test_AI_login_page_UI(setup, eyes_setup):
    driver = setup
    eyes = eyes_setup
    eyes.batch = b
    eyes.open(driver, "Hackathon Test", "loginUITest", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True
    
    driver.get(DEMO_APP_URL)

    eyes.check("Login Window test", Target.window())
    
#params for data driven test with marks
login_data = [ 
    pytest.param("some_user", "", "Password must be present"), 
    pytest.param("", "some_pwd", "Username must be present"), 
    pytest.param("", "", "Both Username and Password must be present"),
    pytest.param("aa", "bb", "Jack Gomez")
    ] 

#ids for the test items
id_names = [
   "password empty",
   "username empty",
   "both username password empty",
   "successful login"
]

# Data-Driven Test
@pytest.mark.parametrize("username, password, message", login_data, ids = id_names)
def test_data_driven_AI_test(setup, username, password, message, eyes_setup):
    driver = setup
    eyes = eyes_setup
    eyes.batch = b 
    eyes.open(driver, "Hackathon Test", "DataDrivenTest", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True
    driver.get(DEMO_APP_URL)
    
    driver.find_element_by_id("username").send_keys(username)
    
    driver.find_element_by_id("password").send_keys(password)
    
    driver.find_element_by_id("log-in").click()
    
    if message == "Jack Gomez":
        eyes.check("Welcome Window test ", Target.window())
    else:
        eyes.check("Login Window test ", Target.window())  
        
        
#Table Sort Test
def test_table_sort_test(setup, eyes_setup): 
    driver = setup
    eyes = eyes_setup
    eyes.batch = b 
    eyes.open(driver, "Hackathon Test", "TableSortTest", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True
    driver.get(DEMO_APP_URL)
    
    driver.find_element_by_id("username").send_keys("aa")
    
    driver.find_element_by_id("password").send_keys("bb")
    
    driver.find_element_by_id("log-in").click()
    
    driver.find_element_by_xpath("//th[@id='amount']").click()
    
    eyes.check("After table sort ", Target.window())
    
    
# Canvas Chart Test
def test_canvas_chart_test(setup, eyes_setup):
    driver = setup
    eyes = eyes_setup
    eyes.batch = b 
    eyes.open(driver, "Hackathon Test", "CanvasChartTest", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True
    
    driver.get(DEMO_APP_URL)
    
    driver.find_element_by_id("username").send_keys("ss")
    
    driver.find_element_by_id("password").send_keys("nn")
    
    driver.find_element_by_id("log-in").click()
    
    #assert("Jack Gomez" == driver.find_element_by_id("logged-user-name-new").text)
    
    driver.find_element_by_id("showExpensesChart").click()
    
    driver.find_element_by_id("addDataset")
    
    eyes.check("canvas chart data ", Target.window())
    
# Dynamic Content Test
def test_dynamic_content_test(setup, eyes_setup):
    driver = setup
    eyes = eyes_setup
    eyes.batch = b 
    eyes.open(driver, "Hackathon Test", "DynamicContentTest", {'width': 800, 'height': 600})
    eyes.force_full_page_screenshot = True
    
    driver.get(DEMO_APP_URL + "?showAd=true")
    
    driver.find_element_by_id("username").send_keys("ss")
    
    driver.find_element_by_id("password").send_keys("nn")
    
    driver.find_element_by_id("log-in").click()  
    
    eyes.check("dynamic content data ", Target.window())
