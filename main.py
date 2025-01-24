from playwright_utils import PlaywrightManager
from pages.employer_auth_page import EmployerAuthPage
from pages.employer_dashboard_page import EmployerDashboardPage
from pages.vacancy_responses_page import VacancyResponsesPage
from pages.general_elements.header_element import HeaderElement


def main():
    with PlaywrightManager() as pw:
        auth_page = EmployerAuthPage(pw)
        auth_page.page.goto(auth_page.url)
        auth_page.page.locator(auth_page.Locators.login_via_password_button).click()
        auth_page.page.locator(auth_page.Locators.login_button).click()
        auth_page.page.locator(auth_page.Locators.email_input).type('awf2014@yandex.ru')
        auth_page.page.locator(auth_page.Locators.password_input).type('25394557Qq')
        auth_page.page.locator(auth_page.Locators.login_button).press('Enter')

        dashboard_page = EmployerDashboardPage(pw)
        dashboard_page.page.locator(HeaderElement.Locators.employer_vacancies_list_button_link).click()

        vacancy_responses_page = VacancyResponsesPage(
            pw,
            url='https://krasnodar.hh.ru/employer/vacancyresponses?vacancyId=116039293'
        )
        vacancy_responses_page.page.goto(vacancy_responses_page.url)
        vacancy_responses_page.page.locator('#response-filters div ~ svg').is_visible()
        vacancy_responses_page.page.locator('#response-filters div:text("Новые")').click()
        vacancy_responses_page.page.locator('#response-filters div ~ svg').is_hidden()
        cnt = vacancy_responses_page.page.locator('[data-qa="vacancy-real-responses"] > div h3[class*=title] a').count()
        print(cnt)
        vacancy_responses_page.page.pause()


if __name__ == "__main__":
    main()
