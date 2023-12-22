'''
  Problema Merge Two Sorted Lists do site LeetCode feito em python.
  Link do problema: https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Nó fictício inicial
        dummy = ListNode()
        # Ponteiro atual
        current = dummy
        
        # Enquanto ambas as listas tiverem nós
        while list1 is not None and list2 is not None:
            # Compare os valores dos nós atuais de ambas as listas
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
                
        # Se ainda houver nós nas listas
        current.next = list1 if list1 else list2     
  
        return dummy.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged_list = Solution().mergeTwoLists(list1, list2)
# Printa cada um dos valores da linked list retornada
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
