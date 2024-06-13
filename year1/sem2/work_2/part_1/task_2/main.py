import sys

def main():
    print("First rectangle")
    print("Enter coordinates of the left bottom corner:")
    x1 = input("x: ")
    validate_input(x1)
    y1 = input("y: ")
    validate_input(y1)
    w1 = input("width: ")
    validate_input(w1)
    h1 = input("height: ")
    validate_input(h1)
    
    print("Second rectangle")
    print("Enter coordinates of the left bottom corner:")
    x2 = input("x: ")
    validate_input(x2)
    y2 = input("y: ")
    validate_input(y2)
    w2 = input("width: ")
    validate_input(w2)
    h2 = input("height: ")
    validate_input(h2)

    rect1 = (float(x1), float(y1), float(w1), float(h1))
    rect2 = (float(x2), float(y2), float(w2), float(h2))

    if intersects(rect1, rect2):
        print("The rectangles intersect.")
    else:
        print("The rectangles do not intersect.")

    if contains(rect1, rect2):
        print("The first rectangle contains the second one.")
    elif contains(rect2, rect1):
        print("The second rectangle contains the first one.")

def contains(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return x1 <= x2 and y1 <= y2 and x1 + w1 >= x2 + w2 and y1 + h1 >= y2 + h2

def intersects(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2

def validate_input(x):
    if not is_number(x):
        print("Invalid input. Must be a number.")
        sys.exit(1)

def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    main()
