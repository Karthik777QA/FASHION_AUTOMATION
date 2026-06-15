from Pages.login.login import login_page
from Utils.data_reader import DataReader

def test_login_correct(page):
    data = DataReader.json_parser("Test_data/login_data.json")
    url  = DataReader.json_parser("config/config.json")
    login_data =data["login_credentials"]
    home_url = url["qa"]
    login_EP = login_page(page) #OBJECT FOT THE CLASS login_page
    login_EP.page.goto(home_url["base_url"],wait_until="domcontentloaded",
    timeout=60000) #home page is launched
    login_EP.verify("//div[@class='carousel-inner']//div[1]//div[1]//h1[1]//span[1]") #verify the landing in the home page
    print("Landed in the home page")
    login_EP.click_login()
    login_EP.login_set(login_data)
    login_EP.verify_user_name("ul[class='nav navbar-nav'] li a b","KARTHIK")


