import allure
import pytest

from config.config import (
    USERNAME,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage


def login(page):

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )


@allure.epic("OrangeHRM")
@allure.feature("Leave")
class TestLeave:

    @pytest.mark.smoke
    @pytest.mark.leave
    @allure.title("Open Leave module")
    def test_open_leave(self, page):

        login(page)

        DashboardPage(page).open_leave()

        assert "/leave/viewLeaveList" in page.url

    @pytest.mark.regression
    @pytest.mark.leave
    @allure.title("Verify Leave List")
    def test_leave_list(self, page):

        login(page)

        DashboardPage(page).open_leave()

        leave = LeavePage(page)

        assert leave.is_leave_list_displayed()

    @pytest.mark.regression
    @pytest.mark.leave
    @allure.title("Open Apply Leave")
    def test_apply_leave(self, page):

        login(page)

        DashboardPage(page).open_leave()

        leave = LeavePage(page)

        leave.open_apply_leave()

        assert "/leave/applyLeave" in page.url

    @pytest.mark.regression
    @pytest.mark.leave
    @allure.title("Open My Leave")
    def test_my_leave(self, page):

        login(page)

        DashboardPage(page).open_leave()

        leave = LeavePage(page)

        leave.open_my_leave()

        assert "/leave/viewMyLeaveList" in page.url