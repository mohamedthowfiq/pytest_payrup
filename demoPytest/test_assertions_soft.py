import softest
from selenium import webdriver
from selenium.webdriver.common.by import By

class AssertionsTest(softest.TestCase):
  pass
  def test_lambdatest_radio_button_demo_value(self):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("")
    driver.find_element(By.XPATH,"//h4[contains(text(),'Gender')]//following::input[@value='Male']").click()
    driver.find_element(By.XPATH,"//h4[contains(text(),'Age Group')]//following::input[@value='15 - 50']").click()
    driver.find_element(By.XPATH,"//button[text()='Get values']").click()
    gender = driver.find_element(By.CSS_SELECTOR,".genderbutton").text
    age_group = driver.find_element(By.CSS_SELECTOR,"groupradiobutton").text

    self.soft_assert(self.assertIs,"Male",gender,"Gender is not Correct")
    # assert gender=="Male","Gender is not Correct"
    self.soft_assert(self.assertTrue,driver.title.__contains__("Selenium Grid Online"))
    # assert driver.title.__contains__("Selenium Grid Online")

    self.soft_assert(self.assertIn,"51",age_group,"Age Group is not Correct")
    # assert "51" in age_group,"Age Group is not Correct"
    self.assert_all("This is a message we can write")