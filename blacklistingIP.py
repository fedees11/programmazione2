import ipaddress
import random
import time
from collections import deque

# 1) Funzioni di conversione
def ipToInt(ip):
    return int(ipaddress.ip_address(ip))

def intToIp(n):
    return str(ipaddress.ip_address(n))

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None: return Node(key)
    if key < node.key: node.left = insert(node.left, key)
    elif key > node.key: node.right = insert(node.right, key)
    return node

def search(node, key):
    if node is None or node.key == key: return node is not None
    if key < node.key: return search(node.left, key)
    return search(node.right, key)

blacklist_ips = [f"192.168.1.{i}" for i in range(1, 1001)]
blacklist_ints = [ipToInt(ip) for ip in blacklist_ips]
random.shuffle(blacklist_ints)

root = None
for val in blacklist_ints:
    root = insert(root, val)

pacchetti = []
for i in range(10):
    pacchetti.append(f"192.168.1.{random.randint(1, 1000)}")
for i in range(10):
    pacchetti.append(f"192.168.2.{random.randint(1, 255)}")
random.shuffle(pacchetti)

queue = deque(pacchetti)

bloccati = 0
permessi = 0

print("--- Processamento Pacchetti ---")
while queue:
    ip = queue.popleft()
    ip_int = ipToInt(ip)
    if search(root, ip_int):
        print(f"IP {ip} -> BLOCCATO")
        bloccati += 1
    else:
        print(f"IP {ip} -> PERMESSO")
        permessi += 1

print(f"\n--- Riepilogo: {bloccati} Bloccati, {permessi} Permessi ---")

test_ip = ipToInt("192.168.1.500")

start = time.perf_counter()
for _ in range(10000): search(root, test_ip)
end_bst = time.perf_counter() - start

start = time.perf_counter()
for _ in range(10000): (test_ip in blacklist_ints)
end_list = time.perf_counter() - start

print(f"\nTempo ricerca BST (10k op): {end_bst:.5f}s")
print(f"Tempo ricerca Lista (10k op): {end_list:.5f}s")

if end_bst < end_list:
    print(f"Il BST è {end_list/end_bst:.2f} volte più veloce della lista.")
else:
    print(f"La lista è {end_bst/end_list:.2f} volte più veloce del BST.")