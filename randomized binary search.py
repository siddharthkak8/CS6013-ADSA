import random
def bin_search(A, left, right, k):
    #Code here
    while(left<=right):
        t=random.randint(left,right)
        if(A[t]==k):
            return t
        elif(A[t]<k):
            return bin_search(A,t+1,right,k)
        else:
            return bin_search(A,left,t-1,k)
    
    return -1