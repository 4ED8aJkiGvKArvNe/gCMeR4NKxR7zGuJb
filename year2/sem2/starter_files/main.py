import sys

def main():
    print("Hello, world!")

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
