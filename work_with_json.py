import json
from work_with_vacancies import Vacancy
from abc import ABC, abstractmethod
import os


class Saver(ABC):
    """Абстрактный класс для сохранения данных в разных форматах"""

    @abstractmethod
    def clear_file(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def show_file(self):
        pass


class JSONSaver:
    """Класс для сохранения данных в формате json"""

    @staticmethod
    def add_vacancy(vacancy: Vacancy):
        """Сохраняет данные в json файл"""

        # Создаем словарь с данными о вакансии
        data = {"number": vacancy.number, "profession": vacancy.name, "link": vacancy.link, "salary_from": vacancy.salary_from,
                "salary_to": vacancy.salary_to, "currency": vacancy.currency}

        # Открываем файл на запись
        with open("vacancies.json", 'a', encoding="utf-8") as f:
            if os.stat("vacancies.json").st_size == 0:
                json.dump([data], f, ensure_ascii=False)
            else:
                with open("vacancies.json", encoding="utf-8") as json_file:
                    data_list = json.load(json_file)
                data_list.append(data)
                with open("vacancies.json", "w", encoding="utf-8") as json_file:
                    json.dump(data_list, json_file, ensure_ascii=False)

    @staticmethod
    def clear_file():
        with open("vacancies.json", "w") as f:
            pass

    @staticmethod
    def get_vacancies_by_salary(range_from: int, range_to: int):
        """Выводит на экран вакансии с зарплатой в заданном диапазоне"""

        count_vacancies = 0

        if os.stat("vacancies.json").st_size == 0:
            print("Файл пустой")
        else:
            with open("vacancies.json", encoding="utf-8") as json_file:
                data_list = json.load(json_file)

            for row in data_list:
                vacancy = Vacancy(row["number"], row["profession"], row["link"], row["salary_from"],
                                  row["salary_to"], row["currency"])
                if range_from < vacancy < range_to:
                    count_vacancies += 1
                    print(vacancy)

            if count_vacancies == 0:
                print("Не найдено подходящих вакансий")

    @staticmethod
    def delete_vacancy(number: int):
        """Функция удаляет вакансию из файла по номеру вакансии"""

        if os.stat("vacancies.json").st_size == 0:
            print("Файл пустой")
        else:
            with open("vacancies.json", encoding="utf-8") as json_file:
                temp_list = json.load(json_file)
            data_list = []

            # Удаляем вакансию
            count_vacancies = 0
            for row in temp_list:
                if row["number"] != number:
                    count_vacancies += 1
                    data_list.append(row)

            if count_vacancies == len(temp_list):
                print("Такой вакансии нет в файле. Скорее всего, вы уже удалили её.")

            with open("vacancies.json", "w", encoding="utf-8") as json_file:
                json.dump(data_list, json_file, ensure_ascii=False)

    @staticmethod
    def show_file():
        """Вывод на экран содержимого файла"""
        if os.stat("vacancies.json").st_size == 0:
            print("Файл пустой")
        else:
            with open("vacancies.json", encoding="utf-8") as json_file:
                data_list = json.load(json_file)

            for row in data_list:
                vacancy = Vacancy(row["number"], row["profession"], row["link"], row["salary_from"],
                                  row["salary_to"], row["currency"])
                print(vacancy)
