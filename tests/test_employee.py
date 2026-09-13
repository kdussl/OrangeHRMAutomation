import allure
import pytest

from config.config import (
    USERNAME,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage


def login(page):

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )


@allure.epic("OrangeHRM")
@allure.feature("Employee")
class TestEmployee:

    @pytest.mark.regression
    @pytest.mark.employee
    @allure.title("Search existing employee")
    def test_search_existing_employee(self, page):

        login(page)

        DashboardPage(page).open_pim()

        pim = PIMPage(page)

        pim.search_employee(
            name="Admin"
        )

        assert pim.get_employee_count() >= 0

    @pytest.mark.regression
    @pytest.mark.employee
    @allure.title("Search employee with invalid data")
    def test_search_invalid_employee(self, page):

        login(page)

        DashboardPage(page).open_pim()

        pim = PIMPage(page)

        pim.search_employee(
            name="ZZZZZZZZZZ"
        )

        assert pim.get_employee_count() == 0