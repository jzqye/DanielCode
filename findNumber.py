from random import randint
import time

numList = []
listSize = int(5000000)
# for i in range (0,listSize):
# 	numList.append(randint(0,int(1000)))
# numToFind = numList[randint(0,listSize-1)]
# numList = numList[:]
# swap = 1
# while swap == 1:
# 	swap = 0
# 	for z in range (0,listSize-1):
# 		if numList[z] > numList[z+1]:
# 			numList[z],numList[z+1] = numList[z+1],numList[z]
# 			swap = 1	

for ii in range(0,listSize):
	numList.append(ii)
numToFind = numList[randint(0,listSize-1)]
#######################################################################
print("Find this number: " + str(numToFind))
print("------------- Round 1 ------------")
start = time.time()
############# find numToFind in numList ###############
numIndex = 0
for x in range(0,listSize):
	if numToFind == numList[x]:
		numIndex = x

end = time.time()
print("The number " + str(numList[numIndex]) + " is at this index: " + str(numIndex))
#######################################################
print("Time elapsed: ")
print(end-start)


print("------------- Round 2 ------------")
start = time.time()
############# find numToFind in numList ###############
numIndex = 0
for x in range(0,listSize):
	if numToFind == numList[x]:
		numIndex = x
		break

end = time.time()
print("The number " + str(numList[numIndex]) + " is at this index: " + str(numIndex))
#######################################################
print("Time elapsed: ")
print(end-start)

print("------------- Round 3 ------------")
start = time.time()
############# find numToFind in numList ###############
lowIndex = 0 
middleIndex = listSize/2
highIndex = listSize
while numToFind != numList[middleIndex]:
	middleIndex = (lowIndex + highIndex)/2
	if numToFind < numList[middleIndex]:
		highIndex = middleIndex
	else:
		lowIndex = middleIndex
# if numToFind == numList[middleIndex]:
# 	numIndex = middleIndex

end = time.time()
print("The number " + str(numList[middleIndex]) + " is at this index: " + str(numIndex))
#######################################################
print("Time elapsed: ")
print(end-start)

