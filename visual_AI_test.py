from selenium import webdriver
from applitools.selenium import Eyes, Target
from delayed_assert import expect, assert_expectations
import os
import pytest

DEMO_APP_URL_V1 = "https://demo.applitools.com"
DEMO_APP_URL_V2 = "https://demo.applitools.com/hackathonV2.html"

# Login Page UI Elements Test
def test_AI_login_page_UI(setup):
    eyes = Eyes()
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']
    driver = setup
    #driver = webdriver.Chrome(executable_path=os.path.abspath( "./lib/chromedriver" ))
    eyes.open(driver, "Demo app", "login test", {'width': 800, 'height': 600})
    
    # version of app
    driver.get(DEMO_APP_URL_V1)
    #driver.get(DEMO_APP_URL_V2)

    eyes.check("Login Window test", Target.window())

    results = eyes.close(False)
    
    print(results) 
    eyes.abort()
    
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
def test_data_driven_AI_test(setup, username, password, message):
    driver = setup
    eyes = Eyes()
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']
    eyes.open(driver, "Demo app", "login test", {'width': 800, 'height': 600})
    
    driver.get('https://demo.applitools.com/hackathonV2.html')
    
    driver.find_element_by_id("username").send_keys(username)
    
    driver.find_element_by_id("password").send_keys(password)
    
    driver.find_element_by_id("log-in").click()
    
    eyes.check("Login Window test", Target.window())
    