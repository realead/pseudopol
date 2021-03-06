import unittest
import array

import pseudopol.cpseudopol as c_pp
import pseudopol.ppseudopol as p_pp

class ZeroSubSetSumTester(object): 

    def test_empty_set(self):
        self.assertEqual(False, self.pp.zerosum_subset_exists(array.array('i')))

    def test_set_with_zero1(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[0])))

    def test_set_with_zero2(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[0,1])))

    def test_set_with_zero3(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[2,0,1])))

    def test_set_with_zero4(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[2,4,6,0])))

    def test_only_pos(self):
        self.assertEqual(False, self.pp.zerosum_subset_exists(array.array('i',[2,4,6])))
  
    def test_only_neg(self):
        self.assertEqual(False, self.pp.zerosum_subset_exists(array.array('i',[-2,-4,-6,-4,-8])))  

    def test_two_equal_pm_2(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[2,-2])))  

    def test_two_equal_pm_1(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-1,1]))) 

    def test_two_equal_pm_16(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-16,16])))

    def test_two_equal_pm_15(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-15,15])))  

    def test_two_equal_pm_31(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-31,31]))) 

    def test_two_equal_pm_32(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-32,32])))  

    def test_two_equal_pm_63(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-63,63]))) 

    def test_two_equal_pm_64(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-64,64]))) 

    def test_three_yes_1(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[1,-2,1])))

    def test_three_yes_2(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[1,2,-3])))  

    def test_three_yes_3(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[1,63,-64])))    

    def test_three_yes_4(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-65,63,2])))  

    def test_three_no_1(self):
        self.assertEqual(False, self.pp.zerosum_subset_exists(array.array('i',[1,-3,1])))

    def test_three_no_2(self):
        self.assertEqual(False, self.pp.zerosum_subset_exists(array.array('i',[1,4,-3])))  

    def test_three_no_3(self):
        self.assertEqual(False, self.pp.zerosum_subset_exists(array.array('i',[1,62,-64])))    

    def test_three_no_4(self):
        self.assertEqual(False, self.pp.zerosum_subset_exists(array.array('i',[-66,65,2])))   

    def test_three_not_all_needed(self):
        self.assertEqual(True, self.pp.zerosum_subset_exists(array.array('i',[-64,64,2])))  

    def test_bins_pos_yes(self):
        lst=[2,4,8,16,32,64,128,256,512,1024]        
        for i in range(2,1048,2):
            bins=array.array('i', lst+[-i])
            self.assertEqual(True, self.pp.zerosum_subset_exists(bins))

    def test_bins_pos_no(self):
        lst=[2,4,8,16,32,64,128,256,512,1024]        
        for i in range(1,1048,2):
            bins=array.array('i', lst+[-i])
            self.assertEqual(False, self.pp.zerosum_subset_exists(bins))

    def test_bins_neg_yes(self):
        lst=[-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024]        
        for i in range(2,1048,2):
            bins=array.array('i', lst+[i])
            self.assertEqual(True, self.pp.zerosum_subset_exists(bins))

    def test_bins_neg_no(self):
        lst=[-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024]        
        for i in range(1,1048,2):
            bins=array.array('i', lst+[i])
            self.assertEqual(False, self.pp.zerosum_subset_exists(bins))

### Error tests:

    def test_out_of_memory(self):
        lst=[1<<30]*1000
        bins=array.array('i', lst+[-(x-1) for x in lst])
        with self.assertRaises(MemoryError) as context:
             self.pp.zerosum_subset_exists(bins)

#real testers
class CZeroSubsetSumTester(ZeroSubSetSumTester, unittest.TestCase):
    pp=c_pp

class PZeroSubsetSumTester(ZeroSubSetSumTester, unittest.TestCase):
    pp=p_pp




