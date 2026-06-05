from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    """Базовый класс для всех Page Object"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        """Найти элемент"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        """Кликнуть по элементу с предварительным скроллом"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Ввести текст в поле")
    def send_keys(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text
    
    @allure.step("Проскроллить до элемента")
    def scroll_to_element(self, locator):
        """Проскроллить до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self):
        """Дождаться полной загрузки страницы"""
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    
    @allure.step("Дождаться URL")
    def wait_for_url(self, expected_url):
        """Дождаться нужного URL"""
        self.wait.until(lambda d: d.current_url.rstrip('/') == expected_url.rstrip('/'))
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url.rstrip('/')
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        """Переключиться на новое окно"""
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    @allure.step("Проверить, что URL содержит текст")
    def wait_for_url_contains(self, text):
        """Дождаться, что URL содержит указанный текст"""
        self.wait.until(lambda d: text in d.current_url)