import allure
from selene import browser, be
from selene.core.exceptions import TimeoutException

class SearchPage:

    @allure.step("Открыть поиск")
    def open_search(self):
        browser.element(("accessibility id", "Search")).click()

        # после первого тапа выезжает панель "A Faster way to Search" (с анимацией) —
        # ждём её до 3 секунд и закрываем; если не появилась, идём дальше
        try:
            browser.element(("accessibility id", "Close")).with_(timeout=3).click()
        except TimeoutException:
            pass

        # второй тап по вкладке открывает поле ввода сразу
        browser.element(("accessibility id", "Search")).click()
        return self

    @allure.step("Ввести запрос: {query}")
    def type_query(self, query):
        browser.element(("id", "org.wikipedia.alpha:id/search_src_text")).type(query)
        return self

    @allure.step("Проверить, что в результатах есть: {title}")
    def should_have_result(self, title):
        browser.element(("xpath", f'//*[@text="{title}"]')).should(be.visible)
        return self

    @allure.step("Открыть результат: {title}")
    def open_result(self, title):
        browser.element(("xpath", f'//*[@text="{title}"]')).click()
        return self