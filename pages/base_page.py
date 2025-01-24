from playwright.sync_api import Page
from playwright_utils import PlaywrightManager


class BasePage:
    """
    Базовая (абстрактная) страница
    """
    def __init__(self, playwright_manager: PlaywrightManager):
        self.page: Page = playwright_manager.get_page()
