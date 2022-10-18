from dataclasses import dataclass


def deleteDuplicates(self, head):
    self.head = head
    self.next = None
    print(self.head)


deleteDuplicates([1,1,2,3,3])