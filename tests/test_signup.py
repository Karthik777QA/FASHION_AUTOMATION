import time
from asyncio import wait_for
from conftest import *

from Pages.login.signup import Signup

def test_signup(page):
    signup=Signup(page)
    signup.page.goto(HOME_PAGE,wait_until="networkidle",
    timeout=60000)

    #signup.verify("//div[@class='carousel-inner']//div[1]//div[1]//h1[1]//span[1]")#accertion to check the landing on home page.
    signup.click_login() #Click on login button in the home page.
    signup.verify(":text('New User Signup!')")#accertion to check the landing on the signup page
    print("The page is visible successfully")
    signup.sign_up()#Signup with email and password
    #signup.verify("b:has-text('ENTER ACCOUNT INFORMATION')")#Verify the landing on the registration page
    print("Landed on Registration page")
    signup.register()     #Filling Registration form
    time.sleep(7)
    signup.verify("p:has-text('Congratulations! Your new account has been successfully created!')")#Verify the account is created
    print("Account is created successfully")
    signup.continue_button() #click on the continue button
    signup.verify_user_name("ul[class='nav navbar-nav'] li a b","KARTHIK") #verify the username in the home page
    print("The User is correct in the home page")



