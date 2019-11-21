from selenium import webdriver
from selenium.webdriver.common.by import By
#from applitools.selenium import Eyes, Target
from delayed_assert import expect, assert_expectations
import os
import pytest

DEMO_APP_URL_V1 = "https://demo.applitools.com/hackathon.html"
DEMO_APP_URL_V2 = "https://demo.applitools.com/hackathonV2.html"

# Login Page UI Elements Test
def test_login_page_UI(setup):
    
    driver = setup
    
    # version V1 of demo app
    driver.get(DEMO_APP_URL_V2)
    
    # check for logo is present
    expect( len(driver.find_elements_by_xpath("//img[@src='img/logo-big.png']")) == 1 )
    
    # check the Login Form Header is present
    expect( driver.find_element_by_xpath("//h4[@class='auth-header']").text == "Login Form")
    
    # Assert Username label exists
    expect( driver.find_elements_by_xpath("//label")[0].text == "Username" )
    
    # Assert username placeholder text
    expect( driver.find_element_by_id("username").get_attribute("placeholder") == "Enter your username" )
    
    # Assert Password label exists
    expect( driver.find_elements_by_xpath("//label")[1].text == "Password" )
    
    # Assert Password placeholder text
    expect( driver.find_element_by_id("password").get_attribute("placeholder") == "Enter your password" )

    # Assert Sign in button exists
    expect( driver.find_element_by_id("log-in").text == "Sign in" )
    
    #Assert Remember Me checkbox/label exists
    expect( len(driver.find_elements_by_xpath("//input[@type='checkbox']")) == 1 )
    expect( driver.find_element_by_xpath("//label[@class='form-check-label']").text == "Remember Me" )
    
    #Assert Social icon Twitter exists
    expect( len(driver.find_elements_by_xpath("//img[@src='img/social-icons/twitter.png']")) == 1 )
    
    #Assert Social icon facebook exists
    expect( len(driver.find_elements_by_xpath("//img[@src='img/social-icons/facebook.png']")) == 1 )

    #Assert Social icon Linkedin exists
    expect( len(driver.find_elements_by_xpath("//img[@src='img/social-icons/linkedin.png']")) == 1 )
    
    
    assert_expectations()
    
#params for data driven test with marks
login_data = [ 
    pytest.param("some_user", "", "Password must be present"), 
    pytest.param("", "some_pwd", "Username must be present"), 
    pytest.param("", "", "Both Username and Password must be present"),   # update the error message to new in v2
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
def test_data_driven_test(setup, username, password, message):
    driver = setup
    
    driver.get(DEMO_APP_URL_V2)
    
    driver.find_element_by_id("username").send_keys(username)
    
    driver.find_element_by_id("password").send_keys(password)
    
    driver.find_element_by_id("log-in").click()
    
    if message != "Jack Gomez":
        assert(message == driver.find_element_by_xpath('//*[contains(@id,"random_id")]').text)
    else:
        assert(message == driver.find_element_by_id("logged-user-name-new").text)  #changes the id to reflect in version2 
 
#Table Sort Test
def test_table_sort_test(setup):
    driver = setup
    
    driver.get(DEMO_APP_URL_V2)
    
    driver.find_element_by_id("username").send_keys("ss")
    
    driver.find_element_by_id("password").send_keys("nn")
    
    driver.find_element_by_id("log-in").click()
    
    assert("Jack Gomez" == driver.find_element_by_id("logged-user-name-new").text)
    
    rows = driver.find_elements(By.XPATH,"//table[@id='transactionsTable']/tbody/tr")
    
    #amount = str(rows[0].find_elements(By.TAG_NAME,"td")[4].text)
    amounts = []
    for row in rows:
        sign = str(row.find_elements(By.TAG_NAME,"td")[4].text).split(" ")[0]
        amt = str(row.find_elements(By.TAG_NAME,"td")[4].text).split(" ")[1]
        amt = (sign+amt).replace(",","")
        amounts.append(float(amt))
        
    print("Before sorting: %s", amounts)
    
    print("After sorting: %s", sorted(amounts))
    
    driver.find_element_by_xpath("//th[@id='amount']").click()
    
    rows = driver.find_elements(By.XPATH,"//table[@id='transactionsTable']/tbody/tr")
    amounts_sorted = []
    for row in rows:
        sign = str(row.find_elements(By.TAG_NAME,"td")[4].text).split(" ")[0]
        amt = str(row.find_elements(By.TAG_NAME,"td")[4].text).split(" ")[1]
        amt = (sign+amt).replace(",","")
        amounts_sorted.append(float(amt))
        
    print("after table sorted : %s" ,amounts_sorted)
    
    assert amounts_sorted == sorted(amounts), "sorting is incorrect"
    
# Canvas Chart Test
def test_canvas_chart_test(setup):
    driver = setup
    
    driver.get(DEMO_APP_URL_V1)
    
    driver.find_element_by_id("username").send_keys("ss")
    
    driver.find_element_by_id("password").send_keys("nn")
    
    driver.find_element_by_id("log-in").click()
    
    #assert("Jack Gomez" == driver.find_element_by_id("logged-user-name-new").text)
    
    #Cannot access charts internal data through the DOM, it is built using single Canvas element (canvas technology)
    driver.find_element_by_id("showExpensesChart").click()
    
    
    driver.find_element_by_id("addDataset")

# Dynamic Content Test
def test_dynamic_content_test(setup):
    driver = setup
    
    driver.get("https://demo.applitools.com/hackathon.html?showAd=true")
    #driver.get("https://demo.applitools.com/hackathonV2.html?showAd=true")
    
    driver.find_element_by_id("username").send_keys("ss")
    
    driver.find_element_by_id("password").send_keys("nn")
    
    driver.find_element_by_id("log-in").click()
    
    images = driver.find_elements_by_xpath("//div[contains(@id,'flashSale')]/img")
    # Make sure both gifs exists.
    assert len(images) == 2, "Missing gifs"