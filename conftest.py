import os
import pytest
from core_utils import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from applitools.selenium import Eyes, Target

def pytest_addoption(parser):
    parser.addoption( "--env", action="store", default="qa",
                      help="options: dev or qa or stage or prod" )
    parser.addoption( "--config-file", action="store", default=None,
                      help="specify your config file" )
    
@pytest.fixture( scope="session", autouse=True )
def envopt(request):
    return request.config.getoption( "--env" )

@pytest.fixture( scope="session", autouse=True )
def configopt(request):
    return request.config.getoption( "--config-file" )

@pytest.fixture( scope="function" )
def Mgr(request, envopt, configopt):
    env = envopt
    cf = config.getConfig( env=envopt )

    if configopt:
        cf = config.getConfig( config=configopt )
        env = cf["system"]["env"]
        
    return {"conf": cf,
            "env": env
            }
    
    
@pytest.fixture(scope="function", autouse=False)
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path=os.path.abspath( "./lib/chromedriver" ))
    
    yield driver
    driver.quit()
    
    
@pytest.fixture(scope="function", autouse=False)
def eyes_setup(request):
    eyes = Eyes()
    eyes.api_key = os.environ['APPLITOOLS_API_KEY']  #"qnEyEOnPIYLpklckwTOnqynvZCJPePQgmIyX3buk2us110"   #os.environ['APPLITOOLS_API_KEY']
    
    yield eyes
    
    results = eyes.close(False)
    print(results) 
    eyes.abort()
    
"""   
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )
    if (report.outcome == "failed"):
        if  driver != None:
            if report.when == 'call' or report.when == "setup":  
                xfail = hasattr( report, 'wasxfail' )
                if (report.skipped and xfail) or (report.failed and not xfail):
                    file_name = report.nodeid.replace( "::", "_" ) + ".png"
                    get_fullpage_screenshot( file_name )
                    if file_name:
                        html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                               'onclick="window.open(this.src)" align="right"/></div>' % file_name
                        extra.append( pytest_html.extras.html( html ) )
                report.extra = extra
    
def get_fullpage_screenshot(name):
    if (driver):
        total_height = driver.execute_script( "return document.body.parentNode.scrollHeight" )
        total_width = driver.execute_script( "return document.body.parentNode.scrollWidth" )
        driver.set_window_size( total_width, total_height )
        driver.save_screenshot( name )
"""