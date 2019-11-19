import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from applitools.selenium import Eyes, Target

@pytest.fixture(scope="function", autouse=True)
def setup(request):
    driver = webdriver.Chrome(executable_path=os.path.abspath( "./lib/chromedriver" ))
    
    yield driver
    driver.quit()