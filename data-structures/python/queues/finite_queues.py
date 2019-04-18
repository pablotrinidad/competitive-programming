class Queue:

    def __init__(self, n):
        self.size = n
        self.data = [None] * (n + 1)
        self.head = 0
        self.tail = 0

    def __plus_one(self, pointer):
        return (pointer + 1) % (self.size + 1)

    def __is_empty(self):
        return self.head == self.tail

    def __is_full(self):
        return self.__plus_one(self.tail) == self.head

    def enqueue(self, e):
        if self.__is_full():
            raise Exception('Queue overflowed')
        self.data[self.tail] = e
        self.tail = self.__plus_one(self.tail)

    def dequeue(self):
        if self.__is_empty():
            raise Exception('Queue underflowed')
        e = self.data[self.head]
        self.head = self.__plus_one(self.head)
        return e
