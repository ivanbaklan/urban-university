class WordsFinder:

    def __init__(self, *args):
        self.file_names = list(args)
        self.all_words = {}
        for file in self.file_names:
            self._read_file(file)

    def get_all_words(self):
        return self.all_words

    def _clean_text(self, line):
        line = line.lower()
        replace_list = [",", ".", "=", "!", "?", ";", ":", " - "]
        for i in replace_list:
            line = line.replace(i, "")
        return line.split()

    def _read_file(self, file_name):
        with open(file_name, "r") as file:
            text = file.read()
            self.all_words[file_name] = self._clean_text(text)

    def find(self, find_word):
        result = {}
        for file in self.all_words.keys():
            for num, word in enumerate(self.all_words[file], 1):
                if find_word.lower() == word:
                    result[file] = num
                    break
        return result

    def count(self, count_word):
        result = {}
        for file in self.all_words.keys():
            count = 0
            for word in self.all_words[file]:
                if count_word.lower() == word:
                    count += 1
            result[file] = count
        return result


finder2 = WordsFinder("test_file.txt")
print(finder2.get_all_words())  # Все слова
print(finder2.find("TEXT"))  # 3 слово по счёту
print(finder2.count("teXT"))  # 4 слова teXT в тексте всего


# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
