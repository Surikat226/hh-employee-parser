from pages.base_page import BasePage


class VacancyPage(BasePage):
    """
    Страница конкретной вакансии
    url страницы указывается сразу же при создании объекта страницы, т.к. вакансии всегда разные
    """
    class Locators:
        pass

    def __init__(
        self,
        playwright_manager,
        url: str
    ):
        super().__init__(playwright_manager)
        self.url = url
