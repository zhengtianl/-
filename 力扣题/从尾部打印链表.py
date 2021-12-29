class Solution:
    '''
    递归解析：
终止条件： 当 head == None 时，代表越过了链表尾节点，则返回空列表；
递推工作： 访问下一节点 head.next ；
回溯阶段：
Python： 返回 当前 list + 当前节点值 [head.val] ；
'''
 #method 1
    def reverseprint(self, head: ListNode) -> List[int]:
        return self.reverseprint(head.next) + [head.val] if head else []
#method 2

    def reverseprint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
