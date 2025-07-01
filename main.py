import re

def read_cookbook_from_file(filename):
    """
    Считывает кулинарную книгу из файла и возвращает ее в виде словаря.

    Аргументы:
        имя файла (str): Имя файла, содержащего данные кулинарной книги.

    Возвращается:
        dict: словарь, представляющий кулинарную книгу. Возвращает пустой словарь
              если файл не найден или произошла ошибка.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            return read_cookbook_from_string(text)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def read_cookbook_from_string(text):
    """
    Построчное чтение книги.
    """
    cookbook = {}
    dish_name = None
    num_ingredients = None
    ingredients = []
    lines = text.splitlines()
    line_index = 0

    while line_index < len(lines):
        line = lines[line_index].strip()

        if not line:
            line_index += 1
            continue

        if dish_name is None:
            dish_name = line
            line_index += 1
            continue

        if num_ingredients is None:
            try:
                num_ingredients = int(line)
                line_index += 1
                continue
            except ValueError:
                print(f"Warning: Invalid number of ingredients: {line} for dish {dish_name}. Skipping dish.")
                dish_name = None
                num_ingredients = None
                ingredients = []
                line_index += 1
                continue

        parts = re.split(r' \| ', line)
        if len(parts) == 3:
            ingredient_name, quantity_str, measure = parts
            try:
                quantity = int(quantity_str)
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure.strip()
                })
            except ValueError:
                print(f"Warning: Invalid quantity for ingredient '{ingredient_name}' in dish '{dish_name}'. Skipping ingredient.")
        else:
            print(f"Warning: Invalid ingredient line: '{line}'. Skipping.")
        line_index += 1

        if num_ingredients is not None and len(ingredients) == num_ingredients:
            cookbook[dish_name] = ingredients
            dish_name = None
            num_ingredients = None
            ingredients = []

    return cookbook

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    """
    Счет весов с учетом количества гостей
    """
    shop_list = {}
    for dish_name in dishes:
        if dish_name not in cook_book:
            print(f"Warning: Dish '{dish_name}' not found in the cookbook.")
            continue

        for ingredient in cook_book[dish_name]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list



filename = "recipes.txt"

cook_book = read_cookbook_from_file(filename)

if not cook_book:
    print("Could not load cookbook.  Make sure recipes.txt exists and is properly formatted.")
    exit()

dishes_to_cook = ['Запеченный картофель', 'Омлет']
person_count = 2

shopping_list = get_shop_list_by_dishes(dishes_to_cook, person_count, cook_book)


if shopping_list: #вывод словаря
    print("{")
    for ingredient, details in shopping_list.items():
        print(f"  '{ingredient}': {details},")
    print("}")

else:
    print("No ingredients needed.")