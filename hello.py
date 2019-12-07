import math

def area_of_circle(r):
    return math.pi * math.pow(r, 2)

def main():
    rad = input("Type in radius: ")
    x = area_of_circle(rad)
    print(x)

if __name__ == "__main__":
    main()

