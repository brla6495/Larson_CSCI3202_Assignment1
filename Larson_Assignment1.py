import Queue
import time
class FIFOQueue:
    
    def __init__(self):
        self.queue = Queue.Queue()
        
    def enqueue (self,a):
        self.queue.put(a)
        
    def dequeue (self):
        if not self.queue.empty():
            print self.queue.get()   
             
    def dequeueAll(self):
        while not self.queue.empty():
            print self.queue.get()
            
class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push (self, a):
        self.stack.append(a)
        
    def pop (self):
        if self.checkSize() > 0:
            return self.stack.pop()
        else:
            return self.stack
            
    def checkSize(self):
        return len(self.stack) 

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.data = val
class BinaryTree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.data = val
                        
    def delete(self, val, rootNode):
        if rootNode is None:
            print "Node not found"
            return False   
        elif val == rootNode.data:
            if rootNode.left or rootNode.right:
                print "Node not deleted, has children"
                return False
            else:    
                del rootNode.left
                del rootNode.right
                del rootNode.parent
                del rootNode.data
                del rootNode
                return True
        elif val < rootNode.data:
            self.delete(val, rootNode.left)
        else:
            try:
                self.delete(val, rootNode.right)  
            except:
                pass
                
def add(rootNode, newNode):
    if rootNode is None:
        #rootNode = newNode
        print "Parent not found"
    else:
        if rootNode.data > newNode.data:
            if rootNode.left == None:
                rootNode.left = newNode
                newNode.parent = rootNode
            else:
                add(rootNode.left, newNode)
        else:
            if rootNode.right == None:
                rootNode.right = newNode
                newNode.parent = rootNode
            else:
                add(rootNode.right, newNode)

def printTree(rootNode):
    if not rootNode:
        return
    try:
        print rootNode.data
    except:
        pass
    try:
        printTree(rootNode.left)
    except:
        pass
    try:
        printTree(rootNode.right)
    except:
        pass
        
    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.verticesCount = 0
    def __iter__(self):
        return iter(self.vertices.values())
    def addVertex(self, key):
        if key not in self.vertices:
            self.verticesCount = self.verticesCount + 1
            newVertex = Vertex(key)
            self.vertices[key] = newVertex
            return newVertex
        else:
            print ("Vertex already exists")    
    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None
    def addEdge(self,value1,value2):
        if value1 not in self.vertices:
            print ("One or more vertices not found")
        elif value2 not in self.vertices:
            print ("One or more vertices not found")
        else:
            self.vertices[value1].addAdjacency(self.vertices[value2], 0)
    def findVertex(self, value):
        if value in self.vertices:
            for verts1 in self:
	            for verts2 in verts1.getAdjacencies():
	                if verts1.data == value:
		                print("( %s , %s )" % (verts1.data, verts2.data))
        else:
            print ("false")          

class Vertex:
    def __init__(self, key):
        self.data = key
        self.adjacentTo = {}
    def addAdjacency(self, vertex, weight = 0):
        self.adjacentTo[vertex] = weight
    def getAdjacencies(self):
        return self.adjacentTo.keys()
        
print "---------------------------------------------------------------------------"
print "Queue"
print "---------------------------------------------------------------------------"
time.sleep(2)
print "q = FIFOQueue() // new Queue object"
q = FIFOQueue()
time.sleep(1)
print "q.enqueue(1) // enqueues the integer: 1"
time.sleep(1)
q.enqueue(1)
print "enqueueing 2-10 with a for loop..."
for i in range (2,11):
    q.enqueue(i)
time.sleep(1)
print "q.dequeue() // dequeues first and prints it"
q.dequeue()
time.sleep(1)
print "q.dequeueAll() // dequeues the remaining values and prints them"
time.sleep(1)
q.dequeueAll()
time.sleep(1)
print "---------------------------------------------------------------------------"
print "Stack"
print "---------------------------------------------------------------------------"
time.sleep(2)
print "s = Stack() // new Stack object"
s = Stack()
time.sleep(1)
print "s.push(1) // pushes the integer: 1"
s.push(1)
time.sleep(1)
print "pushing 2-10 with a for loop..."
for i in range (2,11):
    s.push(i)
time.sleep(1)    
print "print s.stack // show stack before popping"    
print s.stack
time.sleep(1)
print "popping using a for loop and s.pop()..."
for i in range (10):
    print s.pop()
    time.sleep(0.1)
time.sleep(1)
print "print s.checkSize() // to make sure it is empty"
time.sleep(1)
print s.checkSize()
time.sleep(1)
print "---------------------------------------------------------------------------"
print "Binary Tree"
print "---------------------------------------------------------------------------"
time.sleep(2)
print "bt = BinaryTree(3) // new BinaryTree object with 3 as root node"
bt = BinaryTree(3)
time.sleep(1)
print "add(bt, Node(2)) // add node with value: 2 to tree (left child of root)"
add(bt, Node(2))
time.sleep(1)
print "adding 4-11 with for loop"
for i in range (4,12):
    add(bt, Node(i))
time.sleep(1)
print "printTree(bt) // prints tree"
time.sleep(1)
printTree(bt)
time.sleep(1)
print "bt.delete(4,bt) // Deletes 4"
bt.delete(4, bt)
time.sleep(1)
print "bt.delete(11,bt) // Deletes 11"
bt.delete(11, bt)
time.sleep(1)
print "printTree(bt) // Prints to show deletion"
printTree(bt)
time.sleep(1)
print "---------------------------------------------------------------------------"
print "Graph"
print "---------------------------------------------------------------------------"
time.sleep(2)
g = Graph()
print "g = Graph() // new Graph object"
time.sleep(1)
print "g.addVertex(1) // adds a vertex with integer value: 1"
g.addVertex(1)
time.sleep(1)
print "adding vertices 2-10 with a for loop..."
for i in range (2,11):
    g.addVertex(i)
time.sleep(1)
print "adding 20 edges..."    
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(1,5)
g.addEdge(1,7)
g.addEdge(2,4)
g.addEdge(2,6)
g.addEdge(2,8)
g.addEdge(2,10)
g.addEdge(2,5)
g.addEdge(3,5)
g.addEdge(3,6)
g.addEdge(3,7)
g.addEdge(3,9)
g.addEdge(3,10)
g.addEdge(4,5)
g.addEdge(4,7)
g.addEdge(4,8)
g.addEdge(4,9)
g.addEdge(4,10)
g.addEdge(5,6)
g.addEdge(5,7)
g.addEdge(5,8)
g.addEdge(5,9)
g.addEdge(5,10)
time.sleep(1)
print "g.findVertex for 1, 2, 3, and 4 // finds vertices and displays their edges"
time.sleep(1)
g.findVertex(1)
time.sleep(0.25)
g.findVertex(2)
time.sleep(0.25)
g.findVertex(3)
time.sleep(0.25)
g.findVertex(4)
time.sleep(0.25)
g.findVertex(5)
print "done."
    

