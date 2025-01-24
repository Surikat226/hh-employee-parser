from pages.base_page import BasePage


class VacancyResponsesPage(BasePage):
    class Locators:
        pass

    def __init__(
        self,
        playwright_manager,
        url: str
    ):
        super().__init__(playwright_manager)
        self.url = url
