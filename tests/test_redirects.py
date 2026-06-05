import allure
from pages.main_page import MainPage
from pages.about_yandex import AboutYandexPage
from utils.urls import Urls


@allure.feature("Редиректы")
class TestRedirects:
    
    @allure.story("Логотип Самоката")
    @allure.title("Проверка редиректа на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        # Переходим на страницу заказа
        driver.get(Urls.ORDER_PAGE)
        
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Дождаться загрузки главной страницы"):
            main_page.wait_for_url(Urls.BASE_URL)
        
        with allure.step("Проверить, что открылась главная страница"):
            assert main_page.get_current_url() == Urls.BASE_URL.rstrip('/'), \
                f"Ожидался {Urls.BASE_URL}, получен {main_page.get_current_url()}"
    
    @allure.story("Логотип Яндекса")
    @allure.title("Проверка редиректа на Дзен при клике на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключиться на новое окно"):
            main_page.switch_to_new_window()
        
        with allure.step("Проверить, что открылась страница Дзена"):
            about_page = AboutYandexPage(driver)
            assert about_page.is_dzen_page_opened(), "Не удалось перейти на Дзен"