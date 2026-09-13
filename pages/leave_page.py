import allure

from playwright.sync_api import Page

from pages.base_page import BasePage


class LeavePage(BasePage):

    def __init__(self, page: Page):

        super().__init__(page)

        self.apply_link = page.get_by_text(
            "Apply",
            exact=True
        )

        self.my_leave_link = page.get_by_text(
            "My Leave",
            exact=True
        )

        self.leave_list_heading = page.get_by_role(
            "heading",
            name="Leave List",
            exact=True
        )

        self.search_button = page.get_by_role(
            "button",
            name="Search"
        )

        self.reset_button = page.get_by_role(
            "button",
            name="Reset"
        )

    @allure.step("Open Apply Leave")
    def open_apply_leave(self):

        self.click(
            self.apply_link
        )

    @allure.step("Open My Leave")
    def open_my_leave(self):

        self.click(
            self.my_leave_link
        )

    def search(self):

        self.click(
            self.search_button
        )

    def reset(self):

        self.click(
            self.reset_button
        )

    def is_leave_list_displayed(self):
        return self.leave_list_heading.is_visible()