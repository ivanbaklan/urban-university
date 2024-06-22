def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    print(first)
    if len(str_number) == 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))
