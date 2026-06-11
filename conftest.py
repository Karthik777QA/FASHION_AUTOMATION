import pytest
import time
import os
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        context =browser.new_context()
        page = context.new_page()
        page.set_default_timeout(60000)
        yield page
        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("Screenshots", exist_ok=True)
            page.screenshot(
                path=f"Screenshots/{item.name}.png",
                full_page=True
            )
def generate_email():
    return f"kartik{int(time.time())}@gmail.com"
HOME_PAGE="https://automationexercise.com/"
#Sign up details
REGISTER_NAME ="KARTHIK"
EMAIL =generate_email()
REGISTER_PASSWORD="Royalmech@777"
FIRST_NAME="Karthik"
lAST_NAME="Kishor"
COMPANY_NAME="TEST SUITE"
ADDRESS1="SMART CITY INFOPARK"
ADDRESS2="opp phase 2 campus kakkand"
STATE="KERALA"
CITY="KOCHI"
ZIPCODE="680675"
MOBILE="8932485912"
#LOGIN CREDENTIAL
EMAIL_LOGIN="testerrom145@gmail.com"
REGISTER_PASSWORD="Royalmech@777"