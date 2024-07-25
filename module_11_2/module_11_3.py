class ExampleClass:
    string = "test"

    def print_string(self):
        print(self.string)


instance = ExampleClass()


def introspection_info(obj):
    result = dict()
    result["type"] = obj.__class__.__name__
    result["attributes"] = [
        attr for attr in dir(obj) if not callable(getattr(obj, attr))
    ]
    result["methods"] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    result["module"] = obj.__class__.__module__
    return result


if __name__ == "__main__":
    """
    Атрибуты:

     - Хранят данные об объекте.
     - Могут быть как переменными экземпляра (self.name), так и переменными класса (Person.species).

    Методы:

     - Определяют поведение объекта.
     - Могут изменять состояние объекта или выполнять операции, связанные с объектом.
     - Включают методы экземпляра, методы класса и статические методы.
    """

    number_info = introspection_info(42)
    print(number_info)

    print(introspection_info("new line"))
    print(introspection_info(instance))
    print(introspection_info([]))
    print(introspection_info({}))

    # Вывод на консоль:
    # {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}
