# from selenium.webdriver.common.by import By
# class BasePage:
#     """
#     The Purpose of a BasePage is ti contain methods
#     common to all Page Objects
#     """
#     def __init__(self,driver):
#         self.driver = driver

#     def find(self,*locator):
#         return self.driver.find_element(*locator)
    
#     def click(self,locator):
#         self.find(*locator).click()
#         # self.driver.find_element(*locator).click

#     def set(self,locator,value):
#         self.find(*locator).clear()
#         self.find(*locator).send_keys(value)

#     def get_text(self,locator):
#         return self.find(*locator).text
    
#     def get_title(self):
#         return self.driver.title
    
#     def click_right_menu_page(self,page_name):
#         # self.click(self.page(page_name))
#         page = By.XPATH,"//h5[text()='"+page_name+"']"
#         self.click(page)

#     # below method allows us to click page,check if page is visible & more actions
#     def page(self,page_name):
#         return By.XPATH,"//h5[text()='"+page_name+"']"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    The Purpose of a BasePage is to contain methods
    common to all Page Objects.
    """
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find(self, *locator):
        # Wait until element is visible on the page
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        # Wait until element is clickable
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def set(self, locator, value):
        element = self.find(*locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text
    
    def get_title(self):
        # Optional: wait until the page title is non-empty
        return self.driver.title
    
    def click_right_menu_page(self, page_name):
        page = (By.XPATH, f"//h5[text()='{page_name}']")
        self.click(page)

    def page(self, page_name):
        return (By.XPATH, f"//h5[text()='{page_name}']")
