def check_duplicate(i, j, code):
    is_duplicate = False
    for pair in code:
        if pair == [i, j] or pair == [j, i]:
            is_duplicate = True
    return is_duplicate


def get_num(num):
    code = []
    for i in range(1, num):
        for j in range(1, num):
            if i == j:
                continue
            if (i + j) > num:
                continue
            if num % (i + j):
                continue
            if check_duplicate(i, j, code):
                continue
            code.append([i, j])
    result = ""
    for pair in code:
        result = result + str(pair[0]) + str(pair[1])
    print(num, "-", result)
    return result


num = int(input("input num: "))
get_num(num)
