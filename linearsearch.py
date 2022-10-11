def linear(list,n,key):
    for i in range(0,n):
        if(list[i]==key):
            return i;
            return -1;
 # now we input the list        
list1 = [10,20,30,80,90,96]
n1 = len(list1)
key1 = 96
# function call
res = linear(list1,n1,key1)
#printing the location of value
if(res == -1):
    print("elemnt not found")
else:
    print("element found ",res)
    
    Worst complexity: O(n)
Average complexity: O(n)
Space complexity: O(1)
Average performance: O(n/2)
