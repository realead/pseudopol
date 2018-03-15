

def find_max_subsum(max_sum, objects):
    reachable=[False]*(max_sum+1)
    reachable[0]=True
    for o in objects:
        for i in range(max_sum,-1,-1):
            if reachable[i] and i+o<=max_sum:
                reachable[i+o]=True

    for i in range(max_sum,0,-1):
        if reachable[i]:
            return i
    
    return 0 





def zerosum_subset_exists(objects):
    if 0 in objects:
        return True

    positive=[x for x in objects if x>0]
    negative=[abs(x) for x in objects if x<0]

    ## all positive
    n=sum(positive)
    reachable=[False]*(n+1)
    reachable[0]=True
    for o in positive:
        for i in range(n,-1,-1):
            if reachable[i] and i+o<=n:
                reachable[i+o]=True

    ## all negative:
    for o in negative:
        for i in range(1,n+1):
            if reachable[i]:
                index=i-o
                if index==0:
                    return True
                elif index>0:
                    reachable[index]=True
  
    return False
   
