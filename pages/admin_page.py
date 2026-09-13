import allure

from playwright.sync_api import Page

from pages.base_page import BasePage


class AdminPage(BasePage):

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

        self.username_input = page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Username"
        ).locator(
            "input"
        )

        self.user_rows = page.locator(
            ".oxd-table-body .oxd-table-row"
        )

    @allure.step("Search admin user")
    def search_user(
        self,
        username
    ):

        self.fill(
            self.username_input,
            username
        )

        self.click(
            self.search_button
        )

    @allure.step("Reset admin search")
    def reset_search(self):

        self.click(
            self.reset_button
        )

    @allure.step("Open Add User")
    def open_add_user(self):

        self.click(
            self.add_button
        )

    def get_user_count(self):

        return self.user_rows.count()