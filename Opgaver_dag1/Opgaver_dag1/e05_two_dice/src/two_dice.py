#!/usr/bin/env python3

def main():
    pass
    i = 1
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 5:
                print(f"({i},{j})")

if __name__ == "__main__":
    main()
