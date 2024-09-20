import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація Colorama для кольорового виведення
init(autoreset=True)

def visualize_directory_structure(path):
    try:
        # Створюємо об'єкт Path
        dir_path = Path(path)

        # Перевіряємо, чи шлях є директорією
        if not dir_path.is_dir():
            print(f"Шлях {path} не є директорією.")
            return

        # Функція для рекурсивного виведення директорій і файлів
        for item in dir_path.rglob('*'):
            if item.is_dir():
                print(Fore.BLUE + f"Директорія: {item}")
            else:
                print(Fore.GREEN + f"Файл: {item}")

    except FileNotFoundError:
        print(f"Директорію за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

# Основний блок для отримання шляху до директорії
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Вкажіть шлях до директорії як аргумент.")
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)
