def qsort(alist): return [] if len(alist)==0 else qsort([item for item in alist[1:] if item < alist[0]]) + [alist[0]] + qsort([item for item in alist[1:] if item >= alist[0]])

print(qsort([5, 7, 8, 4, 9, 2, 2, 3, 6, 8, 1, 8, 3, 9, 3, 6, 3, 1, 6, 0, 7, 0, 3]))


def count(T, v):
    if v == None:
         return 0
    else:
        return count(T, T[v][0]) + 1 + count(T, T[v][1]) 


"""
       0
      / \
     1   2
    / \ / \
  ...........
Eventually the nodes form leaves with 'None' Children

Resursive Relationship:
No. Nodes in Tree Starting at 0 = No. Nodes in Tree Starting at 1 + 1 + No. Nodes in Tree Starting at 2
or more generally:
No. Nodes in Tree Starting at i = No. Nodes in Tree Starting at left child of i + 1 + No. Nodes in Tree Starting at right child of i
The plus one comes from the root node itself!

Base Case: 
The base case is the child of a leaf. But a leaf doesn't have children. 
We represent this as 'None' though. If we hit a 'None', it isn't a tree, so its size
is clearly zero. 

Note that we are clearly moving towards the base case each call as we are always calling
the function on a current 

I'm going to guess that a lot of students will design this function such that it
will never be passed 'None' as the input 'v'. Even though 'None' isn't a node,
we can still utlise it in our recusive function to simplify the logic. 

"""
# Examples:
tree = [(2,1), (3,None), (5,4), (None, None), (None, None), (None,None)]
print(count(tree, 0))
print(count(tree, 1))
print(count(tree, 2))
print(count(tree, 4))
