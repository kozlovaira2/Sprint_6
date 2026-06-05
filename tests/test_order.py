import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData


class TestOrder:
    """Тесты для позитивного сценария заказа самоката"""
    
    @allure.story("Оформление заказа")
    @allure.title("Позитивный сценарий заказа через {button_position} кнопку")
    @pytest.mark.parametrize("button_position", ["top", "bottom"])
    @pytest.mark.parametrize("order_data", TestData.ORDER_DATA)
    def test_positive_order_flow(self, driver, button_position, order_data):
        """Проверка полного флоу заказа самоката"""
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        with allure.step(f"Нажать кнопку заказа ({button_position})"):
            main_page.click_order_button(button_position)
        
        order_page = OrderPage(driver)
        
        with allure.step("Заполнить первую форму заказа"):
            order_page.fill_order_form_first(order_data)
        
        with allure.step("Заполнить вторую форму заказа"):
            order_page.fill_order_form_second(order_data)
        
        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверить, что заказ успешно создан"):
            assert order_page.is_order_successful(), "Сообщение об успешном заказе не появилось"