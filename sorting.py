from random import randint
import time

numList = []
sortedList = []
listSize = int(10000)
for i in range (0,listSize):
	numList.append(randint(0,int(100000)))
# print(numList)

print("Selection Sort!")
start = time.time()
############# Sort numbers in numList into sortedList ###############
sortedList = numList[:]
for y in range (0,listSize):
	for x in range (0,listSize):
 		if sortedList[y]<sortedList[x]:
			sortedList[y], sortedList[x] = sortedList[x], sortedList[y]
# print sortedList
#####################################################################
end = time.time()
print("Time elapsed: ")
print(end-start) 
for i in range (0,listSize-1):
	if sortedList[i] > sortedList[i+1]:
		print("NOT SORTED")
		break


print("Bubble Sort!")
start = time.time()
############# Sort numbers in numList into sortedList ###############
sortedList = numList[:]
swap = 1
while swap == 1:
	swap = 0
	for z in range (0,listSize-1):
		if sortedList[z] > sortedList[z+1]:
			sortedList[z],sortedList[z+1] = sortedList[z+1],sortedList[z]
			swap = 1	
# print sortedList
#####################################################################
end = time.time()
print("Time elapsed: ")
print(end-start) 
for i in range (0,listSize-1):
	if sortedList[i] > sortedList[i+1]:
		print("NOT SORTED")
		break
