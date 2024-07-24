from datetime import datetime
from threading import Thread
from time import sleep


def wite_words(word_count, file_name):
    with open(file_name, "w") as f:
        for word_num in range(word_count):
            f.write(f"Какое-то слово № {word_num}\n")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
time_end = datetime.now()

print(f"Затраченное время без тредов: {time_end-time_start}")

thread_1 = Thread(target=wite_words, args=(10, "example5.txt"))
thread_2 = Thread(target=wite_words, args=(30, "example6.txt"))
thread_3 = Thread(target=wite_words, args=(200, "example7.txt"))
thread_4 = Thread(target=wite_words, args=(100, "example8.txt"))

time_start = datetime.now()
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
time_end = datetime.now()

print(f"Затраченное время с тредами: {time_end-time_start}")
