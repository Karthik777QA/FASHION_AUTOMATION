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

HOME_PAGE="https://automationexercise.com/"
#Sign up details


