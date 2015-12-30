from random import randint
import time

numList = []
sortedList = []
listSize = int(10)
for i in range (0,listSize):
	numList.append(randint(0,int(100)))
print(numList)

start = time.time()
############# Sort numbers in numList into sortedList ###############






#####################################################################
end = time.time()
print("Time elapsed: ")
print(end-start)

for i in range (0,listSize):
	if sortedList[i] > sortedList[i+1]:
		print("NOT SORTED")
print("Sorted!!!!")
print(sortedList)