import allure

from pages.main_page import MainPage
from pages.onboarding_page import OnboardingPage


@allure.feature("Navigation")
@allure.title("Open More tab")
def test_open_more_tab():
    onboarding_page = OnboardingPage()
    main_page = MainPage()

    onboarding_page.skip_onboarding()
    main_page.close_popup_if_present()

    main_page.open_more()
    main_page.should_see_more()