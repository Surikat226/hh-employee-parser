from playwright.sync_api import Playwright, sync_playwright


def run(pw: Playwright):
    engine = pw.chromium
    browser = engine.launch(headless=False, devtools=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://hh.ru/login?role=employer')
    page.locator('[data-qa="expand-login-by_password"]').click()
    page.locator('[data-qa="login-input-username"]').type('awf2014@yandex.ru')
    page.locator('[data-qa="login-input-password"]').type('25394557Qq')
    page.locator('[data-qa="account-login-submit"]').press('Enter')

    page.locator('[data-qa="link"][href*="/employer/vacancies"]').click()

    page.goto('https://krasnodar.hh.ru/vacancy/116039293?hhtmFrom=employer_vacancies')
    page.locator('[data-qa="vacancies-dashboard-responses-link"]').click()
    cnt = page.locator('[data-qa="vacancy-real-responses"] > div h3[class*=title] a').count()
    print(cnt)
    page.pause()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)
