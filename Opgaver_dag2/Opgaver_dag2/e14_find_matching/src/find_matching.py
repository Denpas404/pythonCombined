#!/usr/bin/env python3

def find_matching(L, pattern):
    result = []

    for i, x in enumerate(L): # For hvert index og element i L 
        if pattern in x: # Hvis pattern er i x
            result.append(i) # Tilføj index til result       

    return result

def main():
    pass
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
