from LinkedList import LinkedListSolution as lls
from SumLists import sumList

llA = lls()
llA.add(7)
llA.add(1)
llA.add(6)


llB = lls()
llB.add(5)
llB.add(9)
llB.add(2)

print(llA)
print(llB)

print(sumList(llA,llB))
