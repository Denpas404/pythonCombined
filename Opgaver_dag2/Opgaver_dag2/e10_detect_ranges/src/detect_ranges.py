#!/usr/bin/env python3

def detect_ranges(L):
    sortedList = sorted(L)
    result = []
    i = 0
    while i < len(sortedList): 
        start = sortedList[i] 
        end = sortedList[i] 
        
        while i + 1 < len(sortedList) and sortedList[i] + 1 == sortedList[i + 1]: 
            end = sortedList[i + 1]
            i += 1
        if start == end:
            result.append(start,)
        else:
            result.append((start, end + 1))
        i += 1
        

    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
