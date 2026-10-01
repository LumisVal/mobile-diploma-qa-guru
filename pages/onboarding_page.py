import allure
from selene import browser, be

from utils.attachments import add_screenshot


# noinspection PyMethodMayBeStatic
class OnboardingPage:

    @allure.step("Проверить первый экран onboarding")
    def should_see_first_screen(self):
        browser.element(("xpath", '//*[@text="All the world\'s knowledge"]')).should(be.visible)
        add_screenshot("Первый экран onboarding")

    @allure.step("Проверить второй экран onboarding")
    def should_see_second_screen(self):
        browser.element(("xpath", '//*[@text="Data & Privacy"]')).should(be.visible)
        add_screenshot("Второй экран onboarding")

    @allure.step("Проверить третий экран onboarding")
    def should_see_third_screen(self):
        browser.element(("xpath", '//*[@text="Read in more than 300 languages"]')).should(be.visible)
        add_screenshot("Третий экран onboarding")

    @allure.step("Проверить четвертый экран onboarding")
    def should_see_fourth_screen(self):
        browser.element(("xpath", '//*[@text="Follow your curiosity"]')).should(be.visible)
        add_screenshot("Четвертый экран onboarding")

    @allure.step("Нажать Forward")
    def continue_click(self):
        browser.element(("accessibility id", "Forward")).click()
        add_screenshot("После нажатия Forward")

    @allure.step("Нажать Skip")
    def get_started(self):
        browser.element(("xpath", '//*[@text="Skip"]')).click()
        add_screenshot("После нажатия Skip")

    @allure.step("Пройти onboarding")
    def skip_onboarding(self):
        self.continue_click()
        self.continue_click()
        self.continue_click()
        self.get_started()
        return self

    @allure.step("Пройти onboarding, если он отображается")
    def skip_onboarding_if_present(self):
        if browser.element(("accessibility id", "Forward")).matching(be.visible):
            self.skip_onboarding()
        return self