import threading
from queue import Queue
from time import sleep


class Table:

    def __init__(self, number: int, is_busy: bool = False):
        self.number = number
        self.is_busy = is_busy


class Cafe:

    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables
        self.tables_lock = threading.Lock()

    def customer_arrival(self):
        customers = []
        for i in range(1, 21):
            customer = Customer(i)
            print(f"Посетитель номер {i} прибыл")
            self.serve_customer(customer)
            customers.append(customer)
            sleep(1)
        while True:
            if self.queue.empty():
                break
            customer = self.queue.get()
            self.serve_customer(customer)
            sleep(1)
        for customer in customers:
            customer.join()

    def serve_customer(self, customer):
        with self.tables_lock:
            for table in tables:
                if not table.is_busy:
                    customer.table = table
                    table.is_busy = True
                    customer.start()
                    break
            else:
                self.queue.put(customer)
                print(
                    f"Посетитель номер {customer.name} ожидает свободный стол. (помещение в очередь)"
                )


class Customer(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.table = None

    def run(self):
        print(
            f"Посетитель номер {self.name} сел за стол {self.table.number}. (начало обслуживания)"
        )
        sleep(5)
        self.table.is_busy = False
        print(f"Посетитель номер {self.name} покушал и ушёл. (конец обслуживания)")


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
