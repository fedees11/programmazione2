import random
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None

class LinkedList:
    def __init__(self): self.head = None
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def search(self, target):
        curr = self.head
        while curr:
            if curr.data == target: return True
            curr = curr.next
        return False

class BST:
    def __init__(self): self.root = None
    def insert(self, data):
        if not self.root: self.root = Node(data)
        else: self._insert(self.root, data)
    def _insert(self, node, data):
        if data < node.data:
            if node.left: self._insert(node.left, data)
            else: node.left = Node(data)
        else:
            if node.right: self._insert(node.right, data)
            else: node.right = Node(data)
    def search(self, target):
        return self._search(self.root, target)
    def _search(self, node, target):
        if not node: return False
        if node.data == target: return True
        return self._search(node.left, target) if target < node.data else self._search(node.right, target)

dati = [random.randint(1, 10000) for _ in range(1000)]
target = dati[499]

ll = LinkedList()
bst = BST()
for x in dati:
    ll.insert(x)
    bst.insert(x)

start = time.perf_counter()
ll.search(target)
tempo_ll = time.perf_counter() - start

start = time.perf_counter()
bst.search(target)
tempo_bst = time.perf_counter() - start

# 6) Risultati
print(f"Tempo LinkedList: {tempo_ll:.8f} s")
print(f"Tempo BST:        {tempo_bst:.8f} s")

if tempo_bst < tempo_ll:
    print(f"Il BST è {tempo_ll/tempo_bst:.2f} volte più veloce della LinkedList.")
else:
    print(f"La LinkedList è {tempo_bst/tempo_ll:.2f} volte più veloce del BST.")