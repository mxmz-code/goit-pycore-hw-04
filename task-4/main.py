def parse_input(user_input):
    # Розбираємо введену команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Помилка: необхідно вказати ім'я та номер телефону у форматі: add [ім'я] [номер телефону]."
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} додано."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Помилка: необхідно вказати ім'я та новий номер телефону у форматі: change [ім'я] [новий номер телефону]."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Номер для контакту {name} оновлено."
    else:
        return f"Контакт {name} не знайдено."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Помилка: необхідно вказати ім'я у форматі: phone [ім'я]."
    name = args[0]
    if name in contacts:
        return f"Номер телефону для {name}: {contacts[name]}"
    else:
        return f"Контакт {name} не знайдено."

def show_all(contacts):
    if not contacts:
        return "Контакти відсутні."
    result = "Всі контакти:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def print_help():
    return """
Доступні команди:
1. hello - бот привітає вас
2. add [ім'я] [номер телефону] - додати новий контакт
3. change [ім'я] [новий номер телефону] - змінити номер телефону існуючого контакту
4. phone [ім'я] - показати номер телефону для вказаного імені
5. all - показати всі збережені контакти
6. help - вивести список доступних команд
7. close або exit - завершити роботу бота
"""

def main():
    contacts = {}  # Словник для зберігання контактів
    print("Вітаю! Це бот-помічник. Введіть команду.")
    print(print_help())  # Показуємо підказки при старті

    while True:
        user_input = input("Введіть команду: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Чим можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(print_help())
        else:
            print("Невірна команда. Спробуйте ще раз або введіть 'help' для списку доступних команд.")

if __name__ == "__main__":
    main()
