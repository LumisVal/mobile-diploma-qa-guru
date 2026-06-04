import allure
from selene import browser, be, have

class MainPage:

    @allure.step("Закрыть всплывающее окно Wikipedia Games")
    def close_popup_if_present(self):

        close_buttons = browser.all(
            ("id", "org.wikipedia.alpha:id/closeButton")
        )

        if len(close_buttons) > 0:
            close_buttons.first.click()

        return self

    @allure.step("Открыть вкладку Explore")
    def open_explore(self):
        browser.element(
            ("xpath", "//*[@text='Explore']")
        ).click()

        return self

    @allure.step("Проверить вкладку Explore")
    def should_see_explore(self):
        browser.element(
            ("xpath", "//*[@text='Explore']")
        ).should(have.text("Explore"))

        return self

    @allure.step("Открыть вкладку More")
    def open_more(self):
        browser.element(
            ("xpath", "//*[@text='More']")
        ).click()

        return self

    @allure.step("Проверить вкладку More")
    def should_see_more(self):
        browser.element(
            ("xpath", "//*[@text='Settings']")
        ).should(be.visible)

        return self

    @allure.step("Открыть вкладку Saved")
    def open_saved(self):
        browser.element(
            ("xpath", "//*[@text='Saved']")
        ).click()

        return self

    @allure.step("Проверить вкладку Saved")
    def should_see_saved(self):
        browser.element(
            ("xpath", "//*[@text='Saved']")
        ).should(be.visible)

        return self

    @allure.step("Открыть вкладку Edits")
    def open_edits(self):
        browser.element(
            ("xpath", "//*[@text='Edits']")
        ).click()

        return self

    @allure.step("Проверить вкладку Edits")
    def should_see_edits(self):
        browser.element(
            ("xpath", "//*[@text='Edits']")
        ).should(be.visible)

        return self