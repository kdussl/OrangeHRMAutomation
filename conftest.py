import pytest
import allure

from playwright.sync_api import sync_playwright

from config.config import (
    BASE_URL,
    BROWSER,
    HEADLESS,
    SLOW_MO
)


# =========================================
# Playwright Browser Fixture
# =========================================

@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as playwright:

        if BROWSER.lower() == "chromium":
            browser = playwright.chromium.launch(
                headless=HEADLESS,
                slow_mo=SLOW_MO
            )

        elif BROWSER.lower() == "firefox":
            browser = playwright.firefox.launch(
                headless=HEADLESS,
                slow_mo=SLOW_MO
            )

        elif BROWSER.lower() == "webkit":
            browser = playwright.webkit.launch(
                headless=HEADLESS,
                slow_mo=SLOW_MO
            )

        else:
            raise ValueError(
                f"Unsupported browser: {BROWSER}"
            )

        yield browser

        browser.close()


# =========================================
# Playwright Page Fixture
# =========================================

@pytest.fixture
def page(browser):

    page = browser.new_page()

    # Open OrangeHRM application
    page.goto(
        BASE_URL,
        wait_until="domcontentloaded"
    )

    yield page

    page.close()


# =========================================
# Allure Screenshot Hook
# =========================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    page = item.funcargs.get("page")

    if page is None:
        return

    if report.passed:
        screenshot_name = "Test Passed"

    elif report.failed:
        screenshot_name = "Test Failed"

    else:
        return

    try:

        allure.attach(
            page.screenshot(
                full_page=True
            ),
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )

    except Exception as error:

        print(
            f"Unable to capture screenshot: {error}"
        )