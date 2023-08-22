from abc import ABC, abstractmethod
from exceptions import ParsingError
import requests

class Server(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunter(Server):
    """Класс для работы с платформой HeadHunter"""

    url = "https://api.hh.ru/vacancies/"

    def __init__(self, keyword: str):
        """Конструктор класса"""

        self.params = {
            "count": 100,
            "page":  None,
            "keyword": keyword,
            "archive": False
        }
        self.vacancies = []

    def get_request(self):
        """Метод осуществляет запрос к сайту"""

        response = requests.get(self.url, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий. Статус: {response.status_code}")
        return response.json()

    def get_vacancies(self, page_count=2):
        """Метод осуществляет выборку вакансий"""

        self.vacancies = []
        for page in range(page_count):
            page_vacancies = []
            self.params["page"] = page

            try:
                page_vacancies = self.get_request()
            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f"Добавлено вакансий: {len(page_vacancies)}")
            if len(page_vacancies) == 0:
                break


hh_api = HeadHunter("Python")
print(hh_api.get_request())
