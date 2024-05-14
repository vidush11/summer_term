#I will measure time difference of merge sort in cpp vs python

import time
import math
import random
import json 

random.seed(4)
def merge(start,mid,end,numbers):
    l=end-start+1
    merged_array=[0]*l

    s1=start
    s2=mid+1
    end1=mid
    end2=end

    curr_pos=0
    while (s1<=end1) & (s2<=end2):
        smaller=numbers[s1]
        s1+=1
        if numbers[s2]<smaller:
            smaller=numbers[s2]
            s2+=1
            s1+=-1
        merged_array[curr_pos]=smaller
        curr_pos+=1

    while (s1<=end1):
        merged_array[curr_pos]=numbers[s1]
        curr_pos+=1
        s1+=1

    while (s2<=end2):
        merged_array[curr_pos]=numbers[s2]
        curr_pos+=1
        s2+=1



    for i in range(l):
        numbers[start+i]=merged_array[i]



def merge_sort(start, end, numbers):
    if (start>=end):
        return
    
    if (end-start==1):
        if numbers[start]>numbers[end]:
            temp=numbers[start]
            numbers[start]=numbers[end]
            numbers[end]=temp
    else:
        mid=math.floor((start+end)/2)
        merge_sort(start,mid, numbers)
        merge_sort(mid+1, end, numbers)
        merge(start,mid,end,numbers)

numbers=[x for x in random.choices(range(10**3), k=10**5)]
numbers_=[str(x) for x in random.choices(range(10**3), k=10**5)]

# print(numbers[:100])
numbers_str=''

path1="./numbers.txt"
with open(path1,'w') as file:
    file.write(' '.join(numbers_))

s1=time.time()
# numbers.sort()
merge_sort(0,len(numbers)-1,numbers)
s2=time.time()

# print(numbers)
print(s2-s1)

