# Question: Merge Two Sorted Lists
# Description:
# You are given the heads of two sorted linked lists, list1 and list2. Merge the two lists into one sorted list. Return the merged list.

# Example:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Create a dummy node to serve as the start of the merged list
    dummy = ListNode(-1)
    current = dummy  # Pointer to track the current node in the merged list
    
    # Traverse both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next  # Move to the next node in list1
        else:
            current.next = list2
            list2 = list2.next  # Move to the next node in list2
        current = current.next  # Move the pointer in the merged list
    
    # Append the remaining nodes of the non-empty list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    # Return the head of the merged list
    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode(-1)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example Usage
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

merged_list = mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]
    