from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utilities.test_date import TestDate


class TestLogin(BaseTest):
    def test_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.goto_sign_in_to_payrup()
        login_page.set_mobile_number(TestDate.mobie_number)
        login_page.click_get_otp()
        login_page.set_otp(TestDate.opt)
        actual_title = login_page.get_title()
        print("line 1")
        print(actual_title)
        assert actual_title == "Safe & Secure Mobile Recharges & Bill Payment"