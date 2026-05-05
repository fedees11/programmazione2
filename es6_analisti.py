from es6 import CircularLinkedList

def gestione_turni_sicurezza():
    team = CircularLinkedList()

    team.insertLast("alice")
    team.insertLast("bob")
    team.insertLast("carlo")

    print(f"2. Team iniziale: {team}")

    print("3. Rotazione turni (6 passi):")
    team.traverse(6)

    print("\n4. Diana entra nel team dopo Bob.")
    team.insertAfter("bob", "diana")

    print(f"5. Team aggiornato: {team}")

    print("6. Rotazione turni con Diana (8 passi):")
    team.traverse(8)

    print("\n7. Bob lascia il team.")
    team.remove("bob")

    print(f"8. Team finale: {team}")

    print("9. Rotazione turni finale (6 passi):")
    team.traverse(6)

    print(f"\n10. Numero totale analisti: {team.size()}")

if __name__ == "__main__":
    gestione_turni_sicurezza()