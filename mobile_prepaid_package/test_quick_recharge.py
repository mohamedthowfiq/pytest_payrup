import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


class TestRecharge(softest.TestCase):

    def test_recharge_flow(self):
        # --- Setup Chrome options ---
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--start-maximized")

        service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=service)
        driver.get("https://payrup.com/")

        wait = WebDriverWait(driver, 15)

        # --- Step 1: Go to Prepaid Recharge tab ---
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='module-tab-0']"))
        ).click()

        # --- Step 2: Fill in details ---
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='mui-5']"))
        ).send_keys("7867987677")

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@id='mui-6']"))
        ).send_keys("11")

        # --- Step 3: Click Proceed to Pay ---
        time.sleep(2)
        proceed_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']"))
        )

        driver.execute_script("arguments[0].click();", proceed_btn)

        # --- Step 4: Verify popup appears ---
        try:
            popup = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'Sign in to payRup')]"))
            )
            popup_visible = True
        except:
            popup_visible = False

        # Soft Assertion
        self.soft_assert(self.assertTrue, popup_visible, "Sign-in popup did not appear")

        # Collect all soft assertions, fail if needed
        self.assert_all()
