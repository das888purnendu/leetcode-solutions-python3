# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, n):
        n1 = ListNode(n)
        if self.head is None:
            self.head = n1
            return
        end = self.head
        while (end.next):
            end = end.next
        end.next = n1
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp1=l1
        tmp2=l2
        l3=LinkedList()
        
        ln=0
        
        while True:
            if(tmp1 is not None):
                if(tmp2 is not None):
                    if(tmp1.val>tmp2.val):
                        l3.insert(tmp2.val)
                        l3.insert(tmp1.val)
                        ln+=2
                    else:
                        l3.insert(tmp1.val)
                        l3.insert(tmp2.val)
                        ln+=2
                            
                    tmp1=tmp1.next
                    tmp2=tmp2.next
                    
                else:
                    l3.insert(tmp1.val)
                    tmp1=tmp1.next
                    ln+=1
                    
            elif(tmp2 is not None):
                l3.insert(tmp2.val)
                tmp2=tmp2.next
                ln+=1
                
            if(tmp1 is None and tmp2 is None):
                break
                
                
        # Bubble Sort
        if(l3.head and ln>2):
            tmp=l3.head
            for i in range(ln):
                tmp=l3.head
                for j in range(ln-i-1):
                    if tmp.val > tmp.next.val:
                        tmp.val,tmp.next.val=tmp.next.val,tmp.val
                    tmp=tmp.next
        return l3.head
