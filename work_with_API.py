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
            "found": 1,
            "per_page": 100,
            "pages": 2,
            "page": 0,
            "items": [{}]
        }
        self.vacancies = []
        self.keyword = keyword
        self.headers = {
            "User-Agent: MyApp/1.0 (alexa.sazhaeva@gmail.com)"
        }

    def get_request(self):
        """Метод осуществляет запрос к сайту"""

        response = requests.get(self.url, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий. Статус: {response.status_code}")
        return response.json()["items"]

    def get_vacancies(self, page_count=10):
        """Метод осуществляет выборку вакансий"""

        # Символы, которые необходимо удалить из назвения вакансии
        symbols = ".,()\'\":!;?-"
        self.vacancies = []
        self.params["pages"] = page_count
        for page in range(page_count):
            page_vacancies = []
            temp_vacancies = []
            self.params["page"] = page

            try:
                temp_vacancies = self.get_request()
                for vacancy in temp_vacancies:

                    # Проверяем, что вакансия не в архиве
                    if vacancy["archived"] == False:

                        # Удаляем ненужные символы из названия вакансии
                        name = vacancy["name"].lower()
                        if vacancy["snippet"]["requirement"] is None:
                            description = " "
                        else:
                            description = vacancy["snippet"]["requirement"].lower()
                        for symbol in symbols:
                            name = name.replace(symbol, " ")
                            description = description.replace(symbol, " ")
                        name.split()
                        description.split()


                        # Ищем ключевое слово
                        if self.keyword in name or self.keyword in description:
                            page_vacancies.append(vacancy)

            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                for vacancy in page_vacancies:
                    print(f"Добавлена вакансия: {vacancy['name']}")
            if len(temp_vacancies) == 0:
                print(f"Всего найдено вакансий: {len(self.vacancies)}")
                break
        print(f"Всего найдено вакансий: {len(self.vacancies)}")


class SuperJob(Server):
    """Класс для работы с платформой SuperJob"""

    url = "https://api.superjob.ru/2.0/vacancies/"

    def __init__(self, keyword: str):
        """Конструктор класса"""

        self.params = {
            "count": 10,
            "page": None,
            "keyword": keyword,
            "archive": False
        }
        self.vacancies = []
        self.headers = {
            "X-Api-App-Id": "v3.r.137735273.3c1eb613781d2ccaac4b807f884716c3b44541cf.344b00866b94b08ff81bf8f81eb5422c3e181334"
        }

    def get_request(self):
        """Метод осуществляет запрос к сайту"""

        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий. Статус: {response.status_code}")
        return response.json()["objects"]

    def get_vacancies(self, page_count=10):
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
                for vacancy in page_vacancies:
                    print(f"Добавлена вакансия: {vacancy['profession']}")
            if len(page_vacancies) == 0:
                print(f"Всего найдено вакансий: {len(self.vacancies)}")
                break
        print(f"Всего найдено вакансий: {len(self.vacancies)}")


class Vacancy:
    """Класс для работы с вакансиями"""

    def __int__(self, name: str, link: str, salary: int, description: str, area: str):
        """Конструктор класса"""

        self.name = name
        self.link = link
        self.salary = salary
        self.description = description
        self.area = area

    def __eq__(self, other):
        """Оператор сравнения == """
        if self.salary == other.salary:
            return True
        return False

    def __ne__(self, other):
        """Оператор сравнения != """
        if self.salary != other.salary:
            return True
        return False

    def __lt__(self, other):
        """Оператор сравнения < """
        if self.salary < other.salary:
            return True
        return False

    def __le__(self, other):
        """Оператор сравнения <= """
        if self.salary <= other.salary:
            return True
        return False

    def __gt__(self, other):
        """Оператор сравнения > """
        if self.salary > other.salary:
            return True
        return False

    def __ge__(self, other):
        """Оператор сравнения >= """
        if self.salary >= other.salary:
            return True
        return False

