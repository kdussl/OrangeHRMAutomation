import allure

from utils.allure_helper import attach_screenshot
from utils.logger import get_logger


class BasePage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    # ---------------------------------------------------------
    # Click
    # ---------------------------------------------------------

    @allure.step("Click element")
    def click(self, locator, step_name="Click element"):
        self.logger.info(f"Clicking element: {locator}")

        try:
            locator.click()
            attach_screenshot(self.page, step_name)

        except Exception:
            attach_screenshot(
                self.page,
                f"{step_name} - FAILED"
            )
            raise

    # ---------------------------------------------------------
    # Fill text
    # ---------------------------------------------------------

    @allure.step("Fill text")
    def fill(self, locator, text, step_name="Fill text"):
        self.logger.info(
            f"Filling text into element: {locator}"
        )

        try:
            locator.fill(text)
            attach_screenshot(self.page, step_name)

        except Exception:
            attach_screenshot(
                self.page,
                f"{step_name} - FAILED"
            )
            raise

    # ---------------------------------------------------------
    # Enter text
    # ---------------------------------------------------------

    @allure.step("Enter text")
    def enter_text(self, locator, text, step_name="Enter text"):
        return self.fill(
            locator,
            text,
            step_name
        )

    # ---------------------------------------------------------
    # Get text
    # ---------------------------------------------------------

    def get_text(self, locator):
        self.logger.info(
            f"Getting text from element: {locator}"
        )

        return locator.inner_text()

    # ---------------------------------------------------------
    # Check visibility
    # ---------------------------------------------------------

    def is_visible(self, locator):
        return locator.is_visible()

    # ---------------------------------------------------------
    # Wait for element
    # ---------------------------------------------------------

    def wait_for_visible(self, locator, timeout=10000):
        self.logger.info(
            f"Waiting for element to be visible: {locator}"
        )

        locator.wait_for(
            state="visible",
            timeout=timeout
        )

    # ---------------------------------------------------------
    # Select option
    # ---------------------------------------------------------

    @allure.step("Select option")
    def select_option(
        self,
        locator,
        option,
        step_name="Select option"
    ):
        self.logger.info(
            f"Selecting option: {option}"
        )

        try:
            locator.select_option(option)
            attach_screenshot(self.page, step_name)

        except Exception:
            attach_screenshot(
                self.page,
                f"{step_name} - FAILED"
            )
            raise

    # ---------------------------------------------------------
    # Check checkbox
    # ---------------------------------------------------------

    @allure.step("Check checkbox")
    def check(self, locator, step_name="Check checkbox"):
        self.logger.info(
            f"Checking checkbox: {locator}"
        )

        try:
            locator.check()
            attach_screenshot(self.page, step_name)

        except Exception:
            attach_screenshot(
                self.page,
                f"{step_name} - FAILED"
            )
            raise

    # ---------------------------------------------------------
    # Uncheck checkbox
    # ---------------------------------------------------------

    @allure.step("Uncheck checkbox")
    def uncheck(self, locator, step_name="Uncheck checkbox"):
        self.logger.info(
            f"Unchecking checkbox: {locator}"
        )

        try:
            locator.uncheck()
            attach_screenshot(self.page, step_name)

        except Exception:
            attach_screenshot(
                self.page,
                f"{step_name} - FAILED"
            )
            raise

    # ---------------------------------------------------------
    # Hover
    # ---------------------------------------------------------

    @allure.step("Hover over element")
    def hover(self, locator, step_name="Hover over element"):
        self.logger.info(
            f"Hovering over element: {locator}"
        )

        try:
            locator.hover()
            attach_screenshot(self.page, step_name)

        except Exception:
            attach_screenshot(
                self.page,
                f"{step_name} - FAILED"
            )
            raise

    # ---------------------------------------------------------
    # Press keyboard key
    # ---------------------------------------------------------

    @allure.step("Press keyboard key")
    def press(self, locator, key, step_name="Press keyboard key"):
        self.logger.info(
            f"Pressing key '{key}' on: {locator}"
        )

        try:
            locator.press(key)
            attach_screenshot(self.page, step_name)

        except Exception:
            attach_screenshot(
                self.page,
                f"{step_name} - FAILED"
            )
            raise