#!/usr/bin/env python3

import math

def switch(input_shape):
    if input_shape == "triangle":
        base = float(input("Give base of the triangle: "))
        height = float(input("Give height of the triangle: "))
        area = 0.5 * base * height

    elif input_shape == "rectangle":
        height = float(input("Give height of the rectangle: "))
        width = float(input("Give width of the rectangle: "))
        area = height * width

    elif input_shape == "circle":
        radius = float(input("Give radius of the circle: "))
        area = math.pi * radius ** 2  # Use math.pi for accurate calculation

    else:
        print("Unknown shape!")
        return
    
    print(f"The area is {area:.12f}")  

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        switch(shape)

if __name__ == "__main__":
    main()
