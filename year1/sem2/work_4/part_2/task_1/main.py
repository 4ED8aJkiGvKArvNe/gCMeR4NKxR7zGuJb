import argparse

def main():
    parser = argparse.ArgumentParser();

    # first argument
    parser.add_argument('--shift', type=int, required=True, help='The number of positions to shift the list')

    # second argument
    parser.add_argument('--values', nargs='+', required=True, help='The list of values')

    # parse the arguments
    args = parser.parse_args()

    print("Initial list:", args.values);
    
    shifted_values = shift_list_with_slices(args.values, args.shift)

    print("Shifted list:", shifted_values)

def shift_list_with_slices(values: list, shift: int) -> list:
    return values[shift:] + values[:shift]

def shift_list(values: list, shift: int) -> list:
    shifted_values = []
    for i in range(len(values)):
        shifted_values.append(values[(i + shift) % len(values)])
    return shifted_values


if __name__ == '__main__':
    main()
