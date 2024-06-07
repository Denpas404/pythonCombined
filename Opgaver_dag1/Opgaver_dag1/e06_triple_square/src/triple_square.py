#!/usr/bin/env python3
def triple(num):
    return num * 3

def square(num):
    return num ** 2

def main():
    pass
    for i in range(1, 11):
        squared = square(i)
        tripled = triple(i)

        if squared > tripled:
            break

        print(f"triple({i})=={tripled} square({i})=={squared}")
    
if __name__ == "__main__":
    main()
