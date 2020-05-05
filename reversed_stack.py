class Stack :
    def __init__(self) :
        self.items = []

    def is_empty(self) :
        return self.items == []

    def push(self, data) :
        self.items.append(data)

    def pop(self) :
        return self.items.pop()

    def get_stack(self) :
        for data in reversed(self.items) :
            print(data)


def insertreverse(s, data) :
    if s.is_empty() :
        s.push(data)
    else :
        popped = s.pop()
        insertreverse(s, data)
        s.push(popped)


def reverse(s) :
    if not s.is_empty() :
        popped = s.pop()
        reverse(s)
        insertreverse(s, popped)


s = Stack()
data_list = input('insert elements of stack:').split()
for data in data_list :
    s.push(int(data))
reverse(s)
print('Reversed stack:')
s.get_stack()