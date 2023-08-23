from work_with_API import HeadHunter, SuperJob

def user_interaction():
    print("""Программа предназначена для поиска вакансий. 
    Для того, чтобы начать работу, прочтите правила использования и выберите нужный пункт.
    
    Напишите 1 - чтобы осуществить подбор вакансий по ключевому слову.
    Напишите 2 - чтобы вывести на экран содержимое json файла.
    Напишите 3 - чтобы удалить определенную вакансию из файла.
    Напишите 4 - чтобы отсортировать вакансии по зарплате.
    Напишите 5 - чтобы очистить json файл.
    
    Введите stop для того, чтобы завершить работу программы.""")

    # Создаем объекты для работы с платформами
    hh = HeadHunter()
    sj = SuperJob()

    # Очищаем файл json
    hh.json_saver.clear_file()

    while True:
        user_input = input("\nВведите цифру или 'stop'\n")

        if user_input.lower() == "stop":
            break
        elif user_input == '1':

            keyword = input("Введите ключевое слово: ")
            if keyword and keyword != " ":
                for platform in [hh, sj]:
                    platform.get_vacancies(keyword)
            else:
                print("Ключевое слово введено неверно, попробуйте ещё раз.")

        elif user_input == "2":
            hh.json_saver.show_file()
        elif user_input == "3":
            try:
                number = int(input("Введите номер вакансии, чтобы удалить её из файла: "))
                hh.json_saver.delete_vacancy(number)
            except ValueError as error:
                print("Номер введен некорректно, попробуйте ещё раз.")
        elif user_input == "4":
            # Определяем нижний порог
            try:
                range_from = int(input("Введите нижний порог: "))
            except ValueError as error:
                range_from = 0

            # Определяем нижний порог
            try:
                range_to = int(input("Введите верхний порог: "))
            except ValueError as error:
                range_to = 0

            if 0 <= range_from < range_to:
                hh.json_saver.get_vacancies_by_salary(range_from, range_to)
            else:
                print("Данные введены некорректно.")
        elif user_input == "5":
            hh.json_saver.clear_file()
            print("Файл очищен")


if __name__ == '__main__':
    user_interaction()
