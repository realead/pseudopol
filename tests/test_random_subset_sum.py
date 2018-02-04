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

class RandomSubSetSumTester(unittest.TestCase): 

    def test_unique_weights(self):
        objects=array.array('I', random.sample(range(1,100), 20))
        max_vals=random.sample(range(1,2000), RTC_COUNT)
        for i in max_vals:
           c_result=c_pp.find_max_subsum(i, objects)
           p_result=p_pp.find_max_subsum(i, objects)
           self.assertEqual(c_result, p_result)
    
    def test_nonunique_weights(self):
        lst=[]
        for i in range(500):
           lst.append(random.randint(1,100))
        objects=array.array('I', lst)
        max_vals=random.sample(range(1,2000), RTC_COUNT)
        for i in max_vals:
           c_result=c_pp.find_max_subsum(i, objects)
           p_result=p_pp.find_max_subsum(i, objects)
           self.assertEqual(c_result, p_result)



