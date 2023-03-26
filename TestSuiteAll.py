import unittest
from TestArithmeticOperations import TestArithmeticOperations
from TestBankAccount import TestBankAccount
from TestBasicStatistics import TestBasicStatistics
from TestDateManipulations import TestDateManipulations
from TestGeometryCalculations import TestGeometryCalculations
from TestListManager import TestListManager
from TestQueue import TestQueue
from TestStack import TestStack
from TestStringFormatting import TestStringFormatting
from TestStringManipulation import TestStringManipulation

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestArithmeticOperations))
    suite.addTest(unittest.makeSuite(TestBankAccount))
    suite.addTest(unittest.makeSuite(TestBasicStatistics))
    suite.addTest(unittest.makeSuite(TestDateManipulations))
    suite.addTest(unittest.makeSuite(TestGeometryCalculations))
    suite.addTest(unittest.makeSuite(TestListManager))
    suite.addTest(unittest.makeSuite(TestQueue))
    suite.addTest(unittest.makeSuite(TestStack))
    suite.addTest(unittest.makeSuite(TestStringFormatting))
    suite.addTest(unittest.makeSuite(TestStringManipulation))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
