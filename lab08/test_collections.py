from collections_lab import (
    word_counts, alphabet_sort, common_topics, all_topics,
    totals_by_category, titles_in_category, get_sorted,
)

if __name__ == "__main__":
    # ==========================================
    # ЗАДАНИЕ 1. Частоты слов
    # ==========================================
    assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
    assert word_counts("!!!") == {}
    assert word_counts("") == {}

    # Демонстрация вывода по алфавиту
    print("--- Задание 1: Частоты слов ---")
    counts = word_counts("Python, python! SQL, git, git")
    alphabet_sort(counts)
    print()

    # ==========================================
    # ЗАДАНИЕ 2. Учебные интересы
    # ==========================================
    assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
    assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]
    assert common_topics([], ["sql", "git"]) == []
    assert all_topics([], ["sql", "git"]) == ["git", "sql"]

    # ==========================================
    # ЗАДАНИЕ 3. Запись и пара
    # ==========================================
    print("--- Задание 3: Запись и пара ---")
    table = {'title': 'Python', 'hours': 10}
    table['hours'] = 13
    table['completed'] = False
    data = (table['title'], table['hours'])
    title, hours = data
    print(f"title = {title}")
    print(f"hours = {hours}")
    print()

    # ==========================================
    # ИНДИВИДУАЛЬНЫЙ ВАРИАНТ №9
    # ==========================================
    print("--- Индивидуальный вариант №9 ---")

    # 5 записей, 3 категории
    records = [
        {"title": "Списки", "category": "теория", "amount": 10},
        {"title": "Циклы", "category": "теория", "amount": 15},
        {"title": "FizzBuzz", "category": "практика", "amount": 20},
        {"title": "Калькулятор", "category": "практика", "amount": 25},
        {"title": "Итоговый тест", "category": "контроль", "amount": 30},
    ]

    snapshot = [r.copy() for r in records]

    # Проверки
    assert totals_by_category(records) == {"теория": 25, "практика": 45, "контроль": 30}
    assert totals_by_category([]) == {}
    assert titles_in_category(records, "теория") == ["Списки", "Циклы"]
    assert titles_in_category(records, "нет") == []
    assert titles_in_category([], "теория") == []
    assert records == snapshot  # Проверка, что функции не изменили входные данные

    # Проверка дополнительного задания
    expected_sorted = [("практика", 45), ("контроль", 30), ("теория", 25)]
    assert get_sorted(records) == expected_sorted
    print("\nДополнительное задание (сортировка) работает верно.")
    
    # Вывод сводки по категориям в алфавитном порядке
    totals = totals_by_category(records)
    print("Сводка по категориям (по алфавиту):")
    for cat in sorted(totals):
        print(f"  {cat}: {totals[cat]}")

    # Поиск категории, введённой пользователем
    user_category = input("\nВведите категорию для поиска: ").strip().lower()
    found_titles = titles_in_category(records, user_category)

    if found_titles:
        print(f"Найдены задания в категории '{user_category}': {found_titles}")
    else:
        print(f"В категории '{user_category}' ничего не найдено ([]).")

    print("\nВсе проверки пройдены.")