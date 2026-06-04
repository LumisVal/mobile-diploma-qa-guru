import allure
from selene import browser, be


class SearchPage:

    @allure.step("Открыть поиск")
    def open_search(self):
        browser.element(
            ("xpath", "//*[contains(@text,'Search Wikipedia')]")
        ).click()

        return self

    @allure.step("Ввести запрос")
    def type_query(self, query):
        browser.element(
            ("id", "org.wikipedia.alpha:id/search_src_text")
        ).type(query)

        return self

    @allure.step("Проверить результаты")
    def should_have_results(self):
        browser.element(
            ("id", "org.wikipedia.alpha:id/page_list_item_title")
        ).should(be.visible)

        return self