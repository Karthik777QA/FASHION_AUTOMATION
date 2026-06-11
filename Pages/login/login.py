from pydoc import locate

from Pages.basepage import basepage

from conftest import *


class login_page(basepage):
    def __init__(self,page):
        super().__init__(page)

        self.Login_buttons_home = ":text('Signup / Login')"  # locate_click
        self.login_email= "//input[@data-qa='login-email']" #locator
        self.login_password="//input[@placeholder='Password']" #locator
        self.login_buttons ="button[data-qa='login-button']" #locator
        self.delete_button="a:has-text('Delete Account')" #locator
        self.delete_account="b:has-text('ACCOUNT DELETED!')" #for assertion.

    def click_login(self):
        self.login_button(self.Login_buttons_home)

    def login_set(self):

        self.locate(self.login_email,EMAIL_LOGIN)
        self.locate(self.login_password,REGISTER_PASSWORD)
        self.locate_click(self.login_buttons)





