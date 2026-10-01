import allure
from selene import browser, be


class ArticlePage:

    @allure.step("Проверить, что статья открыта")
    def should_be_opened(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/page_web_view")
        ).should(be.visible)

        return self
