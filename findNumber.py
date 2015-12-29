from random import randint
import time

numList = []
listSize = int(10)
for i in range (0,listSize):
	numList.append(randint(0,int(10e6)))
numToFind = numList[randint(0,listSize-1)]
print(numList)
print("Find this number: " + str(numToFind))
start = time.time()
############# find numToFind in numList ###############
numIndex = 0



print("The number " + str(numList[numIndex]) + " is at this index: " + str(numIndex))
#######################################################
end = time.time()
print("Time elapsed: " + str(end-start))