import allure

from playwright.sync_api import Page

from pages.base_page import BasePage


class RecruitmentPage(BasePage):

    def __init__(self, page: Page):

        super().__init__(page)

        self.add_button = page.get_by_role(
            "button",
            name="Add"
        )

        self.search_button = page.get_by_role(
            "button",
            name="Search"
        )

        self.reset_button = page.get_by_role(
            "button",
            name="Reset"
        )

        self.first_name = page.locator(
            "input[placeholder='First Name']"
        )

        self.middle_name = page.locator(
            "input[placeholder='Middle Name']"
        )

        self.last_name = page.locator(
            "input[placeholder='Last Name']"
        )

        self.email_input = page.locator(
            "input[placeholder='Type here']"
        )

    @allure.step("Open Add Candidate")
    def open_add_candidate(self):

        self.click(
            self.add_button
        )

    @allure.step("Search candidate")
    def search_candidate(self):

        self.click(
            self.search_button
        )

    def reset_search(self):

        self.click(
            self.reset_button
        )

    @allure.step("Enter candidate details")
    def enter_candidate(
        self,
        first_name,
        middle_name,
        last_name
    ):

        self.fill(
            self.first_name,
            first_name
        )

        self.fill(
            self.middle_name,
            middle_name
        )

        self.fill(
            self.last_name,
            last_name
        )