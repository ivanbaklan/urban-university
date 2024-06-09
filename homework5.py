immutable_var = (1, "test", True)
# immutable_var[2] = 4
# TypeError: 'tuple' object does not support item assignment
# Кортеж нельзя изменить из за особенностей внутреннего устройства
# Кортеж создается в памяти единым массивом и не имеет методов для изменения
# О чем сообщает ошибка в выводе интерпретатора
print("Immutable tuple:", immutable_var)
mutable_list = [1, "test", True]
mutable_list[2] = False
print("Mutable list:", mutable_list)
