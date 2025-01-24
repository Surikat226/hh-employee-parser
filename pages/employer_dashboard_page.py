from pages.base_page import BasePage


class EmployerDashboardPage(BasePage):
    """
    Дашборд работодателя с информацией по вакансиям
    """
    class Locators:
        login_via_password_button = 'https://hh.ru/login?role=employer'
        email_input = '[data-qa="login-input-username"]'
        password_input = '[data-qa="login-input-password"]'

    def __init__(self, playwright_manager):
        super().__init__(playwright_manager)
