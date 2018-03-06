from cpython cimport array #needed for python2

cdef extern from "subset_sum.c":
    size_t find_max(size_t N, const unsigned int *objects, size_t max_value)
    int subset_sum_exists(size_t N, const int *objects)


#returns maximal subsum<=max_sum
def find_max_subsum(unsigned long long int max_sum, unsigned int[::1] objects not None):
    return find_max(len(objects), &objects[0], max_sum)


#returns true if a nonempty subset with sum=0 exists, otherwise false
def zerosum_subset_exists(int[::1] objects not None):
    return subset_sum_exists(len(objects), &objects[0])!=0
