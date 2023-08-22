class ParsingError(Exception):
    """Класс-исключение для запросов"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Ошибка запроса'

    def __str__(self):
        return self.message
