import time,pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

@pytest.fixture()
#another name for post condition is teardown
def setup_teardown():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
    yield
    driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
    driver.find_element(By.XPATH,"//a[text()='Logout']").click()

    def test1_Admin_title(setup_teardown):
        driver.find_element(By.XPATH,"//span[text()='Admin']").click()
        assert driver.title == "OrangeHRM"
        print("Test 1 is complete")