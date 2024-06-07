#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    for key in d: # For hver key i d
        for value in d[key]: # For hver value i d[key]
            if value in result: # Hvis value allerede er i result
                result[value].append(key) # Tilføj key til value
            else:
                result[value] = [key] # Ellers opret en ny key med value

    return result

def main():
    pass
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
