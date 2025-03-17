class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # push
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() is False:
            return self.items.pop()
        print('Stack пустой')
        return None

    def peek(self):
        if self.is_empty() is False:
            return self.items[-1]
        print('Stack пустой')
        return None

brackets = "()()(())()()"
marked = [0] * len(brackets)

# for bracket in brackets:
#     marked.append(0)

# 1 реализация
for i in range(0, len(brackets)):
    bracket = brackets[i]
    if marked[i] == 0 and bracket == '(':
        marked[i] = 1
        for j in range(i + 1, len(brackets)):
            if marked[j] == 0 and brackets[j] == ')':
                marked[j] = 1
                break

if marked.__contains__(0):
    print('Not valid')
else:
    print('Valid')


stack = Stack()

for bracket in brackets:
    if bracket == ')' and stack.peek() == '(':
        stack.pop()
        continue
    if bracket == '}' and stack.peek() == '{':
        stack.pop()
        continue
    stack.push(bracket)

if stack.is_empty():
    print('Valid')
else:
    print('Not valid')

