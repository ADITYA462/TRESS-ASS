#!/usr/bin/env python
# coding: utf-8

# Implement Binary tree
# 
# Find height of a given tree
# 
# Perform Pre-order, Post-order, In-order traversal
# 
# Function to print all the leaves in a given binary tree
# 
# Implement BFS (Breath First Search) and DFS (Depth First Search)
# 
# Find sum of all left leaves in a given Binary Tree
# 
# Find sum of all nodes of the given perfect binary tree
# 
# Count subtress that sum up to a given value x in a binary tree
# 
# Find maximum level sum in Binary Tree
# 
# Print the nodes at odd levels of a tree
# 

# In[1]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height_recursive(node.left)
            right_height = self._height_recursive(node.right)
            return max(left_height, right_height) + 1

    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node):
        if node:
            print(node.data, end=' ')
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)

    def post_order_traversal(self):
        self._post_order_recursive(self.root)

    def _post_order_recursive(self, node):
        if node:
            self._post_order_recursive(node.left)
            self._post_order_recursive(node.right)
            print(node.data, end=' ')

    def in_order_traversal(self):
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)
            print(node.data, end=' ')
            self._in_order_recursive(node.right)

    def print_leaves(self):
        self._print_leaves_recursive(self.root)

    def _print_leaves_recursive(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.data, end=' ')
            else:
                self._print_leaves_recursive(node.left)
                self._print_leaves_recursive(node.right)

    def bfs(self):
        if self.root is None:
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        self._dfs_recursive(self.root)

    def _dfs_recursive(self, node):
        if node:
            print(node.data, end=' ')
            self._dfs_recursive(node.left)
            self._dfs_recursive(node.right)

    def sum_of_left_leaves(self):
        return self._sum_of_left_leaves_recursive(self.root, False)

    def _sum_of_left_leaves_recursive(self, node, is_left):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            if is_left:
                return node.data
            else:
                return 0
        return self._sum_of_left_leaves_recursive(node.left, True) + self._sum_of_left_leaves_recursive(node.right, False)

    def sum_of_nodes(self):
        return self._sum_of_nodes_recursive(self.root)

    def _sum_of_nodes_recursive(self, node):
        if node is None:
            return 0
       


# In[4]:


def print_odd_levels(self):
    self._print_odd_levels_recursive(self.root, 1)

def _print_odd_levels_recursive(self, node, level):
    if node:
        if level % 2 != 0:
            print(node.data, end=' ')
            self._print_odd_levels_recursive(node.left, level + 1)
            self._print_odd_levels_recursive(node.right, level + 1)


# In[10]:


tree = BinaryTree()

print("Nodes at odd levels:")


# In[ ]:




