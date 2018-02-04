cdef extern from "subset_sum.c":
    size_t find_max(size_t N, const unsigned int *objects, size_t max_value)


#returns maximal subsum<=max_sum
def find_max_subsum(unsigned long long int max_sum, unsigned int[::1] objects not None):
    return find_max(len(objects), &objects[0], max_sum)
