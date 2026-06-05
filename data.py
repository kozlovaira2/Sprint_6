class TestData:
    """Тестовые данные"""
    
    # Данные для заказов (параметризация)
    ORDER_DATA = [
        {
            "name": "Иван",
            "surname": "Петров",
            "address": "ул. Ленина, 10",
            "metro": "Сокольники",
            "phone": "+79001234567",
            "date": "25.12.2024",
            "rental_period": "сутки",
            "color": "black",
            "comment": "Позвонить за час"
        },
        {
            "name": "Анна",
            "surname": "Сидорова",
            "address": "пр. Мира, 5",
            "metro": "Комсомольская",
            "phone": "+79109876543",
            "date": "30.12.2024",
            "rental_period": "трое суток",
            "color": "grey",
            "comment": "Домофон не работает"
        }
    ]
    
    # Ожидаемые URL
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru"
    
    # Текст успешного заказа
    SUCCESS_ORDER_TEXT = "Заказ оформлен"