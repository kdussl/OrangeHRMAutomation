import allure
import pytest

from config.config import (
    USERNAME,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage


def login(page):

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )


@allure.epic("OrangeHRM")
@allure.feature("Admin")
class TestAdmin:

    @pytest.mark.smoke
    @pytest.mark.admin
    @allure.title("Open Admin")
    def test_open_admin(self, page):

        login(page)

        DashboardPage(page).open_admin()

        assert "/admin/viewSystemUsers" in page.url

    @pytest.mark.regression
    @pytest.mark.admin
    @allure.title("Search Admin user")
    def test_search_user(self, page):

        login(page)

        DashboardPage(page).open_admin()

        admin = AdminPage(page)

        admin.search_user(
            USERNAME
        )

        assert admin.get_user_count() >= 0

    @pytest.mark.regression
    @pytest.mark.admin
    @allure.title("Reset Admin search")
    def test_reset_search(self, page):

        login(page)

        DashboardPage(page).open_admin()

        admin = AdminPage(page)

        admin.search_user(
            USERNAME
        )

        admin.reset_search()

        assert "/admin/viewSystemUsers" in page.url

    @pytest.mark.regression
    @pytest.mark.admin
    @allure.title("Open Add User")
    def test_open_add_user(self, page):

        login(page)

        DashboardPage(page).open_admin()

        admin = AdminPage(page)

        admin.open_add_user()

        assert "/admin/saveSystemUser" in page.url