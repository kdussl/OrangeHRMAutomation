import allure
import pytest

from config.config import (
    USERNAME,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.employee_page import EmployeePage

from utils.test_data import generate_employee_data


def login(page):

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )


def open_pim(page):

    DashboardPage(page).open_pim()


@allure.epic("OrangeHRM")
@allure.feature("PIM")
class TestPIM:

    @pytest.mark.smoke
    @pytest.mark.pim
    @allure.title("Open PIM")
    def test_open_pim(self, page):

        login(page)

        open_pim(page)

        assert "/pim/viewEmployeeList" in page.url

    @pytest.mark.regression
    @pytest.mark.pim
    @allure.title("Search employee")
    def test_search_employee(self, page):

        login(page)

        open_pim(page)

        pim = PIMPage(page)

        pim.search_employee(
            name="John"
        )

        assert pim.get_employee_count() >= 0

    @pytest.mark.regression
    @pytest.mark.pim
    @allure.title("Reset employee search")
    def test_reset_employee_search(self, page):

        login(page)

        open_pim(page)

        pim = PIMPage(page)

        pim.search_employee(
            name="John"
        )

        pim.reset_search()

        assert "/pim/viewEmployeeList" in page.url

    @pytest.mark.regression
    @pytest.mark.pim
    @allure.title("Open Add Employee")
    def test_open_add_employee(self, page):

        login(page)

        open_pim(page)

        pim = PIMPage(page)

        pim.open_add_employee()

        assert "/pim/addEmployee" in page.url

    @pytest.mark.regression
    @pytest.mark.pim
    @allure.title("Add employee")
    def test_add_employee(self, page):

        login(page)

        open_pim(page)

        PIMPage(page).open_add_employee()

        data = generate_employee_data()

        employee = EmployeePage(page)

        employee.add_employee(
            data["first_name"],
            data["middle_name"],
            data["last_name"]
        )

        assert employee.is_personal_details_displayed()