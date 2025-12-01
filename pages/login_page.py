from pages.base_page import BasePage
from pages.safe_and_secure_mobile_recharges_and_bill_payment import SafeAndSecureMobileRechargesAndBillPayment
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    # traditional way of storing locators

    sign_in_to_payrup_box = (By.XPATH,"(//h5[text()='Sign in'])[2]")
    mobile_number_field=(By.XPATH,"//input[@type='number']")
    get_otp_button =(By.XPATH,"//div[@class='Signin_terms__3_clJ']//button[@type='button']")
    otp_field=(By.XPATH,"//form[@class='Signin_customform__Nne7P']//input")
    warning_message = (By.XPATH,"//form[contains(@class,'Signin_customform')]//div[contains(@class,'MuiBox-root')][1]//p[2]")
    
    def __init__(self,driver):
        super().__init__(driver)
    
    def goto_sign_in_to_payrup(self):
        self.click(self.sign_in_to_payrup_box)
        # self.driver.find_element(sign_in_to_payrup_box).click()

    def set_mobile_number(self,mobile_number):
        self.set(self.mobile_number_field,mobile_number)

    def click_get_otp(self):
        self.click(self.get_otp_button)
    
    def set_otp(self,otp):
        self.set(self.otp_field,otp)
        return SafeAndSecureMobileRechargesAndBillPayment(self.driver)
    
    # def log_into_application(self,mobile_number,otp):
    #     self.goto_sign_in_to_payrup()
    #     self.set_mobile_number(mobile_number)
    #     self.click_get_otp()
    #     self.set_otp(otp)

    def get_warning_message(self):
        return self.get_text(self.warning_message)