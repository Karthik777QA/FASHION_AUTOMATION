from Pages.login.login import login_page
from utils.data_reader import Datareader



def test_login_correct(page):
    #Getting data from the json file
    data = Datareader.jason_parser("test_data/signup_data.json")
    user = data["users1"]
    login_details = user["signup_details"]


    login_EP = login_page(page) #OBJECT FOT THE CLASS login_page
    login_EP.page.goto(user["home_page"],wait_until="domcontentloaded",
    timeout=60000) #home page is launched
    login_EP.verify("//div[@class='carousel-inner']//div[1]//div[1]//h1[1]//span[1]") #verify the landing in the home page
    print("Landed in the home page")
    login_EP.click_login()
    login_EP.login_set(login_details)
    login_EP.verify_user_name("ul[class='nav navbar-nav'] li a b",login_details["register_name"])
    print("User name is correct")


