first = int(input("insert first: "))
second = int(input("insert second: "))
third = int(input("insert third: "))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
