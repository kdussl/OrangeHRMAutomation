import allure

from pages.base_page import BasePage
from utils.allure_helper import attach_screenshot


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # -----------------------------------------
        # Login Page Locators
        # -----------------------------------------

        self.username_input = page.locator(
            "input[name='username']"
        )

        self.password_input = page.locator(
            "input[name='password']"
        )

        self.login_button = page.locator(
            "button[type='submit']"
        )

        self.error_message = page.locator(
            ".oxd-alert-content-text"
        )

        self.required_messages = page.locator(
            ".oxd-input-group__message"
        )


    # =========================================
    # Valid Login
    # =========================================

    @allure.step("Login with valid credentials")
    def login(self, username, password):

        self.username_input.wait_for(
            state="visible"
        )

        self.enter_text(
            self.username_input,
            username,
            "Enter username"
        )

        self.enter_text(
            self.password_input,
            password,
            "Enter password"
        )

        self.click(
            self.login_button,
            "Click Login button"
        )

        # Valid login must navigate to Dashboard
        self.page.wait_for_url(
            "**/dashboard/index**",
            timeout=15000
        )

        attach_screenshot(
            self.page,
            "Login successful - Dashboard"
        )


    # =========================================
    # Invalid Login
    # =========================================

    @allure.step("Attempt login with invalid credentials")
    def attempt_login(self, username, password):

        self.username_input.wait_for(
            state="visible"
        )

        self.enter_text(
            self.username_input,
            username,
            "Enter username"
        )

        self.enter_text(
            self.password_input,
            password,
            "Enter password"
        )

        self.click(
            self.login_button,
            "Click Login button"
        )

        # Invalid login should remain on login page
        # and display an error message.
        self.error_message.wait_for(
            state="visible",
            timeout=10000
        )

        attach_screenshot(
            self.page,
            "Invalid login error"
        )


    # =========================================
    # Click Login
    # =========================================

    @allure.step("Click Login")
    def click_login(self):

        self.click(
            self.login_button,
            "Click Login button"
        )


    # =========================================
    # Get Error Message
    # =========================================

    def get_error_message(self):

        return self.error_message.inner_text()


    # =========================================
    # Get Required Message
    # =========================================

    def get_required_message(self):

        return self.required_messages.first.inner_text()


    # =========================================
    # Login Button Visibility
    # =========================================

    def is_login_button_visible(self):

        return self.login_button.is_visible()