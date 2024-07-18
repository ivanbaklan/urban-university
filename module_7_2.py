def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    result = {}
    for num, string in enumerate(strings, 1):
        position = file.tell()
        file.write(f"{string} \n")
        result[(num, position)] = string
    file.close()
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')