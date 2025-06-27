import json

def read_cook_book_json(filename):
    """
    Считывает кулинарную книгу из файла JSON и возвращает ее в виде словаря.

    Аргументы:
        имя файла (str): Путь к файлу JSON, содержащему данные кулинарной книги.

    Возвращается:
        dict: словарь, представляющий кулинарную книгу. Возвращает пустой словарь
              если файл не найден или если во время синтаксического анализа JSON произошла ошибка
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            cook_book = json.load(f)  # Загружает данные JSON непосредственно в словарь
            return cook_book
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}



filename = 'cook_book.json'


cook_book_data = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ]
}

try:
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cook_book_data, f, indent=4, ensure_ascii=False)  # Сохраниение в JSON
except Exception as e:
    print(f"Error creating test file: {e}")

cook_book = read_cook_book_json(filename)

if cook_book:
    print("Cookbook:")
    print(json.dumps(cook_book, indent=4, ensure_ascii=False))
else:
    print("No cookbook found.")


import json

def read_cook_book_json(filename):
    """Reads a cook book from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{filename}'.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """Calculates the required ingredients based on a list of dishes."""
    shop_list = {}
    for dish_name in dishes:
        if dish_name not in cook_book:
            print(f"Warning: Dish '{dish_name}' not found.")
            continue
        for ing in cook_book[dish_name]:
            name = ing['ingredient_name']
            qty = ing['quantity'] * person_count
            measure = ing['measure']
            if name in shop_list:
                shop_list[name]['quantity'] += qty
            else:
                shop_list[name] = {'quantity': qty, 'measure': measure}
    return shop_list


cook_book = read_cook_book_json("cook_book.json")


try:
    person_count = int(input("Введите количество персон: "))
except ValueError:
    print("Invalid input. Using 1 person.")
    person_count = 1


dish_choices = {
    1: ['Запеченный картофель'],
    2: ['Омлет'],
    3: ['Утка по-пекински']
}

try:
    dish_choice = int(input("Введите номер позиции (1, 2, 3): "))
    dishes_to_cook = dish_choices.get(dish_choice, [])
    if not dishes_to_cook:
        print("Invalid dish choice. No dishes will be cooked.")
except ValueError:
    print("Invalid input. No dishes will be cooked.")
    dishes_to_cook = []


shopping_list = get_shop_list_by_dishes(dishes_to_cook,person_count,cook_book)

if shopping_list:
    print("Shopping List:")
    for ingredient, details in shopping_list.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")
else:
    print("No ingredients needed.")

