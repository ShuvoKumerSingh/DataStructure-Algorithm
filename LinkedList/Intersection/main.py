from LinkedList import LinkedListSolution as lls
from Intersection import intersction,addSameNode

llA = lls()
llA.generate(3,0,10)

llB = lls()
llB.generate(4,0,10)

addSameNode(llA,llB,11)
addSameNode(llA,llB,14)


print(llA)
print(llB)

print(intersction(llA,llB))
