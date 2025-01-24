from pages.base_page import BasePage


class EmployerAuthPage(BasePage):
    """
    Экран авторизации работодателя
    """
    class Locators:
        login_via_password_button = '[data-qa="expand-login-by_password"]'
        email_input = '[data-qa="login-input-username"]'
        password_input = '[data-qa="login-input-password"]'
        login_button = '[data-qa="account-login-submit"]'

    def __init__(
        self,
        playwright_manager,
        url: str = 'https://hh.ru/login?role=employer'
    ):
        super().__init__(playwright_manager)
        self.url = url
