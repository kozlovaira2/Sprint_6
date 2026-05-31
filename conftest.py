import pytest
from selenium import webdriver
import allure


@pytest.fixture(params=["firefox"], scope="function")
def driver(request):
    """Фикстура для создания драйвера Firefox"""
    browser_name = request.param
    
    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(10)
    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")
    
    driver.get("https://qa-scooter.praktikum-services.ru")
    yield driver
    driver.quit()


@pytest.fixture
def base_url():
    """Базовый URL сервиса"""
    return "https://qa-scooter.praktikum-services.ru"