#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True


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

  def inOrder(self, node, l, r, maxi, mini):
    
    if node != -1:
      l_ans = r_ans = True
      if node < mini or node >= maxi:
        return False
      if l != -1:
        l_ans = self.inOrder(self.key[l], self.left[l], self.right[l], node, mini)
      #print(node, end=' ')
      if r != -1:
        r_ans = self.inOrder(self.key[r], self.left[r], self.right[r], maxi, node)
      #print(node, l , r, maxi, mini, l_ans, r_ans)
      return l_ans and r_ans
    return True

def main():
  """
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")
  """
  tree = TreeOrders()
  tree.read()
  #print(tree.key)
  #print(tree.left)
  #print(tree.right)
  if tree.n == 0:
    print("CORRECT")
    return
  final = tree.inOrder(tree.key[0],tree.left[0],tree.right[0],4294967296,-4294967296)
  if final:
    print("CORRECT")
  else:
    print("INCORRECT")
    
threading.Thread(target=main).start()
