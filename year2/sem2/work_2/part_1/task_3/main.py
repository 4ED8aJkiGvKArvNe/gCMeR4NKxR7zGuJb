import sys
import argparse

def main():
    # create parser object
    parser = argparse.ArgumentParser();

    # add arguments
    parser.add_argument("parameter_a", type=int, help="First number")
    parser.add_argument("parameter_b", type=int, help="Second number")
    parser.add_argument("parameter_c", type=int, help="Third number")

    # parse arguments
    args = parser.parse_args()

    # print arguments
    print("Got numbers: %d, %d, %d" % (args.parameter_a, args.parameter_b, args.parameter_c))

    if can_be_triangle(args.parameter_a, args.parameter_b, args.parameter_c):
        print("The numbers can be sides of a triangle.")
    else:
        print("The numbers CANNOT be sides of a triangle.")

def can_be_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

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
