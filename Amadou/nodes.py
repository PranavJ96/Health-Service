from unicodedata import name
from py2neo import Graph
from py2neo import  Node, Relationship
graph = Graph("bolt://localhost:7687", auth=("neo4j", "hospital"))

# Create Cleaners
mo = Node("Cleaner", name="Monica",gender="Female", longitude=1.1, latitude=1.2)
rac = Node("Cleaner", name="Rachel",gender="Female", longitude=2.1, latitude=2.2)
c = Node("Cleaner", name="Chandler",gender="Male", longitude=3.1, latitude=3.2)
ros = Node("Cleaner", name="Ross",gender="Male", longitude=4.1, latitude=4.2)
j = Node("Cleaner", name="Joey",gender="Male", longitude=5.1, latitude=5.2)
t = Node("Cleaner", name="Ted",gender="Male", longitude=1.2, latitude=1.1)
b = Node("Cleaner", name="Barney", gender="Male",longitude=1.3, latitude=1.4)
ma = Node("Cleaner", name="Marshall",gender="Male", longitude=1.4, latitude=1.5)
l = Node("Cleaner", name="Lilly", gender="Female",longitude=2.4, latitude=2.5)
rob = Node("Cleaner", name="Robin",gender="Female", longitude=2.5, latitude=2.5)
ray = Node("Cleaner", name="Raymond",gender="Male", longitude=3.4, latitude=3.5)
e = Node("Cleaner", name="Elizabeth",gender="Female", longitude=4.4, latitude=4.5)

cleaners = mo | rac | c | ros | j | t | b | ma | l | rob | ray | e


# Create Rooms
r1 = Node("Rooms", name = 101, floor="1", longitude=1.1, latitude=1.2)
r2 = Node("Rooms", name = 102, floor="1", longitude=1.2, latitude=1.2)
r3 = Node("Rooms", name = 103, floor="1", longitude=1.3, latitude=1.2)
r4 = Node("Rooms", name = 104, floor="1", longitude=1.4, latitude=1.2)
r5 = Node("Rooms", name = 105, floor="1", longitude=1.5, latitude=1.2)
r6 = Node("Rooms", name = 201, floor = "2", longitude=1.6, latitude=1.2)
r7 = Node("Rooms", name = 202, floor = "2", longitude=1.7, latitude=2.2)
r8 = Node("Rooms", name = 203, floor = "2", longitude=1.8, latitude=2.3)
r9 = Node("Rooms", name = 204, floor = "2", longitude=1.9, latitude=2.4)
r10 = Node("Rooms", name = 205, floor = "2",  longitude=2.1, latitude=2.5)
r11 = Node("Rooms", name = 301, floor = "3", longitude=2.2, latitude=2.6)
r12 = Node("Rooms", name = 302, floor = "3", longitude=2.3, latitude=2.7)
r13 = Node("Rooms", name = 303, floor = "3", longitude=2.4, latitude=2.8)
r14 = Node("Rooms", name = 304, floor = "3", longitude=2.5, latitude=2.9)
r15 = Node("Rooms", name = 305, floor = "3", longitude=2.6, latitude=3.0)
r16 = Node("Rooms", name = 401, floor="4", longitude=2.7, latitude=3.1)
r17 = Node("Rooms", name = 402, floor="4", longitude=2.8, latitude=3.2)
r18 = Node("Rooms", name = 403, floor="4", longitude=2.9, latitude=3.0)
r19 = Node("Rooms", name = 404, floor="4", longitude=3.1, latitude=3.8)
r20 = Node("Rooms", name = 405, floor="4", longitude=4.1, latitude=3.9)
r21 = Node("Rooms", name = 501, floor ="5", longitude=5.1, latitude=4.0)
r22 = Node("Rooms", name = 502, floor ="5", longitude=5.2, latitude=4.1)
r23 = Node("Rooms", name = 503, floor ="5", longitude=5.3, latitude=4.2)
r24 = Node("Rooms", name = 504, floor ="5", longitude=5.4, latitude=5.2)

rooms = r1 | r2 | r3 | r4 | r5 | r6 | r7 | r8 | r9 | r10 | r11  | r12 | r13 | r14 | r15 | r16 | r17 | r18 | r19 | r20 | r21 | r22 | r23 | r24



graph.create(rooms)
graph.create(cleaners)
a = graph.run("MATCH (n) RETURN n").data()
print(a)