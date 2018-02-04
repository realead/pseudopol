

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
