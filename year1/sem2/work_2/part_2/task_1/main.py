import math
import sys
from typing import List, Tuple

Value = Tuple[float, float]
ValueList = List[Value]

def main():
    print("Enter numbers:")

    _a = input("a: ")
    a = validate_input(_a)

    _b = input("b: ")
    b = validate_input(_b)

    _c = input("c: ")
    c = validate_input(_c)

    _start = input("start: ")
    start = validate_input(_start)

    _end = input("end: ")
    end = validate_input(_end)

    # validate the end number to be greater than the start number
    if end < start:
        print("End number must be greater than the start number.")
        sys.exit(1)

    _step = input("step: ")
    step = validate_input(_step)

    # validate the step number to be greater than 0
    if step <= 0:
        print("Step number must be greater than 0.")
        sys.exit(1)

    f_x_max, f_x_list = calculate_range(a, b, c, start, end, step)

    # print function values
    for x, f_x in f_x_list:
        print("f(%.2f) = %.2f" % (x, f_x))

    # find and print the average value of the function
    average = find_average(f_x_list)
    print("Average value of the function: %.2f" % average)

    # find and print the average deviation from the maximum value
    average_deviation = find_average_deviation(f_x_list, f_x_max)
    print("Average deviation from the maximum value: %.2f" % average_deviation)

def find_average(f_x_list: ValueList) -> float:
    return sum([x[1] for x in f_x_list]) / len(f_x_list)

def find_average_deviation(f_x_list: ValueList, f_x_max: float) -> float:
    return sum([abs(x[1] - f_x_max) for x in f_x_list]) / len(f_x_list)
    
def calculate_range(a: float, b: float, c: float, start: float, end: float, step: float) -> Tuple[float, ValueList]:
    # maximum value of the function
    f_x_max = -math.inf

    # list of function values
    f_x_list = []

    x = start
    while(x <= end):
        f_x = calculate_value(a, b, c, x)
        
        f_x_list.append([x, f_x])

        if f_x > f_x_max:
            f_x_max = f_x
        
        # increment x by step
        x += step

    return f_x_max, f_x_list

def calculate_value(a: float, b: float, c: float, x: float) -> float:
    try:
        if (x + c < 0 and a != 0):
            return func_1(a, b, x)
        elif (x + c > 0 and a == 0):
            return func_2(a, c, x)
        else:
            return func_3(c, x)
    except ZeroDivisionError:
        return math.inf

def func_1(a: float, b: float, x: float) -> float:
    return -a * x**3 - b

def func_2(a: float, c: float, x: float) -> float:
    return (x - a) / (x - c)

def func_3(c: float, x: float) -> float:
    return x / c + c / x

def validate_input(x: any) -> float:
    if not is_number(x):
        print("Invalid input. Must be a number.")
        sys.exit(1)
    return float(x)

def is_number(x) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    main()
