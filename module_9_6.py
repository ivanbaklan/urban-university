def all_variants(text):
    for r_side in range(1, len(text)+1):
        for l_side in range(len(text)):
            if l_side + r_side > len(text):
                continue
            yield text[l_side:l_side+r_side]


a = all_variants("abc")
for i in a:
    print(i)

# a
# b
# c
# ab
# bc
# abc