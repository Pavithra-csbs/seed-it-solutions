"""
Problem: Q2 - Add Reverse-Digit Lists Problem
Category: General
Difficulty: Medium
Platform: SEED-IT Platform (https://seed-it.com)
Date Solved: 2026-09-17
Language: python3
Test Cases: 30 / 30 Passed (100%)
"""

import sys, json

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry =0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1+val2+carry
            carry = total //10

            curr.next = ListNode(total%10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

if __name__ == '__main__':
    args = json.loads(sys.stdin.readline())
    l1_vals, l2_vals = args[0], args[1]
    def build(vals):
        head = None
        cur = None
        for v in vals:
            node = ListNode(v)
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = cur.next
        return head
    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out
    l1 = build(l1_vals)
    l2 = build(l2_vals)
    res = Solution().addTwoNumbers(l1, l2)
    print(json.dumps(to_list(res)))
