class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty()) # True
s.push(5)
s.push('hello')
print(s.peek()) # hello
s.push(True)
print(s.size()) # 3
print(s.isEmpty()) # False
s.push(500)
print(s.pop())
print(s.pop())
print(s.size())  # 2
# 使用for循环遍历打印列表中的值（即目前栈中元素）
for _ in range(s.size()):
    print(s.items[_], end=' ')
