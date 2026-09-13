import allure
import pytest

from config.config import (
    USERNAME,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def login(page):

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )


@allure.epic("OrangeHRM")
@allure.feature("Dashboard")
class TestDashboard:

    @pytest.mark.smoke
    @pytest.mark.dashboard
    @allure.title("Verify Dashboard")
    def test_dashboard(self, page):

        login(page)

        dashboard = DashboardPage(page)

        assert dashboard.is_dashboard_displayed()

    @pytest.mark.dashboard
    @allure.title("Navigate to PIM")
    def test_navigate_to_pim(self, page):

        login(page)

        DashboardPage(page).open_pim()

        assert "/pim/viewEmployeeList" in page.url

    @pytest.mark.dashboard
    @allure.title("Navigate to Leave")
    def test_navigate_to_leave(self, page):

        login(page)

        DashboardPage(page).open_leave()

        assert "/leave/viewLeaveList" in page.url

    @pytest.mark.dashboard
    @allure.title("Navigate to Recruitment")
    def test_navigate_to_recruitment(self, page):

        login(page)

        DashboardPage(page).open_recruitment()

        assert "/recruitment/viewCandidates" in page.url

    @pytest.mark.dashboard
    @allure.title("Navigate to Admin")
    def test_navigate_to_admin(self, page):

        login(page)

        DashboardPage(page).open_admin()

        assert "/admin/viewSystemUsers" in page.url