def total_salary(path):
    try:
        total = 0
        count = 0

        # Відкриваємо файл за допомогою контекстного менеджера
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Розділяємо рядок на ім'я та зарплату
                    name, salary = line.strip().split(',')

                    # Перевіряємо, чи зарплата є числом
                    if not salary.isdigit():
                        raise ValueError(f"Невірний формат зарплати для {name}: {salary}")

                    total += int(salary)
                    count += 1
                except ValueError as ve:
                    print(f"Помилка в рядку: {line.strip()} - {ve}")

        # Розраховуємо середню зарплату
        average = total / count if count > 0 else 0

        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return None, None

# Приклад використання
path_to_file = 'salaries.txt'
total, average = total_salary(path_to_file)
if total is not None:
    print(f"Загальна сума зарплат: {total}, Середня зарплата: {average}")
