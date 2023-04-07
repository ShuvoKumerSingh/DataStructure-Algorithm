from LinkedList import LinkedListSolution as lls
from Partition import partition

customLL = lls()
customLL.generate(10,0,99)
print(customLL)
partitionLL = partition(customLL,10)
print(partitionLL)
