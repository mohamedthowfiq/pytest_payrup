from pages.base_page import BasePage
from utilities.locators import CauroselButtons
from pages.prepaid_mobile_recharge_page import PrepaidMobileRechargePage


class MobileRechargeAndDthPage(BasePage):

    def __init__(self,driver):
        self.locate = CauroselButtons
        super().__init__(driver)

    def mobile_recharge_and_dth(self):
        self.click(self.locate.mobile_recharge_and_dth)
        return PrepaidMobileRechargePage(self.driver)