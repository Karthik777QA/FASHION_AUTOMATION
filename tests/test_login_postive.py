from Pages.login.login import login_page

from conftest import *

def test_login_correct(page):
    login_EP = login_page(page) #OBJECT FOT THE CLASS login_page
    login_EP.page.goto(HOME_PAGE,wait_until="domcontentloaded",
    timeout=60000) #home page is launched
    login_EP.verify("//div[@class='carousel-inner']//div[1]//div[1]//h1[1]//span[1]") #verify the landing in the home page
    print("Landed in the home page")
    login_EP.click_login()
    login_EP.login_set()
    login_EP.verify_user_name("ul[class='nav navbar-nav'] li a b",REGISTER_NAME)
    print("User name is correct")


