import time
from utils.data_generator import generate_email
from Pages.basepage import basepage

class Signup(basepage):
    def __init__(self,page):
        super().__init__(page)

        self.Login_buttons= ":text('Signup / Login')" #locate_click
        self.Register_name= "Name" #get_by_placeholder
        self.Register_email= "//form[@action='/signup']/input[@name='email']" #locator
        self.Signup_button = ("button", "Signup") #get by role
        self.Mr_radio_button ="#id_gender1" #get by role
        self.Register_Password = ("textbox","Password *") #get_by_role
        #Date of Birth
        self.Day_drop_down ="//select[@id='days']" #select locator
        self.Day_options="6" #select text

        self.Month_drop_down = "//select[@id='months']" #select locator
        self.Month_options= "October" #select text

        self.Year_drop_down = "//select[@id='years']"  # select locator
        self.Year_options = "2000"  # select text

        self.Newsletter_check_box= "#newsletter" #check_box
        #Address information

        self.First_name=("textbox","First name *",)
        self.Last_name= "Last name *"  #label
        self.Company_name="#company" #locate
        self.Address1=("textbox", "Address * (Street address, P.O. Box, Company name, etc.)") #get by role
        self.Address2=("textbox","Address 2") #get by label
        self.Country_dropdown="//select[@id='country']"  #select locator
        self.Country_option= "India"
        self.State =("textbox","State *") #get_by_role
        self.City =("textbox", "City *")  #get_by_role
        self.zip_code="#zipcode" #locator
        self.Mobile =("textbox","Mobile Number *")
        self.Create_button=("button","Create Account") #get_by_role
        self.Continue_button="a:has-text('Continue')"

    def click_login(self):
        self.login_button(self.Login_buttons)
    def sign_up(self,signup_data):
        self.placeholder(self.Register_name, signup_data["register_name"])
        self.page.locator(self.Register_email).fill(generate_email())
        self.role_click(self.Signup_button)
    def register(self,signup_data):

        self.check_box(self.Mr_radio_button)
        self.role(self.Register_Password, signup_data["register_password"])
        #Date of birth
        self.select(self.Day_drop_down,self.Day_options)
        self.select(self.Month_drop_down,self.Month_options)
        self.select(self.Year_drop_down,self.Year_options)
        self.check_box(self.Newsletter_check_box)
        #Address
        self.role(self.First_name,signup_data["first_name"])
        self.label(self.Last_name,signup_data["last_name"])
        self.locate(self.Company_name,signup_data["company_name"])
        self.role(self.Address1,signup_data["address1"])
        self.role(self.Address2,signup_data["address2"])
        self.select(self.Country_dropdown,self.Country_option)
        self.role(self.State,signup_data["state"])
        self.role(self.City,signup_data["city"])
        self.locate(self.zip_code,signup_data["zipcode"])
        self.role(self.Mobile,signup_data["mobile"])
        self.role_click(self.Create_button)
        time.sleep(10)

    #continue button
    def continue_button(self):
        self.locate_click(self.Continue_button)








