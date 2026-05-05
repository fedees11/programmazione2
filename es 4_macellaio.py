from es4 import Coda  

def simulazione_macellaio():
    fila = Coda()

    clienti = ["Mario", "Giulia", "Tonino", "Rosa"]
    for c in clienti:
        fila.enqueue(c)
    print(f"Fila iniziale: {fila}")

    primo_servito = fila.dequeue()
    print(f"Servo: {primo_servito}")

    fila.enqueue("Enzo")
    print("È arrivato Enzo.")

    print(f"Persone ancora in fila: {fila.size()}")

    print("\n--- CLIENTI RIMANENTI ---")
    while not fila.isEmpty():
        prossimo = fila.dequeue()
        print(f"Servo: {prossimo}")
    
    print("Tutti i clienti sono stati serviti. Il macellaio chiude!")

if __name__ == "__main__":
    simulazione_macellaio()