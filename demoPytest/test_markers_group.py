import pytest,time
from selenium import webdriver
from selenium.webdriver.common.by import By

pytestmark =[pytest.mark.regression,pytest.mark.sanity]
# pytestmark = pytest.mark.regression # file level mark

@pytest.mark.integration
@pytest.mark.smoke
def test_lambdatest_ajax_form():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
  time.sleep(3)
  driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
  driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
  driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
  title=driver.title

  assert title=="OrangeHRM","Title doesn't matched"


def test_e2e():
  print("End to End Test")

@pytest.mark.smoke
def test_login():
  print("Log Into Application")

@pytest.mark.smoke
def test_logout():
  print("Log Out Application")
