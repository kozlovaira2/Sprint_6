import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


@allure.feature("Редиректы")
class TestRedirects:
    
    @allure.story("Логотип Самоката")
    @allure.title("Проверка редиректа на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_redirect(self, driver, base_url):
        # Переходим на страницу заказа
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Дождаться загрузки главной страницы"):
            # Ждём, когда URL станет главной страницей (с или без слеша)
            WebDriverWait(driver, 10).until(
                lambda d: d.current_url.rstrip('/') == base_url.rstrip('/')
            )
        
        with allure.step("Проверить, что открылась главная страница"):
            assert driver.current_url.rstrip('/') == base_url.rstrip('/'), \
                f"Ожидался {base_url}, получен {driver.current_url}"
    
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