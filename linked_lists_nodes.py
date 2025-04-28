#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 12:44:44 2025

@author: tancredi
"""

# What is a Linked List?

# A Linked List is a sequence of nodes where each node points to the next node.

# Each Node contains:
# - Data (the value)
# - Next (a pointer to the next node)

# Unlike arrays, linked lists don't need contiguous memory.

# ---

# Basic Linked List in Python

# 1. Define a Node class

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# Every Node has:
# - data → the value stored
# - next → the link to the next node

# ---

# 2. Create a Linked List manually

# head = Node(1)         # First node (head)
# second = Node(2)       # Second node
# third = Node(3)        # Third node

# # Link them together
# head.next = second
# second.next = third

# Now the list is: 1 -> 2 -> 3 -> None

# ---

# 3. Traverse (print) the Linked List

# current = head
# while current is not None:
#     print(current.data, end=" -> ")
#     current = current.next
# print("None")

# Output:
# 1 -> 2 -> 3 -> None

# ---

# Key operations on Linked Lists

# | Operation         | How to do it                      |
# |:------------------|:----------------------------------|
# | Insert at front   | New node points to head, move head |
# | Insert at end     | Traverse to last node, add after it |
# | Delete a node     | Change .next pointer of previous node |
# | Search a value    | Traverse until found |

# ---

# Example: Insert at front

# new_node = Node(0)
# new_node.next = head
# head = new_node

# Now the list is 0 -> 1 -> 2 -> 3 -> None

# ---

# Example: Insert at end

# new_node = Node(4)

# current = head
# while current.next:
#     current = current.next

# current.next = new_node

# Now the list is 0 -> 1 -> 2 -> 3 -> 4 -> None

# ---

# Full simple Linked List class (optional, cleaner)

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# Usage:

# ll = LinkedList()
# ll.insert_at_end(1)
# ll.insert_at_end(2)
# ll.insert_at_end(3)
# ll.print_list()

# Output:
# 1 -> 2 -> 3 -> None

# ---

# Quick Cheat Sheet:

# | Task                     | Code                          |
# |:--------------------------|:------------------------------|
# | Create node               | n = Node(data)                |
# | Create list               | Link nodes using .next        |
# | Traverse list             | Use while current loop        |
# | Insert at beginning       | new.next = head; head = new   |
# | Insert at end             | Traverse to last, add new node |

# ---

# Linked Lists are super useful for dynamic structures where insertion/deletion needs to be fast!