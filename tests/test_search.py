import allure

from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage
from pages.search_page import SearchPage


@allure.feature("Search")
@allure.title("Search article in Wikipedia")
def test_search_article():
    onboarding_page = OnboardingPage()
    main_page = MainPage()
    search_page = SearchPage()

    onboarding_page.skip_onboarding()
    main_page.close_popup_if_present()

    search_page.open_search()
    search_page.type_query("Python")
    search_page.should_have_results()


@allure.feature("Article")
@allure.title("Open article from search results")
def test_open_article_from_search_results():
    onboarding_page = OnboardingPage()
    main_page = MainPage()
    search_page = SearchPage()

    onboarding_page.skip_onboarding()
    main_page.close_popup_if_present()

    search_page.open_search()
    search_page.type_query("Python")
    search_page.should_have_results()