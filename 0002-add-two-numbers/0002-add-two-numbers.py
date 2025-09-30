# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2 
        result = ListNode()
        current= result
        carry = 0

        while head1 or head2 or carry:
            
            if head1:
                num1 = head1.val
            else: 
                num1= 0

            if head2:
                num2= head2.val
            else:
                num2= 0

            sumVal= num1+ num2 + carry
            num = sumVal%10
            carry= sumVal//10
            current.next=ListNode(num)
            current=current.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        return result.next
