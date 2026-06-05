from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    """Страница заказа"""
    
    # Локаторы первой формы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локаторы второй формы заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK = (By.XPATH, "//label[text()='чёрный жемчуг']")
    COLOR_GREY = (By.XPATH, "//label[text()='серая безысходность']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    
    # Локаторы календаря
    CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker')]")
    CALENDAR_DAY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
    
    # Локаторы модального окна
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[contains(text(), 'Заказ оформлен')]")
    
    # Варианты срока аренды
    RENTAL_OPTIONS = {
        "сутки": (By.XPATH, "//div[text()='сутки']"),
        "двое суток": (By.XPATH, "//div[text()='двое суток']"),
        "трое суток": (By.XPATH, "//div[text()='трое суток']"),
        "четверо суток": (By.XPATH, "//div[text()='четверо суток']"),
        "пятеро суток": (By.XPATH, "//div[text()='пятеро суток']"),
        "шестеро суток": (By.XPATH, "//div[text()='шестеро суток']"),
        "семеро суток": (By.XPATH, "//div[text()='семеро суток']")
    }
    
    @allure.step("Заполнить первую форму заказа")
    def fill_order_form_first(self, order_data):
        """Заполнить первую форму заказа"""
        self.send_keys(self.NAME_INPUT, order_data["name"])
        self.send_keys(self.SURNAME_INPUT, order_data["surname"])
        self.send_keys(self.ADDRESS_INPUT, order_data["address"])
        self.send_keys(self.METRO_STATION, order_data["metro"])
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{order_data['metro']}']")))
        self.click_element((By.XPATH, f"//div[text()='{order_data['metro']}']"))
        self.send_keys(self.PHONE_INPUT, order_data["phone"])
        self.click_element(self.NEXT_BUTTON)
    
    @allure.step("Заполнить вторую форму заказа")
    def fill_order_form_second(self, order_data):
        """Заполнить вторую форму заказа"""
        # === ВЫБОР ДАТЫ ЧЕРЕЗ КАЛЕНДАРЬ ===
        date_field = self.find_element(self.DATE_INPUT)
        date_field.click()
        
        # Получаем число из даты (25.12.2024 -> 25)
        day = order_data["date"].split('.')[0]
        
        # Ждём появления календаря
        self.wait.until(EC.presence_of_element_located(self.CALENDAR))
        
        # Находим и кликаем на нужный день в календаре
        day_locator = (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        day_element = self.wait.until(EC.element_to_be_clickable(day_locator))
        day_element.click()
        
        # === СРОК АРЕНДЫ ===
        self.click_element(self.RENTAL_PERIOD)
        self.click_element(self.RENTAL_OPTIONS[order_data["rental_period"]])
        
        # === ЦВЕТ ===
        if order_data.get("color") == "black":
            self.click_element(self.COLOR_BLACK)
        elif order_data.get("color") == "grey":
            self.click_element(self.COLOR_GREY)
        
        # === КОММЕНТАРИЙ ===
        if order_data.get("comment"):
            self.send_keys(self.COMMENT_INPUT, order_data["comment"])
        
        # === КНОПКА ЗАКАЗАТЬ ===
        self.click_element(self.ORDER_BUTTON)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        """Подтвердить заказ в модальном окне"""
        self.click_element(self.CONFIRM_BUTTON)
    
    @allure.step("Проверить, что заказ успешно создан")
    def is_order_successful(self):
        """Проверить, что заказ успешно создан"""
        return self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE)) is not None