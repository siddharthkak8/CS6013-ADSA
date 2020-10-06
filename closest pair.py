import math

def closestpair(nums):
    minimum=float('-inf')
    distance=0
    for i in range(0,len(nums)):
        xi=int(nums[i][0])
        yi=int(nums[i][1])
        #print(xi,yi)
        for j in range(i+1, len(nums)):
            xj=int(nums[j][0])
            yj=int(nums[j][1])
            #print(xj,yj)
            distance=math.pow((xi-xj),2) + math.pow((yi-yj),2)
            distance= math.sqrt(distance)
            #print(xj,yj,distance)
            if(distance<minimum):
                ai=xi
                aj=xj
                bi=yi
                bj=yj
                
                minimum=distance
    print(ai,bi,aj,bj)
    return minimum

            
def main():
    nums=[[1,2],[2,3],[-4,3],[2,2],[0,0]]
    a=closestpair(nums)
    print(a)
    
if __name__=="__main__": 
    main() 
	
	
	
	
	
	
#Closest pair problem brute force method