import pytest
from selenium import webdriver
from utilities.test_date import TestDate
# @pytest.fixture(params=["chrome","firefox","edge"])
@pytest.fixture(params=["chrome"])
def initialize_driver(request):
  if request.param == "chrome":
    driver = webdriver.Chrome()
  # elif request.param == "firefox":
  #   driver = webdriver.Firefox()
  # elif request.param == "edge":
  #   driver = webdriver.Edge()
  request.cls.driver = driver  # connects driver to class
  print("Browser: ",request.param) 
  driver.get(TestDate.url)
  driver.maximize_window()
  yield
  print("Close driver")
  driver.close() 