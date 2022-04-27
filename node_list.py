class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def next(self, foo):
    #     self.next = ListNode(foo)


def make_special_list(python_list):
    tail = head = ListNode(python_list[0])
    for i in python_list[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head


special_list = make_special_list([1, 2, 3])

print(special_list.val)
print(special_list.next.val)
print(special_list.next.next.val)
assert special_list.val == 1
assert special_list.next.val == 2
assert special_list.next.next.val == 3