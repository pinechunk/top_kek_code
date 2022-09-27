# 1. push(item), добавляющий элемент на вершину стека

# 2. pop(), удаляющий самый верхний элемент стека и возвращающий его.

# Если в стеке нет элементов, метод должен выбросить ошибку или вернуть null.

# 3. max(), возвращающий максимальное значение в стеке на данный момент.
# Если в стеке нет элементов, метод должен выбросить ошибку или вернуть null.

# Каждый метод должен иметь постоянную временную сложность.

class Stack:
    def __init__(self):
        self.stack = []
        self.max = None

    def push(self, item):
        self.stack.append(item)
        if len(self.stack) == 1 or item > self.max:
            self.max = item

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        if len(self.stack) == 0:
            self.max = None
        elif removed == self.max:
            self.max = self.stack[0]
            for value in self.stack:
                if value > self.max:
                    self.max = value
        return removed

    def get_max(self):
        return self.max

s = Stack()
s.push(199)
s.push(27)
s.push(35)
print(s.stack)
s.pop()
print(s.max)
