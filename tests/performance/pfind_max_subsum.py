import pseudopol.ppseudopol as p_pp
import numpy as np
import sys

max_val=int(sys.argv[1])

vals=list(np.random.randint(1,500000,5000, dtype=np.uint32))
print(p_pp.find_max_subsum(max_val, vals))

