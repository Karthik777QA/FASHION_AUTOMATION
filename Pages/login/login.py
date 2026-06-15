from pydoc import locate

from Pages.basepage import basepage




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

    def login_set(self,login_data):

        self.locate(self.login_email,login_data["email_login"])
        self.locate(self.login_password,login_data["password_login"])
        self.locate_click(self.login_buttons)





