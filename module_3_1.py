calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(word):
    count_calls()
    return len(word), word.upper(), word.lower()


def is_contains(string, list_to_search):
    count_calls()
    for word in list_to_search:
        if word.lower() == string.lower():
            return True
    return False


print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contains("Urban", ["ban", "BaNaN", "urBAN"]))  # Urban ~ urBan
print(is_contains("cycle", ["recycle", "cyclic"]))  # No matches
print(calls)
