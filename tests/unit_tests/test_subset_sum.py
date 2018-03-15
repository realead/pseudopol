import unittest
import array

import pseudopol.cpseudopol as c_pp
import pseudopol.ppseudopol as p_pp

class SubSetSumTester(object): 

    def test_empty_set(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I')))

    def test_one_bit_too_big(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [64])))
    
    def test_last_bin_in_last(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [63])))

    def test_one_element_too_big(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [2])))

    def test_one_element_too_2(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [60])))

    def test_one_element_too_3(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [32])))

    def test_one_element_too_4(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [31])))

    def test_one_element_too_5(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [3])))

    def test_one_element_too_6(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [7])))

    def test_one_element_too_7(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [8])))

    def test_one_element_too_8(self):
        self.assertEqual(0, self.pp.find_max_subsum(1, array.array('I', [15])))

    def test_one_element_fits(self):
        self.assertEqual(1, self.pp.find_max_subsum(1, array.array('I', [1])))

    def test_max_last_bit(self):
        self.assertEqual(0, self.pp.find_max_subsum(63, array.array('I', [64])))

    def test_max_frist_bit(self):
        self.assertEqual(64, self.pp.find_max_subsum(64, array.array('I', [64])))

    def test_max_frist_bit2(self):
        self.assertEqual(63, self.pp.find_max_subsum(64, array.array('I', [63])))

    def test_max_frist_bit3(self):
        self.assertEqual(63, self.pp.find_max_subsum(64, array.array('I', [63,2])))

    def test_zero_weigth(self):
        self.assertEqual(0, self.pp.find_max_subsum(64, array.array('I', [0])))

### examples with more elements
    def test_bins(self):
        bins=array.array('I', [1,2,4,8,16,32,64,128,256,512,1024])
        for i in range(1048):
            self.assertEqual(i, self.pp.find_max_subsum(i, bins))

    def test_one_zero_weigth(self):
        self.assertEqual(64, self.pp.find_max_subsum(64, array.array('I', [0,63,1,2])))

### Error tests:

    def test_out_of_memory(self):
        bins=array.array('I', [1<<31]*10000)
        m=1<<48#for bigger number  (sys.maxsize for P3 or sys.maxint for P2) it could be OverflowError
        with self.assertRaises(MemoryError) as context:
             self.pp.find_max_subsum(m, bins)

      
#real testers
class CSubSetSumTester(SubSetSumTester, unittest.TestCase):
    pp=c_pp

class PSubSetSumTester(SubSetSumTester, unittest.TestCase):
    pp=p_pp




