class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max = [0,]

    def Push(self, a):
        if a >= self.__max[len(self.__max)-1]:
            self.__max.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if(self.__stack.pop() == self.__max[len(self.__max)-1]):
            self.__max.pop()

    def Max(self):
        #print(self.__max, len(self.__stack)-1)
        return self.__max[len(self.__max)-1]


if __name__ == '__main__':
    stack = StackWithMax()
    num_queries = int(input())
    queries =[]
    for i in range(num_queries):
        queries.append([j for j in input().split()])
    for query in queries:
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
