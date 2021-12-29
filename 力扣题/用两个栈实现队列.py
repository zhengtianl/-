'''
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
'''

class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendtail(self, value: int) -> None:
        self.A.append(value)

    def deletehead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())  # 加入a的倒序
        return self.B.pop()
