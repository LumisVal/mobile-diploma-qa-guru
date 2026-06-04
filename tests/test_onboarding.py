import allure

from pages.onboarding_page import OnboardingPage


@allure.title("Wikipedia onboarding")
def test_onboarding():
    page = OnboardingPage()

    page.should_see_first_screen()
    page.continue_click()

    page.should_see_second_screen()
    page.continue_click()

    page.should_see_third_screen()
    page.continue_click()

    page.should_see_fourth_screen()
    page.get_started()