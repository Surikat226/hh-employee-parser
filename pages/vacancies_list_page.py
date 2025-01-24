from pages.base_page import BasePage


class VacanciesListPage(BasePage):
    """
    Страница со списком вакансий работодателя
    """
    class Locators:
        pass

    def __init__(
        self,
        playwright_manager,
        url: str = 'https://krasnodar.hh.ru/employer/vacancies'
    ):
        super().__init__(playwright_manager)
        self.url = url
