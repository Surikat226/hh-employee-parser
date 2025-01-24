from playwright.sync_api import sync_playwright


class PlaywrightManager:
    def __init__(self, browser_type="chromium", headless: bool = False):
        self.browser_type = browser_type
        self.playwright = None
        self.browser = None
        self.page = None
        self.headless = headless

    def __enter__(self):
        self.playwright = sync_playwright().start()
        if self.browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_type == "webkit":
            self.browser = self.playwright.webkit.launch(headless=self.headless)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        self.page = self.browser.new_page()
        return self

    def get_page(self):
        return self.page

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.page:
            self.page.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
