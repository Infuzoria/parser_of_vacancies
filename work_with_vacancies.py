from utils import exchange


class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, number: str, name: str, link: str, salary_from=None, salary_to=None, currency=None):
        """Конструктор класса"""

        self.number = int(number)
        self.name = name
        self.link = link
        if salary_from and currency.upper() != "RUB" and currency.upper() != "RUR":
            self.salary_from = exchange(currency, salary_from)
        else:
            self.salary_from = salary_from
        if salary_to and currency.upper() != "RUB" and currency.upper() != "RUR":
            self.salary_to = exchange(currency, salary_to)
        else:
            self.salary_to = salary_to
        self.currency = "RUB"

    def __str__(self):
        """Вывод информации в пользовательском режиме"""

        if self.salary_from is None and self.salary_to is None:
            return f"\nНомер вакансии: {self.number}\nНазвание вакансии: {self.name}\nСсылка: {self.link}"
        else:
            return (f"\nНомер вакансии: {self.number}\nНазвание вакансии: {self.name}\nСсылка: {self.link}\nЗарплата"
                    f"\nот: {self.salary_from}\nдо: {self.salary_to}\nВалюта: {self.currency}")

    def __eq__(self, other):
        """Оператор сравнения == """
        # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
        if self.salary_to:
            first_salary = self.salary_to
        elif self.salary_from:
            first_salary = self.salary_from
        else:
            first_salary = 0

        if type(other) == Vacancy:
            # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
            if other.salary_to:
                second_salary = other.salary_to
            elif other.salary_from:
                second_salary = other.salary_from
            else:
                second_salary = 0
        elif type(other) == int:
            second_salary = other

        if first_salary == second_salary:
            return True
        return False

    def __ne__(self, other):
        """Оператор сравнения != """
        # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
        if self.salary_to:
            first_salary = self.salary_to
        elif self.salary_from:
            first_salary = self.salary_from
        else:
            first_salary = 0

        if type(other) == Vacancy:
            # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
            if other.salary_to:
                second_salary = other.salary_to
            elif other.salary_from:
                second_salary = other.salary_from
            else:
                second_salary = 0
        elif type(other) == int:
            second_salary = other

        if first_salary != second_salary:
            return True
        return False

    def __lt__(self, other):
        """Оператор сравнения < """
        # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
        if self.salary_to:
            first_salary = self.salary_to
        elif self.salary_from:
            first_salary = self.salary_from
        else:
            first_salary = 0

        if type(other) == Vacancy:
            # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
            if other.salary_to:
                second_salary = other.salary_to
            elif other.salary_from:
                second_salary = other.salary_from
            else:
                second_salary = 0
        elif type(other) == int:
            second_salary = other

        if first_salary < second_salary:
            return True
        return False

    def __le__(self, other):
        """Оператор сравнения <= """
        # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
        if self.salary_to:
            first_salary = self.salary_to
        elif self.salary_from:
            first_salary = self.salary_from
        else:
            first_salary = 0

        if type(other) == Vacancy:
            # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
            if other.salary_to:
                second_salary = other.salary_to
            elif other.salary_from:
                second_salary = other.salary_from
            else:
                second_salary = 0
        elif type(other) == int:
            second_salary = other

        if first_salary <= second_salary:
            return True
        return False

    def __gt__(self, other):
        """Оператор сравнения > """
        # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
        if self.salary_to:
            first_salary = self.salary_to
        elif self.salary_from:
            first_salary = self.salary_from
        else:
            first_salary = 0

        if type(other) == Vacancy:
            # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
            if other.salary_to:
                second_salary = other.salary_to
            elif other.salary_from:
                second_salary = other.salary_from
            else:
                second_salary = 0
        elif type(other) == int:
            second_salary = other

        if first_salary > second_salary:
            return True
        return False

    def __ge__(self, other):
        # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
        if self.salary_to:
            first_salary = self.salary_to
        elif self.salary_from:
            first_salary = self.salary_from
        else:
            first_salary = 0

        if type(other) == Vacancy:
            # Устанавливаем зарплату. Выбираем либо верхний, либо нижний порог
            if other.salary_to:
                second_salary = other.salary_to
            elif other.salary_from:
                second_salary = other.salary_from
            else:
                second_salary = 0
        elif type(other) == int:
            second_salary = other

        if first_salary >= second_salary:
            return True
        return False
