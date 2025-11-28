
import pytest,time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("initialize_driver")
class BaseClass:
    pass

class Test_class_income_calculator(BaseClass):
  def test_income_calculator(self):

      

      self.driver.get("https://payrup.com/")

      become_a_merchant = self.wait.until(
          EC.element_to_be_clickable((By.XPATH, "//a[text()='Become a Merchant']"))
      )
      become_a_merchant.click()

      # SWITCH TO NEW TAB
      self.driver.switch_to.window(self.driver.window_handles[1])
      print("Switched to new tab")
      time.sleep(3)
      income_cal = self.wait.until(
          EC.element_to_be_clickable((By.XPATH, "//button[text()='Income Calculator']"))
      )
      income_cal.click()
      time.sleep(3)
      for i in range(3):
          no_of_transaction = self.wait.until(
              EC.element_to_be_clickable((By.XPATH, f"//input[@id=':r{i}:']"))
          )
          no_of_transaction.send_keys("4")

      cal_btn = self.wait.until(
          EC.element_to_be_clickable((By.XPATH, "//button[text()='Calculate']"))
      )
      cal_btn.click()

















 





