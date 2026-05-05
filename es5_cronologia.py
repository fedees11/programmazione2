from es5 import LinkedList

def gestisci_cronologia():
    cronologia = LinkedList()

    cronologia.insertLast("admin")
    cronologia.insertLast("mario")
    cronologia.insertLast("sara")

    print(f"Punto 2: {cronologia}")

    cronologia.insertAfter("mario", "guest")

    print(f"Punto 4: {cronologia}")

    cronologia.insertBefore("admin", "root")

    print(f"Punto 6: {cronologia}")

    cronologia.insertBefore("sara", "luca")

    print(f"Punto 8: {cronologia}")

    cronologia.removeFirst()

    print(f"Punto 10: {cronologia}")

    cronologia.removeLast()

    print(f"Punto 12: {cronologia}")

    print(f"Punto 13 - Numero modifiche: {cronologia.size()}")

    print(f"Punto 14 - Modifica più recente: {cronologia.peekFirst()}")

if __name__ == "__main__":
    gestisci_cronologia()