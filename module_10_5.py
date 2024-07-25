import multiprocessing


class WarehouseManager:
    data = None

    def __init__(self):
        if not self.data:
            self.data = multiprocessing.Manager().dict()

    def process_request(self, request):
        product_name, action, val = request
        if action == "receipt":
            if product_name not in self.data:
                self.data[product_name] = val
            else:
                self.data[product_name] = self.data[product_name] + val
        if action == "shipment":
            if product_name in self.data and self.data[product_name] > 0:
                self.data[product_name] = self.data[product_name] - val

    def run(self, requests):
        processes = []
        for request in requests:
            process = multiprocessing.Process(
                target=self.process_request, args=(request,)
            )
            processes.append(process)
        [process.start() for process in processes]
        [process.join() for process in processes]


if __name__ == "__main__":
    # Создаем менеджера склада

    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50),
    ]
    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)

# Вывод на консоль:
# {"product1": 70, "product2": 100, "product3": 200}
