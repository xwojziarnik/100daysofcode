"""Posortuj dwie linked listy"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        tail = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1, tail = list1.next, list1
            else:
                tail.next = list2
                list2, tail = list2.next, list2

        if list1 or list2:
            tail.next = list1 if list1 else list2

        return head.next
