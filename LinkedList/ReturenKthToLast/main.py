from LinkedList import LinkedListSolution as lls
from ReturnKthToLast import nthToLast

customLL = lls()
customLL.generate(10,0,5)
print(customLL)
nth = nthToLast(customLL,3)
print(nth)
