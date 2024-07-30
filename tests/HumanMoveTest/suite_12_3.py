import unittest

from tests_12_3 import RunnerTest, TournamentTest

HumanMoveTestSuite = unittest.TestSuite()
HumanMoveTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
HumanMoveTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(HumanMoveTestSuite)
