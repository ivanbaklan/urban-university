import logging
import sys
import unittest

from rt_with_exceptions import Runner


class RunnerTes(unittest.TestCase):

    def test_walk(self):
        try:
            test_runner = Runner("test_runner", -10)
            for _ in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=sys.exc_info())

    def test_run(self):
        try:
            test_runner = Runner(1)
            for _ in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning(
                "Неверный тип данных для объекта Runner", exc_info=sys.exc_info()
            )

    def test_challenge(self):
        test_runner_1 = Runner("test_runner_1")
        test_runner_2 = Runner("test_runner_2")
        for _ in range(10):
            test_runner_1.walk()
            test_runner_2.run()
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        filemode="w",
        filename="runner_tests.log",
        encoding="utf8",
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    unittest.main()
