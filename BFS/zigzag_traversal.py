import collections
"""
Problem Statements:
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner 
for the following levels.
"""

"""
Input: Root node
Output : a list of sublists of each level, but zig zag 
O(N)
"""

class treeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

def zigzag(treeNode):
    # we initialize a list to record the result 
    res = []
    # we initialize a Queue
    Q = collections.deque()
    #Q will only have the root node initially 
    Q.append(treeNode)
    #initialize a boolean leftToRight 
    leftToRight = True
        #we start with left to right, then we switch to right to left at the end of each loop 

    #while the Q is not empty:
    while Q:
        #get the length of each level
        level_length = len(Q)
    
        # initialize a sublist 
        level_list = collections.deque()

        

        #loop through the current level
        for i in range(level_length):
            #pop the first element of Q
            cur_node = Q.popleft()

            #if leftToRight is true, we append normally
            #else, we appendleft 
            if leftToRight == True:
                level_list.append(cur_node.data)
            else:
                level_list.appendleft(cur_node.data)
            

            #add left children to the Q if there are any 
            if cur_node.left:
                Q.append(cur_node.left)
            #add right childten to the Q if there are any
            if cur_node.right:
                Q.append(cur_node.right)
        
        
        res.append(level_list)
        #switch the boolean 
        leftToRight = not leftToRight
    return res


        
     





"""
Testing
"""
#Build a tree

rootNode = treeNode(12) 
node1  = treeNode(7)
node2  = treeNode(1)
node3 = treeNode(9)
node4 = treeNode(10)
node5 = treeNode(5)
node6 = treeNode(20)
node7 = treeNode(17)

rootNode.left = node1
rootNode.right = node2
node1.left = node3
node2.left = node4
node2.right = node5
node4.left = node6
node4.right = node7

print(zigzag(rootNode))


