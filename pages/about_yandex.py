from pages.base_page import BasePage
import allure


class AboutYandexPage(BasePage):
    """Страница Дзена (проверка редиректа)"""
    
    @allure.step("Проверить, что открылась страница Дзена")
    def is_dzen_page_opened(self):
        """Проверить, что открылась страница Дзена"""
        self.wait_for_url_contains("dzen.ru")
        return "dzen.ru" in self.get_current_url()