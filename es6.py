class NodoC:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None

class CircularLinkedList:
    def __init__(self):
        self.__testa = None
        self.__coda  = None
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__testa     = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.insertFirst(valore)
            return
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__coda      = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        corrente = self.__testa
        while True:
            if corrente.valore == valore_riferimento:
                if corrente == self.__coda:
                    self.insertLast(nuovo_valore)
                    return
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
            if corrente == self.__testa:
                break
        raise ValueError(f"{valore_riferimento} non trovato")

    def remove(self, valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore:
            self.removeFirst()
            return
        corrente = self.__testa
        while corrente.next != self.__testa:
            if corrente.next.valore == valore:
                if corrente.next == self.__coda:
                    self.__coda = corrente
                corrente.next = corrente.next.next
                self.__size -= 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore} non trovato")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        valore = self.__testa.valore
        if self.__testa == self.__coda:
            self.__testa = self.__coda = None
        else:
            self.__testa = self.__testa.next
            self.__coda.next = self.__testa
        self.__size -= 1
        return valore

    def traverse(self, passi):
        if self.isEmpty():
            print("Lista vuota")
            return
        corrente = self.__testa
        for i in range(passi):
            print(f"turno {i + 1}: {corrente.valore}")
            corrente = corrente.next

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        if self.isEmpty(): return "CircularLinkedList([])"
        res, corrente = [], self.__testa
        while True:
            res.append(str(corrente.valore))
            corrente = corrente.next
            if corrente == self.__testa: break
        return "CircularLinkedList([" + " → ".join(res) + " → ...])"