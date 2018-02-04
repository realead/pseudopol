import unittest
import array
import random

import pseudopol.cpseudopol as c_pp
import pseudopol.ppseudopol as p_pp

random.seed(42)

class RadnomSubSetSumTester(unittest.TestCase): 

    def test_unique_weights(self):
        objects=array.array('I', random.sample(range(1,100), 20))
        for i in range(2000):
           c_result=c_pp.find_max_subsum(i, objects)
           p_result=p_pp.find_max_subsum(i, objects)
           self.assertEqual(c_result, p_result)
    
    def test_nonunique_weights(self):
        lst=[]
        for i in range(500):
           lst.append(random.randint(1,100))
        objects=array.array('I', lst)
        for i in range(2000):
           c_result=c_pp.find_max_subsum(i, objects)
           p_result=p_pp.find_max_subsum(i, objects)
           self.assertEqual(c_result, p_result)



