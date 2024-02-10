import csv

# Файл, в котором будут храниться данные справочника
PHONEBOOK_FILE = "phonebook.csv"

def load_phonebook():
    """
    Загружает данные справочника из файла.
    """
    phonebook = []
    try:
        with open(PHONEBOOK_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                phonebook.append(row)
    except FileNotFoundError:
        pass
    return phonebook

def save_phonebook(phonebook):
    """
    Сохраняет данные справочника в файл.
    """
    with open(PHONEBOOK_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(phonebook)

def display_contacts(phonebook, page, page_size=5):
    """
    Выводит на экран страницу контактов.
    """
    start = (page - 1) * page_size
    end = start + page_size
    for i, contact in enumerate(phonebook[start:end], start=start):
        print(f"{i + 1}. {contact}")

def add_contact(phonebook, contact):
    """
    Добавляет новый контакт в справочник.
    """
    phonebook.append(contact)
    save_phonebook(phonebook)
    print("Контакт успешно добавлен.")

def edit_contact(phonebook, index, new_contact):
    """
    Редактирует существующий контакт в справочнике.
    """
    if 0 < index <= len(phonebook):
        phonebook[index - 1] = new_contact
        save_phonebook(phonebook)
        print("Контакт успешно отредактирован.")
    else:
        print("Неверный индекс контакта.")

def search_contacts(phonebook, **kwargs):
    """
    Ищет контакты по заданным характеристикам.
    """
    results = []
    for contact in phonebook:
        if all(key in contact and contact[key] == value for key, value in kwargs.items()):
            results.append(contact)
    return results

def main():
    phonebook = load_phonebook()

    while True:
        print("\nМеню:")
        print("1. Вывод контактов")
        print("2. Добавление контакта")
        print("3. Редактирование контакта")
        print("4. Поиск контакта")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            page = int(input("Введите номер страницы: "))
            display_contacts(phonebook, page)
        elif choice == "2":
            new_contact = input("Введите новый контакт в формате Фамилия,Имя,Отчество,Организация,Рабочий телефон,Личный телефон: ").split(",")
            add_contact(phonebook, new_contact)
        elif choice == "3":
            index = int(input("Введите номер контакта для редактирования: "))
            new_contact = input("Введите новые данные контакта в формате Фамилия,Имя,Отчество,Организация,Рабочий телефон,Личный телефон: ").split(",")
            edit_contact(phonebook, index, new_contact)
        elif choice == "4":
            search_criteria = input("Введите характеристики для поиска в формате ключ=значение через запятую: ").split(",")
            search_params = {}
            for criteria in search_criteria:
                key, value = criteria.split("=")
                search_params[key.strip()] = value.strip()
            results = search_contacts(phonebook, **search_params)
            print("Результаты поиска:")
            for result in results:
                print(result)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":

    main()
