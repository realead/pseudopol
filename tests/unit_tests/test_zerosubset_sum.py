import unittest
import array

import pseudopol.cpseudopol as c_pp
import pseudopol.ppseudopol as p_pp

class SubSetSumTester(object): 

    def test_empty_set(self):
        self.assertEqual(False, self.fun(array.array('i')))

    def test_set_with_zero1(self):
        self.assertEqual(True, self.fun(array.array('i',[0])))

    def test_set_with_zero2(self):
        self.assertEqual(True, self.fun(array.array('i',[0,1])))

    def test_set_with_zero3(self):
        self.assertEqual(True, self.fun(array.array('i',[2,0,1])))

    def test_set_with_zero4(self):
        self.assertEqual(True, self.fun(array.array('i',[2,4,6,0])))

    def test_only_pos(self):
        self.assertEqual(False, self.fun(array.array('i',[2,4,6])))
  
    def test_only_neg(self):
        self.assertEqual(False, self.fun(array.array('i',[-2,-4,-6,-4,-8])))  

    def test_two_equal_pm_2(self):
        self.assertEqual(True, self.fun(array.array('i',[2,-2])))  

    def test_two_equal_pm_1(self):
        self.assertEqual(True, self.fun(array.array('i',[-1,1]))) 

    def test_two_equal_pm_16(self):
        self.assertEqual(True, self.fun(array.array('i',[-16,16])))

    def test_two_equal_pm_15(self):
        self.assertEqual(True, self.fun(array.array('i',[-15,15])))  

    def test_two_equal_pm_31(self):
        self.assertEqual(True, self.fun(array.array('i',[-31,31]))) 

    def test_two_equal_pm_32(self):
        self.assertEqual(True, self.fun(array.array('i',[-32,32])))  

    def test_two_equal_pm_63(self):
        self.assertEqual(True, self.fun(array.array('i',[-63,63]))) 

    def test_two_equal_pm_64(self):
        self.assertEqual(True, self.fun(array.array('i',[-64,64]))) 


#real testers
class CZeroSubsetSumTester(SubSetSumTester, unittest.TestCase):
    fun=c_pp.zerosum_subset_exists

#class PSubSetSumTester(SubSetSumTester, unittest.TestCase):
#    pp=p_pp




