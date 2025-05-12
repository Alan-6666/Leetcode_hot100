"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
 

示例 1:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
 

提示：

-231 <= val <= 231 - 1
pop、top 和 getMin 操作总是在 非空栈 上调用
push, pop, top, and getMin最多被调用 3 * 104 次
"""

class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = [] #是一个辅助栈，存储当前栈的最小值，常数返回最小元素

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.min_st.append(val)
        else:
            self.st.append(val)
            self.min_st.append(min(val, self.min_st[-1]))
        
    def pop(self) -> None:
        res = self.st[-1]

        self.st = self.st[:-1]
        self.min_st = self.min_st[:-1]
        return res

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.min_st[-1]
        