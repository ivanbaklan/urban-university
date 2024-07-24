first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(item[0]) - len(item[1]) for item in zip(first, second) if len(item[0]) != len(item[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))


# [1, 2]
# [False, False, True]