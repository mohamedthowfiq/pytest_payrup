import pytest
from selenium import webdriver

# @pytest.fixture(params=["chrome","firefox","edge"])
@pytest.fixture(params=["chrome","edge"])
def initialize_driver(request):
  if request.param == "chrome":
    driver = webdriver.Chrome()
  # elif request.param == "firefox":
  #   driver = webdriver.Firefox()
  elif request.param == "edge":
    driver = webdriver.Edge()
  request.cls.driver = driver  # connects driver to class
  print("Browser: ",request.param) 
  yield
  print("Close driver")
  driver.close()