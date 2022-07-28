
import collections
"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should
 populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

"""
Input : a root node
Output : A list of sublists of nodes on each level

TC : O(N) - we traverse each node exactly once
"""
#we create a treeNode class 
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#build a binary tree
root = TreeNode(3) #define our root node
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

def levelOrder(rootNode):
    result = [] #record the final result 
    Q = collections.deque() #we initialize a queue to record the nodes level by level
    Q.append(rootNode) #we initialize the queue to have only the root node 

    while (Q): #while Q is not empty, the algo keeps going 
        length = len(Q) #the number of nodes at a particular level
        sublist = [] #we have a sublist to record nodes at every level 
        for i in range(length):
            cur_node = Q.popleft() #pop the first element in the Queue
            if cur_node: #if the node is not null
                sublist.append(cur_node.val) #append the value to the current level
                if cur_node.left : #if there exists a left child , add the left child to the queue
                    Q.append(cur_node.left)
                if cur_node.right: #if there exists a right child, add the right child to the queue 
                    Q.append(cur_node.right)
        result.append(sublist) #add each level to the final result 
    
    return result

print(levelOrder(root))

            



