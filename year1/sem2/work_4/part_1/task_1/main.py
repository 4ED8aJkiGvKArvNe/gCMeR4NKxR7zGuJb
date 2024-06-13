import argparse

def main():
    parser = argparse.ArgumentParser();

    # expect list of values
    parser.add_argument('--values', nargs='+', required=True, help='The list of values')

    # parse the arguments
    args = parser.parse_args()

    print("All values:", args.values)

    unique_values = find_unique(args.values)
    
    print('Unique values:', unique_values)

def find_unique_with_set(values: list) -> list:
    return list(set(values))

def find_unique(values: list) -> list:
    unique_values = []
    for value in values:
        if value not in unique_values:
            unique_values.append(value)
    return unique_values

if __name__ == '__main__':
    main()
