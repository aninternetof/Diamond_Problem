import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build a diamond.')
    parser.add_argument('-n', '--number', type=int, default=5, help='Input number [default 5]')
    args = parser.parse_args()
    n = args.number
    print("Running diamond program with integer {}".format(n))
    rows = []

    for row in list(range(n)):
        if row == 0:
            rows.append('*' * (n - 1) + str(n) + '*' * (n-1)) 
        else:
            num_out = n - 1 - row
            num_in = 2 * row -1
            rows.append('*' * num_out + str(n) + '*' * num_in + str(n) + '*' * num_out)

    
    for row in rows:
        print(row)

    for row in list(reversed(rows))[1:]:
        print(row)
