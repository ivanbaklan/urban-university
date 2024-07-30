import unittest

from tests_12_3 import RunnerTes, TournamentTest

HumanMoveTestSuite = unittest.TestSuite()
HumanMoveTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTes))
HumanMoveTestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(HumanMoveTestSuite)
