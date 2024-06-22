data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]


def calculate_structure_sum(data_structure):
    if not data_structure:
        return 0
    if isinstance(data_structure, int):
        return data_structure
    if isinstance(data_structure, str):
        return calculate_structure_sum(len(data_structure))
    if isinstance(data_structure, dict):
        data = [*data_structure.keys(), *data_structure.values()]
        return calculate_structure_sum(data)
    if (
        isinstance(data_structure, list)
        or isinstance(data_structure, tuple)
        or isinstance(data_structure, set)
    ):
        sum_ = 0
        for i in data_structure:
            sum_ = sum_ + calculate_structure_sum(i)
        return sum_


result = calculate_structure_sum(data_structure)
print(result)
assert result == 99
