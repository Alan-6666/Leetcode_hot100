"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]
 
提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
 

"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#插入排序，超时
class Solution:
    def insertionSort(self, head: ListNode):
        #如果为空，或者只有一个链表则直接返回
        if not head or not head.next:
            return head
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        #已经排序好的节点
        sorted_list = head
        #当前待插入的节点
        cur = head.next 
        
        while cur:
            if sorted_list.val <= cur.val:
                #正好升序，无需移动
                sorted_list = sorted_list.next 
            else:
                #cur较小，需要插入到sorted_list前面
                prev = dummy_head
                #找到小于cur.val的节点
                while prev.next.val <= cur.val:
                    prev = prev.next
                #断开cur，sorted_list连接到cur.next
                sorted_list.next = cur.next
                #cur插入到prev之后
                cur.next = prev.next
                prev.next = cur
            #更新待判断节点
            cur = sorted_list.next 
        
        return dummy_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSort(head)

        