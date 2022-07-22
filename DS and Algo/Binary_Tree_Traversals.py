# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [-1 for i in range(self.n)]
    self.left = [-1 for i in range(self.n)]
    self.right = [-1 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self, node, l, r):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    #print(node, l , r, self.left[l], self.right[r])
    if node != -1:
      if l != -1:
        self.inOrder(self.key[l], self.left[l], self.right[l])
      print(node, end=' ')
      if r != -1:
        self.inOrder(self.key[r], self.left[r], self.right[r])
    
                
    return None

  def preOrder(self, node, l, r):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    #print(node, l , r)
    if node != -1:
      print(node, end=" ")
      if l != -1:
        self.preOrder(self.key[l], self.left[l], self.right[l])
      
      if r != -1:
        self.preOrder(self.key[r], self.left[r], self.right[r])
                
    return None

  def postOrder(self, node, l, r):
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    #self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    
    if node != -1:
      if l != -1:
        self.postOrder(self.key[l], self.left[l], self.right[l])
      
      if r != -1:
        self.postOrder(self.key[r], self.left[r], self.right[r])
      print(node, end=' ')
    return None

def main():
	tree = TreeOrders()
	tree.read()
	#print(tree.key)
	##print(tree.left)
	#print(tree.right)
	tree.inOrder(tree.key[0],tree.left[0],tree.right[0])
	print()
	tree.preOrder(tree.key[0],tree.left[0],tree.right[0])
	print()
	tree.postOrder(tree.key[0],tree.left[0],tree.right[0])
	print()
	
	#print(" ".join(str(x) for x in tree.inOrder()))
	#print(" ".join(str(x) for x in tree.preOrder()))
	#print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
