data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]


def calculate_structure_sum(data_structure, summ=[0]):
    if not data_structure:
        return 0
    if isinstance(data_structure, int):
        summ[0] = summ[0] + data_structure
        return data_structure
    if isinstance(data_structure, str):
        return calculate_structure_sum(len(data_structure), summ)
    if isinstance(data_structure, dict):
        data = [*data_structure.keys(), *data_structure.values()]
        return calculate_structure_sum(data, summ)
    if (
        isinstance(data_structure, list)
        or isinstance(data_structure, tuple)
        or isinstance(data_structure, set)
    ):
        for i in data_structure:
            calculate_structure_sum(i, summ)
        return summ[0]


result = calculate_structure_sum(data_structure)
print(result)
assert result == 99
