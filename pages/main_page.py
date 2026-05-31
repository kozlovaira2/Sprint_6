from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure
import time


class MainPage(BasePage):
    """Главная страница"""
    
    # Локаторы
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header')]//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header')]//img[@alt='Yandex']")
    
    # Вопросы в FAQ
    QUESTION_1 = (By.ID, "accordion__heading-0")
    QUESTION_2 = (By.ID, "accordion__heading-1")
    QUESTION_3 = (By.ID, "accordion__heading-2")
    QUESTION_4 = (By.ID, "accordion__heading-3")
    QUESTION_5 = (By.ID, "accordion__heading-4")
    QUESTION_6 = (By.ID, "accordion__heading-5")
    QUESTION_7 = (By.ID, "accordion__heading-6")
    QUESTION_8 = (By.ID, "accordion__heading-7")
    
    # Ответы в FAQ
    ANSWER_1 = (By.ID, "accordion__panel-0")
    ANSWER_2 = (By.ID, "accordion__panel-1")
    ANSWER_3 = (By.ID, "accordion__panel-2")
    ANSWER_4 = (By.ID, "accordion__panel-3")
    ANSWER_5 = (By.ID, "accordion__panel-4")
    ANSWER_6 = (By.ID, "accordion__panel-5")
    ANSWER_7 = (By.ID, "accordion__panel-6")
    ANSWER_8 = (By.ID, "accordion__panel-7")
    
    # Ожидаемые тексты ответов
    EXPECTED_ANSWERS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Принять куки")
    def accept_cookies(self):
        """Принять куки с ожиданием"""
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable(self.COOKIE_BUTTON)
            )
            cookie_button.click()
            self.wait.until(EC.invisibility_of_element_located(self.COOKIE_BUTTON))
        except:
            pass
    
    @allure.step("Нажать кнопку заказа")
    def click_order_button(self, button_position="top"):
        """Нажать кнопку заказа"""
        if button_position == "top":
            self.click_element(self.ORDER_BUTTON_TOP)
        else:
            self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
            self.click_element(self.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Кликнуть на вопрос {question_index}")
    def click_question(self, question_index):
        """Кликнуть на вопрос по индексу через JavaScript"""
        questions = [
            self.QUESTION_1, self.QUESTION_2, self.QUESTION_3, self.QUESTION_4,
            self.QUESTION_5, self.QUESTION_6, self.QUESTION_7, self.QUESTION_8
        ]
        
        element = self.wait.until(EC.presence_of_element_located(questions[question_index]))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)
        
        answers = [
            self.ANSWER_1, self.ANSWER_2, self.ANSWER_3, self.ANSWER_4,
            self.ANSWER_5, self.ANSWER_6, self.ANSWER_7, self.ANSWER_8
        ]
        self.wait.until(EC.visibility_of_element_located(answers[question_index]))
    
    @allure.step("Получить текст ответа на вопрос {question_index}")
    def get_answer_text(self, question_index):
        """Получить текст ответа по индексу вопроса"""
        answers = [
            self.ANSWER_1, self.ANSWER_2, self.ANSWER_3, self.ANSWER_4,
            self.ANSWER_5, self.ANSWER_6, self.ANSWER_7, self.ANSWER_8
        ]
        element = self.wait.until(EC.visibility_of_element_located(answers[question_index]))
        return element.text
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        """Кликнуть на логотип Самоката"""
        self.click_element(self.SCOOTER_LOGO)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        """Кликнуть на логотип Яндекса"""
        self.click_element(self.YANDEX_LOGO)