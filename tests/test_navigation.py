import allure

from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage


@allure.feature("Navigation")
@allure.title("Open Saved tab")
def test_open_saved_tab():
    onboarding_page = OnboardingPage()
    main_page = MainPage()

    onboarding_page.skip_onboarding()
    main_page.close_popup_if_present()

    main_page.open_saved()
    main_page.should_see_saved()


@allure.feature("Navigation")
@allure.title("Open Edits tab")
def test_open_edits_tab():
    onboarding_page = OnboardingPage()
    main_page = MainPage()

    onboarding_page.skip_onboarding()
    main_page.close_popup_if_present()

    main_page.open_edits()
    main_page.should_see_edits()