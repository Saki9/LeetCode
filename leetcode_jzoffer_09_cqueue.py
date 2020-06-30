class CQueue:
    """
    @titile 剑指 Offer 09. 用两个栈实现队列

    创建两个栈，一个用于append，当执行delete时如果另一栈为空，
    将该栈所有元素弹出到另一个栈，并从另一个栈弹出返回值

    |   | |   |    |   | |   |    |   | |   |
    | 2 | |   | -> |   | | 5 | -> |   | |   |
    |_5_| |___|    |___| |_2_|    |___| |_2_|
    """

    def __init__(self):
        self.stack_l = []
        self.stack_r = []

    def appendTail(self, value: int) -> None:
        self.stack_l.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_l) == 0 and len(self.stack_r) == 0:
            return -1

        if len(self.stack_r) == 0:
            for i in range(len(self.stack_l)):
                self.stack_r.append(self.stack_l.pop(-1))

        return self.stack_r.pop(-1)


queue = CQueue()
print(queue.deleteHead())
queue.appendTail(5)
queue.appendTail(2)
print(queue.deleteHead())
print(queue.deleteHead())
