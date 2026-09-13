import allure
import pytest

from config.config import (
    USERNAME,
    PASSWORD
)

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.recruitment_page import RecruitmentPage

from utils.test_data import generate_candidate_data


def login(page):

    LoginPage(page).login(
        USERNAME,
        PASSWORD
    )


@allure.epic("OrangeHRM")
@allure.feature("Recruitment")
class TestRecruitment:

    @pytest.mark.smoke
    @pytest.mark.recruitment
    @allure.title("Open Recruitment")
    def test_open_recruitment(self, page):

        login(page)

        DashboardPage(page).open_recruitment()

        assert "/recruitment/viewCandidates" in page.url

    @pytest.mark.regression
    @pytest.mark.recruitment
    @allure.title("Search candidate")
    def test_search_candidate(self, page):

        login(page)

        DashboardPage(page).open_recruitment()

        recruitment = RecruitmentPage(page)

        recruitment.search_candidate()

        assert "/recruitment/viewCandidates" in page.url

    @pytest.mark.regression
    @pytest.mark.recruitment
    @allure.title("Open Add Candidate")
    def test_open_add_candidate(self, page):

        login(page)

        DashboardPage(page).open_recruitment()

        recruitment = RecruitmentPage(page)

        recruitment.open_add_candidate()

        assert "/recruitment/addCandidate" in page.url

    @pytest.mark.regression
    @pytest.mark.recruitment
    @allure.title("Enter candidate details")
    def test_enter_candidate_details(self, page):

        login(page)

        DashboardPage(page).open_recruitment()

        recruitment = RecruitmentPage(page)

        recruitment.open_add_candidate()

        data = generate_candidate_data()

        recruitment.enter_candidate(
            data["first_name"],
            data["middle_name"],
            data["last_name"]
        )

        assert (
            recruitment.first_name.input_value()
            == data["first_name"]
        )