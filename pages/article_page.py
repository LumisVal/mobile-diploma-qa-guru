import allure
from selene import browser, be


class ArticlePage:

    @allure.step("Проверить заголовок статьи: {title}")
    def should_have_title(self, title):
        browser.element(("xpath", f'//android.widget.TextView[@text="{title}"]')).should(be.visible)
        return self