#!/usr/bin/env python3
def triple(num):
    return num * 3

def square(num):
    return num ** 2

def main():
    pass
for i in range(1, 11):
    if square(i) > triple(i):
        break
    else:
        print(f"triple({i})=={triple(i)}\tsquare({i})=={square(i)}")
    
if __name__ == "__main__":
    main()
