from cpython cimport array #needed for python2

cdef extern from "subset_sum.c":
    size_t find_max(size_t N, const unsigned int *objects, size_t max_value, int *error)
    int subset_sum_exists(size_t N, const int *objects)


#returns maximal subsum<=max_sum
def find_max_subsum(unsigned long long int max_sum, unsigned int[::1] objects not None):
    cdef int error=0 
    #corner case: 
    if(len(objects)==0):
        return 0    
    #check errors:
    result=find_max(len(objects), &objects[0], max_sum, &error)
    if error!=0:
         raise MemoryError()
    return result


#returns true if a nonempty subset with sum=0 exists, otherwise false
def zerosum_subset_exists(int[::1] objects not None):
    cdef int result=0
    if(len(objects)==0):
        return False
    result=subset_sum_exists(len(objects), &objects[0])
    if result<0:
         raise MemoryError()
    return result!=0
