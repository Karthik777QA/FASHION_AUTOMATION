import pytest

class basepage:
    def __init__(self,page):
        self.page=page
    def locate(self,locator,text):
        self.page.locator(locator).fill(text)
    def locate_click(self,locator):
        self.page.locator(locator).click()
    def role(self,locator,text):
        role,name=locator
        self.page.get_by_role(role,name=name).fill(text)
    def role_click(self,locator):
        role,name = locator
        self.page.get_by_role(role,name=name).click()
    def text(self,locator):
        self.page.get_by_text(locator)
    def select(self,locator,text):
        self.page.locator(locator).select_option(text)
    def check_box(self,locator):
        self.page.locator(locator).check()
    def label(self,locator,text):
        self.page.get_by_label(locator).fill(text)
    def placeholder(self,locator,text):
            self.page.get_by_placeholder(locator).fill(text)
    def verify(self,locator):
        assert self.page.locator(locator).is_visible()

    def verify_user_name(self, locator, user_name):
        text = self.page.locator(locator).text_content()

        print("Expected:", user_name)
        print("Actual:", text)

        assert user_name == text

        #login button in home page

    def login_button(self,locator):
        self.locate_click(locator)

