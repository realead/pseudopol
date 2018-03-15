import unittest
import array
import random
import os

import pseudopol.cpseudopol as c_pp
import pseudopol.ppseudopol as p_pp

random.seed(42)

try: 
    RTC_COUNT=int(os.environ['RTC_COUNT'])
except:
    RTC_COUNT=20

class RandomZeroSubSetSumTester(unittest.TestCase): 

    def test_unique_objects(self):
        for _ in range(RTC_COUNT*5):
            n1=random.randint(10,40)
            n2=random.randint(10,40)
            objects=array.array('i', list(random.sample(range(1,100), n1))+[-x for x in random.sample(range(1,100), n2)])
            c_result=c_pp.zerosum_subset_exists(objects)
            p_result=p_pp.zerosum_subset_exists(objects)
            self.assertEqual(c_result, p_result)




