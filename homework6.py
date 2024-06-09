my_dict = {"Anya": 1975, "Shon": 1999, "Masha": 2002}
print("Dict:", my_dict)
print("Existing value:", my_dict["Anya"])
print("Not existing value:", my_dict.get("Egor"))
my_dict.update({"Bob": 1986, "Lisa": 1998})
print("Deleted value:", my_dict.pop("Shon"))
print("Modified dictionary:", my_dict)
print("")
my_set = {2, "Груша", 72.514}
print("Set:", my_set)
my_set.update((True, (1, 2, 3)))
my_set.remove(2)
print("Modified set:", my_set)
