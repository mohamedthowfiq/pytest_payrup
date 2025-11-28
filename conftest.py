import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# @pytest.fixture(params=["chrome","firefox","edge"])
# @pytest.fixture(params=["chrome","edge"])
@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    if request.param == "chrome":
      driver = webdriver.Chrome()
    # elif request.param == "firefox":
    #   driver = webdriver.Firefox()
    # elif request.param == "edge":
    #   driver = webdriver.Edge()

    request.cls.driver = driver  # connects driver to class
    request.cls.wait = WebDriverWait(driver, 10, poll_frequency=2)# create WebDriverWait and attach to class
    
    print(f"Browser: {request.param}") 
    yield
    print("Close driver")
    driver.close()