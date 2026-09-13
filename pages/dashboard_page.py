import allure

from pages.base_page import BasePage
from utils.allure_helper import attach_screenshot


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.dashboard_heading = page.get_by_role(
            "heading",
            name="Dashboard",
            exact=True
        )

        self.admin_menu = page.get_by_role(
            "link",
            name="Admin",
            exact=True
        )

        self.pim_menu = page.get_by_role(
            "link",
            name="PIM",
            exact=True
        )

        self.leave_menu = page.get_by_role(
            "link",
            name="Leave",
            exact=True
        )

        self.recruitment_menu = page.get_by_role(
            "link",
            name="Recruitment",
            exact=True
        )

        self.user_dropdown = page.locator(
            ".oxd-userdropdown-tab"
        )

        self.logout_link = page.get_by_text(
            "Logout",
            exact=True
        )

    @allure.step("Wait for Dashboard")
    def wait_for_dashboard(self):

        self.page.wait_for_url(
            "**/dashboard/index**",
            timeout=15000
        )

        self.dashboard_heading.wait_for(
            state="visible"
        )

        attach_screenshot(
            self.page,
            "Dashboard displayed"
        )

    def is_dashboard_displayed(self):

        try:
            self.dashboard_heading.wait_for(
                state="visible",
                timeout=5000
            )

            return True

        except Exception:

            return False

    @allure.step("Open Admin")
    def open_admin(self):

        self.click(
            self.admin_menu,
            "Click Admin"
        )

    @allure.step("Open PIM")
    def open_pim(self):

        self.click(
            self.pim_menu,
            "Click PIM"
        )

    @allure.step("Open Leave")
    def open_leave(self):

        self.click(
            self.leave_menu,
            "Click Leave"
        )

    @allure.step("Open Recruitment")
    def open_recruitment(self):

        self.click(
            self.recruitment_menu,
            "Click Recruitment"
        )

    @allure.step("Logout")
    def logout(self):

        self.click(
            self.user_dropdown,
            "Open user menu"
        )

        self.click(
            self.logout_link,
            "Click Logout"
        )

        self.page.wait_for_url(
            "**/auth/login**",
            timeout=15000
        )

        attach_screenshot(
            self.page,
            "Logout successful - Login page"
        )