import math
import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

#sorting of the list
ages.sort()
print(ages)
#finding min and max number in list
print("the smallest number of list : ",min(ages))
print("the largest number of list  : ",max(ages))

#adding the min and max age again  to list
ages.append(19)
ages.append(26)
print("After addition of  min and max ages to list : ",ages)

#toget the median age
med = statistics.median(ages)
print("Median age  of the list :", str(med))

#toget the  average age
Avg = sum(ages) / len(ages)
print("Average  age of the list is :" , str(Avg))

#toget range of ages
print("Range of ages is : ", (max(ages)-min(ages)))