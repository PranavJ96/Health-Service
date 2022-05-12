from unicodedata import name
from py2neo import Graph
from py2neo import  Node, Relationship
graph = Graph("bolt://localhost:7687", auth=("neo4j", "hospital"))

# Cleaner
b = Node("Cleaner", name="Barney", gender="Male",longitude=1.3, latitude=1.4)
c = Node("Cleaner", name="Chandler",gender="Male", longitude=3.1, latitude=3.2)
e = Node("Cleaner", name="Elizabeth",gender="Female", longitude=4.4, latitude=4.5)
j = Node("Cleaner", name="Joey",gender="Male", longitude=5.1, latitude=5.2)
l = Node("Cleaner", name="Lilly", gender="Female",longitude=2.4, latitude=2.5)
t = Node("Cleaner", name="Ted",gender="Male", longitude=1.2, latitude=1.1)
#Rooms
r1 = Node("Rooms", name = 101, floor="1", longitude=1.1, latitude=1.2)
r2 = Node("Rooms", name = 102, floor="1", longitude=1.2, latitude=1.2)
r3 = Node("Rooms", name = 103, floor="1", longitude=1.3, latitude=1.2)
r4 = Node("Rooms", name = 104, floor="1", longitude=1.4, latitude=1.2)
r5 = Node("Rooms", name = 105, floor="1", longitude=1.5, latitude=1.2)
r6 = Node("Rooms", name = 201, floor = "2", longitude=1.6, latitude=1.2)
r7 = Node("Rooms", name = 202, floor = "2", longitude=1.7, latitude=2.2)

CLEAN = Relationship.type("CLEAN")

cleaners = [b, c, e, j, l, t]
#compare distance between room and user inside the for loop
# min dist
# selected cleaner
#if b for(i=0 ;i < )
b_r1 = CLEAN(b,r1)
#

c_r2 = CLEAN(c,r2)
e_r3 = CLEAN(j,r3)
j_r4 = CLEAN(j,r4)
l_r5 = CLEAN(l,r5)
t_r6 = CLEAN(b,r6)
t_r7 = CLEAN(b,r7)

cleaned_room = b_r1 | c_r2 | e_r3 | j_r4 | l_r5 | t_r6 | t_r7
# identity = r1.__len__()

graph.create(cleaned_room)

# print(identity)
