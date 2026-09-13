import allure
import pytest

from config.config import (
    USERNAME,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@allure.epic("OrangeHRM")
@allure.feature("Login")
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.login
    @allure.title("Valid login")
    @allure.severity(
        allure.severity_level.CRITICAL
    )
    def test_valid_login(self, page):

        login = LoginPage(page)

        with allure.step(
            "Enter valid credentials"
        ):
            login.login(
                USERNAME,
                PASSWORD
            )

            dashboard = DashboardPage(page)

            dashboard.wait_for_dashboard()

            assert dashboard.is_dashboard_displayed()

    @pytest.mark.login
    @allure.title("Invalid username")
    @allure.severity(
        allure.severity_level.NORMAL
    )
    def test_invalid_username(self, page):

        login = LoginPage(page)

        login.login(
            "InvalidUser",
            PASSWORD
        )

        assert "Invalid credentials" in (
            login.get_error_message()
        )

    @pytest.mark.login
    @allure.title("Invalid password")
    def test_invalid_password(self, page):

        login = LoginPage(page)

        login.login(
            USERNAME,
            "InvalidPassword"
        )

        assert "Invalid credentials" in (
            login.get_error_message()
        )

    @pytest.mark.login
    @allure.title("Invalid username and password")
    def test_invalid_credentials(self, page):

        login = LoginPage(page)

        login.login(
            "InvalidUser",
            "InvalidPassword"
        )

        assert "Invalid credentials" in (
            login.get_error_message()
        )

    @pytest.mark.login
    @allure.title("Empty username")
    def test_empty_username(self, page):

        login = LoginPage(page)

        login.password_input.fill(
            PASSWORD
        )

        login.click_login()

        assert "Required" in (
            login.get_required_message()
        )

    @pytest.mark.login
    @allure.title("Empty password")
    def test_empty_password(self, page):

        login = LoginPage(page)

        login.username_input.fill(
            USERNAME
        )

        login.click_login()

        assert "Required" in (
            login.get_required_message()
        )

    @pytest.mark.smoke
    @pytest.mark.login
    @allure.title("Logout")
    def test_logout(self, page):

        login = LoginPage(page)

        login.login(
            USERNAME,
            PASSWORD
        )

        dashboard = DashboardPage(page)

        dashboard.logout()

        assert "/auth/login" in page.url