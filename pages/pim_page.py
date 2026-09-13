import allure

from playwright.sync_api import Page

from pages.base_page import BasePage


class PIMPage(BasePage):

    def __init__(self, page: Page):

        super().__init__(page)

        self.add_button = page.get_by_role(
            "button",
            name="Add"
        )

        self.employee_name_input = page.locator(
            "input[placeholder='Type for hints...']"
        ).first

        self.employee_id_input = page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Employee Id"
        ).locator(
            "input"
        )

        self.search_button = page.get_by_role(
            "button",
            name="Search"
        )

        self.reset_button = page.get_by_role(
            "button",
            name="Reset"
        )

        self.table_rows = page.locator(
            ".oxd-table-body .oxd-table-row"
        )

        self.first_row = self.table_rows.first

    @allure.step("Open Add Employee")
    def open_add_employee(self):

        self.click(
            self.add_button
        )

    @allure.step("Search employee")
    def search_employee(
        self,
        name=None,
        employee_id=None
    ):

        if name:

            self.fill(
                self.employee_name_input,
                name
            )

        if employee_id:

            self.fill(
                self.employee_id_input,
                employee_id
            )

        self.click(
            self.search_button
        )

    @allure.step("Reset employee search")
    def reset_search(self):

        self.click(
            self.reset_button
        )

    def get_employee_count(self):

        return self.table_rows.count()

    def is_employee_present(
        self,
        employee_name
    ):

        return self.page.get_by_text(
            employee_name,
            exact=True
        ).is_visible()

    def select_first_employee(self):

        self.first_row.get_by_role(
            "checkbox"
        ).check()

    def delete_selected_employee(self):

        delete_button = self.page.get_by_role(
            "button",
            name="Delete Selected"
        )

        delete_button.click()

        self.page.get_by_role(
            "button",
            name="Yes, Delete"
        ).click()