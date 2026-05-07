import random
import time
from es5_cronologia import LinkedList
from es7 import BST

def benchmark():
    numeri = [random.randint(1, 10000) for _ in range(1000)]

    lista = LinkedList()
    albero = BST()
    for n in numeri:
        lista.insertLast(n)
        albero.insert(n)

    target = numeri[499]
    print(f"--- Benchmark Ricerca: {target} ---")

    start_ll = time.perf_counter()
    corrente = lista._LinkedList__testa 
    while corrente:
        if corrente.valore == target: break
        corrente = corrente.next
    end_ll = time.perf_counter()
    tempo_ll = end_ll - start_ll

    start_bst = time.perf_counter()
    albero.search(target)
    end_bst = time.perf_counter()
    tempo_bst = end_bst - start_bst

    print(f"Tempo LinkedList: {tempo_ll:.8f} s")
    print(f"Tempo BST:        {tempo_bst:.8f} s")
    
    if tempo_bst > 0:
        print(f"\nIl BST è {int(tempo_ll/tempo_bst)} volte più veloce!")

if __name__ == "__main__":
    benchmark()