def read_matrix(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    if not lines:
        raise ValueError("Файл пуст")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось 2 значения (строки и столбцы)")

    try:
        cnt_strings = int(header[0])
        cnt_columns = int(header[1])
    except ValueError:
        raise ValueError("Строка 1: заголовок должен состоять из целых чисел")

    if cnt_strings <= 0 or cnt_columns <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть больше нуля")

    data_lines = lines[1:]

    if len(data_lines) != cnt_strings:
        raise ValueError(f"Ожидалось {cnt_strings} строк (сейчас - {len(data_lines)})")

    result = []
    for i, line in enumerate(data_lines, 2):
        parts = line.split()
        if len(parts) != cnt_columns:
            raise ValueError(f"Строка {i}: ожидалось {cnt_columns} чисел (сейчас - {len(parts)})")
        try:
            row = [int(x) for x in parts]
        except ValueError:
            raise ValueError(f"Строка {i}: содержится нечисловая ячейка")
        result.append(row)

    return result


def selected_sum(matrix):
    if not matrix:
        return 0
    return sum(matrix[-1])