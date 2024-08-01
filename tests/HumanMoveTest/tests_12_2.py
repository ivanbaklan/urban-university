import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

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

    def test_Tournament_1(self):
        """
        test tournament distance = 90 with Усэйн and Ник
        """
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        results = tournament_1.start()
        self.all_results.append(results)
        self.assertEqual(results[2].name, self.runner_3.name)

    def test_Tournament_2(self):
        """
        test tournament distance = 90 with Андрей and Ник
        """
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        results = tournament_2.start()
        self.all_results.append(results)
        self.assertEqual(results[2].name, self.runner_3.name)

    def test_Tournament_3(self):
        """
        test tournament distance = 90 with Усэйн, Андрей and Ник
        """
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament_3.start()
        self.all_results.append(results)
        self.assertEqual(results[3].name, self.runner_3.name)

    def test_Tournament_4(self):
        """
        additional test tournament distance = 90 with Усэйн and Андрей
        этот тест падает потому что в классе Tournament методе start
        допущена логическая ошибка, проверка на выполнение дистанции должна проходить
        после обновления атрибутов всех учасников.
        """
        tournament_4 = Tournament(90, self.runner_2, self.runner_1)
        results = tournament_4.start()
        self.assertEqual(results[2].name, self.runner_2.name)


if __name__ == "__main__":
    unittest.main()
