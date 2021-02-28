class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def copy_values(self, set):
      head = self.head
      while head is not None:
        set.add(head.value)
        head = head.next


def union(llist_1, llist_2):
    # traverse each list and store unique values in union set
    union = set()
    for list in (llist_1, llist_2):
      list.copy_values(union)
    return union

def intersection(llist_1, llist_2):
    list_values_1 = set()
    list_values_2 = set()
    intersection = set()
    # if either list is empty there is no intersection 
    if llist_1.head is None or llist_2.head is None:
        return None

    head_1 = llist_1.head
    head_2 = llist_2.head
    # go over both lists at the same time until you reach the end of both lists
    while head_1 or head_2:
        if head_1:
          # if a node value in list is already in our list 2 bucket, it is part of the intersection
            if head_1.value in list_values_2:
                intersection.add(head_1.value)
          # add the node value to its own list 1 values bucket
            list_values_1.add(head_1.value)
            head_1 = head_1.next
        if head_2:
          # same as above, in reverse:
            if head_2.value in list_values_1:
                intersection.add(head_2.value)
            list_values_2.add(head_2.value)
            head_2 = head_2.next

    return intersection

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
