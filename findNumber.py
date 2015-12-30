from random import randint
import time

numList = []
listSize = int(10e6)
for i in range (0,listSize):
	numList.append(randint(0,int(10e9)))
numToFind = numList[randint(0,listSize-1)]
#print(numList)
print("Find this number: " + str(numToFind))
print("------------- Round 1 ------------")
start = time.time()
############# find numToFind in numList ###############
numIndex = 0
for x in range(0,listSize):
	if numToFind == numList[x]:
		numIndex = x

print("The number " + str(numList[numIndex]) + " is at this index: " + str(numIndex))
#######################################################
end = time.time()
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

print("The number " + str(numList[numIndex]) + " is at this index: " + str(numIndex))
#######################################################
end = time.time()
print("Time elapsed: ")
print(end-start)
