def get_cats_info(path):
    cats_info = []

    try:
        # Відкриваємо файл за допомогою контекстного менеджера
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Розділяємо рядок на ідентифікатор, ім'я та вік
                    cat_id, name, age = line.strip().split(',')

                    # Перевіряємо, чи вік є числом
                    if not age.isdigit():
                        raise ValueError(f"Невірний формат віку для кота {name}: {age}")

                    # Додаємо інформацію про кота до списку
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": int(age)
                    })

                except ValueError as ve:
                    print(f"Помилка в рядку: {line.strip()} - {ve}")

        return cats_info

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None

# Приклад використання
path_to_file = 'cats.txt'
cats_info = get_cats_info(path_to_file)
if cats_info is not None:
    print(cats_info)
