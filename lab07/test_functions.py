from functions import average, select_numbers, normalize_text, sum_digits

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
assert select_numbers([-5, 0, 2, 5], 2) == [0, 2]
assert select_numbers([], 2) == []
assert select_numbers([-1, 0, 1, 2, 3], 2) == [0, 1, 2]
assert select_numbers([1, 1, 1, 1], 2) == [1, 1, 1, 1]
original_list = [-5, 0, 2, 5]
copy_list = original_list.copy()
select_numbers(original_list, 2)
assert original_list == copy_list
print("Базовые проверки пройдены")
