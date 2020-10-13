# coding:utf-8

class Stack(object):
    # 初始化栈
    def __init__(self):
        self.items=[]

    # 判断是否为空，为空返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items)-1]

    # 返回栈大小
    def size(self):
        return len(self.items)

    # 入栈
    def push(self, item):
        return self.items.append(item)

    # 出栈
    def pop(self):
        return self.items.pop()


if __name__ == "__main__":
    my_stack = Stack()          # 初始化实例
    my_stack.push('1')
    my_stack.push('2')
    print("1:",my_stack.size())
    print("2:",my_stack.peek())
    print("3:",my_stack.pop())
    print("4:",my_stack.peek())
    print("5:",my_stack.size())
    print("6:",my_stack.pop())
    print("7:",my_stack.size())
    print("8:",my_stack.is_empty())


