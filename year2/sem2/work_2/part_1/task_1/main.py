import math

def main():
    print('Enter a number:');
    user_input = input();

    try:
        r = float(user_input);
    except ValueError:
        print('The input is not a number.');
        return;

    if (r >= 2 and r <= 4):
        m = func_1(r);
    elif (r > 4):
        m = func_2(r)
    else:
        m = func_3(r);

    print('Result:', m);

def func_1(r):
    return r**3 + r + 0.5;

def func_2(r):
    return 2.2 * 10**(-4) * r - math.sin(r);

def func_3(r):
    return (r + math.cos(r)) / (math.pi + r);

if __name__ == '__main__':
    main()
