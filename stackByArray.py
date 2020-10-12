# coding:utf-8

class Stack(object):
    # 初始化栈
    def __init__(self,x):
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
    def pop(self, item):
        return self.items.pop()
