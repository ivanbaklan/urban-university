import unittest

import runner
from runner_and_tournament import Runner, Tournament


class RunnerTes(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_walk(self):
        test_runner = runner.Runner("test_runner")
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_run(self):
        test_runner = runner.Runner("test_runner")
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_challenge(self):
        test_runner_1 = runner.Runner("test_runner_1")
        test_runner_2 = runner.Runner("test_runner_2")
        for _ in range(10):
            test_runner_1.walk()
            test_runner_2.run()
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print({key: val.name for key, val in result.items()})

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_Tournament_1(self):
        """
        test tournament distance = 90 with Усэйн and Ник
        """
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        results = tournament_1.start()
        self.all_results.append(results)
        self.assertEqual(results[2].name, self.runner_3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_Tournament_2(self):
        """
        test tournament distance = 90 with Андрей and Ник
        """
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        results = tournament_2.start()
        self.all_results.append(results)
        self.assertEqual(results[2].name, self.runner_3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_Tournament_3(self):
        """
        test tournament distance = 90 with Усэйн, Андрей and Ник
        """
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament_3.start()
        self.all_results.append(results)
        self.assertEqual(results[3].name, self.runner_3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_Tournament_4(self):
        """
        additional test tournament distance = 90 with Усэйн and Андрей
        этот тест падает потому что в классе Tournament методе start
        допущена логическая ошибка, проверка на выполнение дистанции должна проходить
        после обновления атрибутов всех учасников.
        """
        tournament_4 = Tournament(90, self.runner_2, self.runner_1)
        results = tournament_4.start()
        print(results[2].name)
        print(self.runner_2.name)
        self.assertEqual(results[2].name, self.runner_2.name)
