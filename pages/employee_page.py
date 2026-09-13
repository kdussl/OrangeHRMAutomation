import allure

from playwright.sync_api import Page

from pages.base_page import BasePage


class EmployeePage(BasePage):

    def __init__(self, page: Page):

        super().__init__(page)

        self.first_name = page.locator(
            "input[name='firstName']"
        )

        self.middle_name = page.locator(
            "input[name='middleName']"
        )

        self.last_name = page.locator(
            "input[name='lastName']"
        )

        self.employee_id = page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Employee Id"
        ).locator(
            "input"
        ).first

        self.save_buttons = page.get_by_role(
            "button",
            name="Save"
        )

        self.personal_details_heading = page.get_by_text(
            "Personal Details",
            exact=True
        )

    @allure.step("Add employee")
    def add_employee(
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

        self.save_buttons.first.click()

    @allure.step("Update employee name")
    def update_name(
        self,
        first_name,
        last_name
    ):

        self.fill(
            self.first_name,
            first_name
        )

        self.fill(
            self.last_name,
            last_name
        )

        self.save_buttons.first.click()

    def is_personal_details_displayed(self):

        return self.personal_details_heading.is_visible()