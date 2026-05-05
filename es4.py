from collections import deque

class Coda:
    
    def __init__(self):
        self.__data = deque()

    def enqueue(self, elemento):
        self.__data.append(elemento)

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Impossibile eseguire dequeue: la coda è vuota")
        return self.__data.popleft()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Impossibile eseguire peek: la coda è vuota")
        return self.__data[0]

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Coda({list(self.__data)})"