'''
Created on 20/09/2013

@author: gabriel.flores
'''
import unittest
import SudokuResolver


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMissOneNumber(self):
        lines = "x34678912672195348198342567859761423426853791713924856961537284287419635345286179"    
        resolved = SudokuResolver.resolve(lines)
        expected = "561847923\n379521684\n428963175\n613789542\n794652318\n852134796\n935478261\n146295837\n287316459\n"
        self.assertEqual(expected, resolved, "resolved dont match")

    def testMissSeveralNumbers(self):
        lines = "53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79"
        resolved = SudokuResolver.resolve(lines)

        expected = "561847923\n379521684\n428963175\n613789542\n794652318\n852134796\n935478261\n146295837\n287316459\n"
        self.assertEqual(expected, resolved, "resolved dont match")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()