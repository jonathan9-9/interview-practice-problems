# Using your notes and the results of the ordering problem, implement the
# function binary_search(items, target) in Python.


def binary_search(items, target):
    start = 0
    end = len(items) - 1
    while start <= end:
        half = (start + end) // 2
        value = items[half]
        if target == value:
            return value

        elif target < value:
            end = half - 1
        else:
            start = half + 1
    return None


# The function find_lists_with_minimum_value takes in a list of lists.
# The function will consider all of the values in all of the lists and
# find the minimum value. Then, it will return a list that contains the
# indexes of the lists that contain the minimum value in increasing order

# INPUT
[
    [6, 4, 5, 2, 6, 3, 2],
    [3, 3, 3, 4],
    [4, 2, 3, 2, 4],
]

# OUTPUT
[0, 2]


def find_lists_with_minimum_value(lists):
    list_of_indexes = []
    min_value = float("inf")
    for idx, lst in enumerate(lists):
        current_minimum = min(lst)
        if current_minimum < min_value:
            min_value = current_minimum
            list_of_indexes = [idx]
        elif current_minimum == min_value:
            list_of_indexes.append(idx)
    return list_of_indexes


# OR


def find_lists_with_minimum_value(lists):
    minimum = min([min(nums) for nums in lists])
    return [i for i, nums in enumerate(lists) if minimum in nums]


# When babies babble, they say things like GAGAGOOGOO or BABABABA. For the purposes of this question, we'll define a baby talk word to be any non-empty string of letters that can be divided into two equal-length portions in such a way that the first portion is identical to the second.

# Based on that definition, the following strings are words in baby talk: GAGA, GOOGOO, BABA, GUBBAGUBBA, DOGGIEDOGGIE, FDSFDS, IWANTMOREMILKIWANTMOREMILK, and XX.

# The following strings are not words in baby talk: BABAB, GAGOO, BA, DOGGIE, and X.

# Complete the baby_talk function to find the longest substring consisting of baby talk, as defined above, and return that length. In the test cases below, the longest baby talk string in each input string is underlined.


def baby_talk(s):
    max_length = 0
    for i, letter in enumerate(s):
        for j in range(1, len(s) // 2 + 1):
            if s[i: j + i] == s[j + i:j + (j + i)]:
                max_length = max(max_length, j * 2)
    return max_length


# OR


def baby_talk(s):
    longest = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring_length = j - i + 1

            if substring_length % 2 == 0:
                first_half = s[i : i + substring_length // 2]
                second_half = s[i + substring_length // 2:j + 1]
                if first_half == second_half:
                    longest = max(longest, substring_length)
    return longest


# Node implementation for a singly-linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Singly Linked List implementation


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def printList(self):
        pointer = self.head

        while pointer != None:
            print(pointer.data, end="-->")
            pointer = pointer.next

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print("TODO: Implement add with the tail")

    # OR

    # def add(self, data):
    #     if self.head == None:
    #         self.head = Node(data)
    #         self.tail = self.head
    #     else:
    #         self.tail.next = Node(data)
    #         self.tail = self.tail.next

    def size(self):
        count = 0
        pointer = self.head
        while pointer != None:
            pointer = pointer.next
            count += 1
        print("TODO: Implement size function that prints size of Linked List")
        print(count)

    def delete_second_to_last(self):
        if self.head is None:
            return
        prev = None
        current = self.head

        while current.next.next is not None:
            prev = current
            current = current.next

        prev.next = current.next
        self.tail = prev

        print("TODO: Implement the code to delete the second to last node")


if __name__ == "__main__":
    list = LinkedList()
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)

    list.size()

    # When called for this list, the output should be 1->2->4->
    list.delete_second_to_last()

    list.printList()

# Complete the function below to count the number of "H"s followed by "A"s in a string.
# The "A" does not have to immediately follow the "H".
# "HXAXHXA"	2
# "HHHHHAAAAA"	1
# O(n) time complexity


def count_letters(string):
    ha_count = 0
    on_h = False

    for i in string:
        if i == "H":
            on_h = True

        if i == "A" and on_h == True:
            ha_count = ha_count + 1
            on_h = False

    return ha_count


# Complete the function below to count the number of "HACK"s in a string. The letters do not
# have to immediately follow one another.
# "HHHAAACCCKKK"	1
# "HXACXKXXHACXK"	2
# O(n) time complexity


def count_letters(string):
    word_search = "HACK"
    word_index = 0

    hack_count = 0
    for char in string:
        if word_search[word_index] == char:
            word_index = word_index + 1

            # If word_index == length of hack, we read hack once
            if word_index == 4:
                hack_count = hack_count + 1
                word_index = 0

    return hack_count


# Nodes and links


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.links = []

    def link_node(self, node):
        self.links.append(node)


# Trees


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)


# Binary Search Tree


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Searching a binary tree


def binary_tree_search(node, target):
    if node is None or target == node.value:
        return node
    if target < node.value:
        return binary_tree_search(node.left, target)
    else:
        return binary_tree_search(node.right, target)


# Inserting into a BST


def binary_tree_insert(node, insert_value):
    if insert_value < node.value:
        if node.left is None:
            new_node = BinarySearchTreeNode(insert_value)
            node.left = new_node
        else:
            binary_tree_insert(node.left, insert_value)
    elif insert_value > node.value:
        if node.right is None:
            new_node = BinarySearchTreeNode(insert_value)
            node.right = new_node
        else:
            binary_tree_insert(node.right, insert_value)


# Deleting from a BST (look thru online resources)


# MERGE SORT


# Merge lists in a way that sorts them as well
def merge(left, right):
    leftIndex = 0
    rightIndex = 0
    sortedList = []

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            sortedList.append(left[leftIndex])
            leftIndex = leftIndex + 1
        else:
            sortedList.append(right[rightIndex])
            rightIndex = rightIndex + 1

    # Append the remaining items into sortedList
    if leftIndex < len(left):
        while leftIndex < len(left):
            sortedList.append(left[leftIndex])
            leftIndex = leftIndex + 1
    elif rightIndex < len(right):
        while rightIndex < len(right):
            sortedList.append(right[rightIndex])
            rightIndex = rightIndex + 1

    return sortedList


# Recursively break lists to individual lists
def mergeSort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])

    # returns the sorted merged left and right
    return merge(left, right)


if __name__ == "__main__":
    print(mergeSort([4, 1, 5, 9, 2, 6, 7]))
    # print(mergeSort([3, 7, 1, 4, 2, 6]))
