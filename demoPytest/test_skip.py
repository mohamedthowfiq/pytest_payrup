import pytest
from datetime import datetime
from selenium import webdriver


class TestLambdaTest:
  def test_sample_app_title(self):
    driver = webdriver.Chrome()
    driver.get("https://payrup.com/")
    pytest.skip()
    expected_title= "Safe & Secure Mobile Recharges & Bill Payment"
    print("line 1")
    assert expected_title == driver.title



# slipping test by using decorator
  @pytest.mark.skip(reason="Code has not deployed")
  def test_ecommerce_title(self):
    driver = webdriver.Chrome()
    self.driver.get("https://payrup.com/")
    expected_title= "Safe & Secure Mobile Recharges & Bill Payment"
    print("line 2")
    assert expected_title == self.driver.title

  @pytest.mark.skip()  #withour reason becoz it is not mandotory
  def test_special_offers(self):
     driver = webdriver.Chrome()
     driver.get("https://payrup.com/")
     expected_title = "Safe & Secure Mobile Recharges & Bill Payment"
     print("line 3")
     assert expected_title == self.driver.title

  @pytest.mark.skipif(
    datetime.now()<=datetime(2099,12,31),
    reason = "Repo is not complete until after finishing tutorial")
  def test_pytest_github_repo(self):
    driver = webdriver.Chrome()
    driver.get("https://github.com/mohamedthowfiq/pytest_payrup")
    expected_title="mohamedthowfiq/pytest_payrup"
    print("title :",expected_title)
    print("line 4")
    assert expected_title.__contains__(expected_title)

