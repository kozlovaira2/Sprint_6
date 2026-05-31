import allure
from pages.main_page import MainPage
from pages.about_yandex import AboutYandexPage
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature("Редиректы")
class TestRedirects:
    """Тесты для проверки редиректов"""
    
    @allure.story("Логотип Самоката")
    @allure.title("Проверка редиректа на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_redirect(self, driver, base_url):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Дождаться загрузки главной страницы"):
            WebDriverWait(driver, 10).until(lambda d: d.current_url == base_url)
        
        with allure.step("Проверить, что открылась главная страница"):
            assert driver.current_url == base_url, f"Ожидался {base_url}, получен {driver.current_url}"
    
    @allure.story("Логотип Яндекса")
    @allure.title("Проверка редиректа на Дзен при клике на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключиться на новое окно"):
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            driver.switch_to.window(driver.window_handles[1])
        
        with allure.step("Проверить, что открылась страница Дзена"):
            about_page = AboutYandexPage(driver)
            assert about_page.is_dzen_page_opened(), "Не удалось перейти на Дзен"