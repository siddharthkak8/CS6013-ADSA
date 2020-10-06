def cuberoot(a):
    start=1
    end=a
    while(start<=end):
        mid=(start+end)//2
        if(mid*mid*mid==a):
            return mid
        elif (mid * mid*mid > a) :
            end = mid-1
        else :
            start = mid + 1
    return mid
    
            
def main():
    nums=1001
    a=cuberoot(nums)
    print(a)
    
if __name__=="__main__": 
    main() 
	