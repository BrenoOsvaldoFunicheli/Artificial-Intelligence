from Three.Node import Node
from Three.Search.DepthSearch import DepthSearch

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.set_successor(value=b)
a.set_successor(value=c)
c.set_successor(value=d)

s = DepthSearch()

s.search(a, d)