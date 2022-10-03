class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()

    def append(self, data):
        new_node=node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total += 1
            cur = cur.next
        return total

    def showList(self):
        seen = []
        cur_node = self.head
        while cur_node.next!=None:
            cur_node = cur_node.next
            seen.append(cur_node.data)
        print(seen)

list1 = linked_list()
list2 = linked_list()

list1.append(1)
list1.append(2)
list1.append(4)
list2.append(1)
list2.append(3)
list2.append(4)


def mergeTwoLists(list1, list2):
    if not list1: return list2
    if not list2: return list1
    
    current = dummy = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1: current.next = list1
    if list2: current.next = list2
        
    return dummy.next