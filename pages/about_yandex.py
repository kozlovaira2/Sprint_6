from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class AboutYandexPage(BasePage):
    """Страница Дзена (проверка редиректа)"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Проверить, что открылась страница Дзена")
    def is_dzen_page_opened(self):
        """Проверить, что открылась страница Дзена"""
        self.wait.until(lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url)
        return "dzen.ru" in self.driver.current_url or "yandex.ru" in self.driver.current_url