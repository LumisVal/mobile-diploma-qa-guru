import allure
from selene import browser, have, be

from utils.attachments import add_screenshot


# noinspection PyMethodMayBeStatic
class OnboardingPage:

    @allure.step("Проверить первый экран onboarding")
    def should_see_first_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("The Free Encyclopedia")
        )

        add_screenshot( "Первый экран onboarding")

    @allure.step("Проверить второй экран onboarding")
    def should_see_second_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("New ways to explore")
        )

        add_screenshot( "Второй экран onboarding")

    @allure.step("Проверить третий экран onboarding")
    def should_see_third_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("Reading lists")
        )

        add_screenshot( "Третий экран onboarding")

    @allure.step("Проверить четвертый экран onboarding")
    def should_see_fourth_screen(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/primaryTextView")
        ).should(
            have.text("Data & Privacy")
        )

        add_screenshot( "Четвертый экран onboarding")

    @allure.step("Нажать Continue")
    def continue_click(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

        add_screenshot( "После нажатия Continue")

    @allure.step("Нажать Get Started")
    def get_started(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/fragment_onboarding_done_button")
        ).click()

        add_screenshot( "После нажатия Get Started")

    @allure.step("Пройти onboarding")
    def skip_onboarding(self):
        self.continue_click()
        self.continue_click()
        self.continue_click()
        self.get_started()

        return self

    @allure.step("Пройти onboarding, если он отображается")
    def skip_onboarding_if_present(self):
        if browser.element(
                ("id", "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).matching(be.visible):
            self.continue_click()
            self.continue_click()
            self.continue_click()
            self.get_started()

        return self