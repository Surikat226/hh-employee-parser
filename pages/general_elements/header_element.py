from pages.base_page import BasePage


class HeaderElement(BasePage):
    """
    Общая шапка с локаторами
    """
    class Locators:
        employer_vacancies_list_button_link = '[data-qa="link"][href*="/employer/vacancies"]'

    def __init__(
        self,
        playwright_manager,
    ):
        super().__init__(playwright_manager)
