import allure
import pytest
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature("FAQ")
class TestFAQ:
    """Тесты для раздела «Вопросы о важном»"""
    
    @allure.story("Проверка ответов на вопросы")
    @allure.title("Проверка, что текст ответа соответствует ожидаемому")
    @pytest.mark.parametrize("question_index", range(8))
    def test_faq_answers(self, driver, question_index):
        main_page = MainPage(driver)
        
        # Ждём загрузки страницы
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        
        main_page.accept_cookies()
        
        with allure.step(f"Кликнуть на вопрос {question_index + 1}"):
            main_page.click_question(question_index)
        
        with allure.step(f"Получить текст ответа на вопрос {question_index + 1}"):
            actual_answer = main_page.get_answer_text(question_index)
        
        with allure.step("Сравнить с ожидаемым текстом"):
            expected_answer = main_page.EXPECTED_ANSWERS[question_index]
            assert actual_answer == expected_answer, \
                f"Ответ на вопрос {question_index + 1} не совпадает.\nОжидалось: {expected_answer}\nПолучено: {actual_answer}"