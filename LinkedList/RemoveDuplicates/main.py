from LinkedList import LinkedListSolution as lls
from RemoveDuplicates import removeDuplicates1

customLL = lls()
customLL.generate(10,0,5)
print(customLL)
rmv = removeDuplicates1(customLL)
print(rmv)
