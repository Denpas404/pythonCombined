#!/usr/bin/env python3

# Funktionen distinct_characters tager en liste af strenge som input.
def distinct_characters(L):
    # Opret et tomt dictionary til at gemme resultatet.
    dic = {}
    # Gennemgå hver streng i inputlisten.
    for word in L: 
        # Brug sæt-containeren til midlertidigt at gemme de forskellige tegn i strengen, og find længden af dette sæt.
        # Sæt har unikke elementer, så antallet af elementer i sættet vil være antallet af forskellige tegn i strengen.
        dic[word] = len(set(word)) 
    # Returner det opdaterede dictionary med antallet af forskellige tegn for hver streng.
    return dic


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
