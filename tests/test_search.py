import allure

from pages.article_page import ArticlePage
from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage
from pages.search_page import SearchPage


@allure.feature("Search")
@allure.title("Search article in Wikipedia")
def test_search_article():
    OnboardingPage().skip_onboarding()
    MainPage().close_popup_if_present()

    search_page = SearchPage()
    search_page.open_search()
    search_page.type_query("Python")
    search_page.should_have_result("Python (programming language)")


@allure.feature("Article")
@allure.title("Open article from search results")
def test_open_article_from_search_results():
    OnboardingPage().skip_onboarding()
    MainPage().close_popup_if_present()

    search_page = SearchPage()
    search_page.open_search()
    search_page.type_query("Python")
    search_page.open_result("Python (programming language)")

    ArticlePage().should_have_title("Python (programming language)")