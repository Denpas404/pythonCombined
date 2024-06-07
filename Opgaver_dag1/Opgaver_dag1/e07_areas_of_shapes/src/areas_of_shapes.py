#!/usr/bin/env python3

import math

def switch(input_shape):
    if input_shape == "triangle":
        base = float(input("Give base of the triangle: "))
        height = float(input("Give height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area is {area}")               
    elif input_shape == "rectangle":
        width = float(input("Give width of the rectangle: "))
        height = float(input("Give height of the rectangle: "))
        area = width * height
        print(f"The area is {area}")
    elif input_shape == "circle":
        radius = float(input("Give radius of the circle: "))
        area = math.pi * radius ** 2
        print(f"The area is {area}")
    else:
        print("Unknown shape!")
    

def main():
    # enter you solution here
    endless = True
    while endless:
        input_sharpe = input("Choose a shape (triangle, rectangle, circle): ")  
        switch(input_sharpe)

if __name__ == "__main__":
    main()
