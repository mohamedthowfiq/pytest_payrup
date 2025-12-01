import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
  pass
class Test_Drivers(BaseClass):
  def test_multiple_browsers(self):
      self.driver.get("https://payrup.com/")
      title = self.driver.title
      print("Title :", title)
      assert title == "Safe & Secure Mobile Recharges & Bill Payment"