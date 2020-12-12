import argparse
import sys
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--surname', type=str, required=True)
    parser.add_argument('--middle_name', type=str, default=None, required=False)
    parser.add_argument('--age', type=int, required=True)
    parser.add_argument('--sex', type=str, required=True, choices=["M", "F"])
    parser.add_argument('--married', required=False, default=False, action='store_true')
    parser.add_argument('--hobbies', default=None, required=False, nargs='*')

    args = parser.parse_args(sys.argv[1:])

    if not os.path.isfile("journal.txt"):
        with open("journal.txt", "w") as f:
            f.write(str(args.__dict__) + '\n')
    else:
        with open("journal.txt", "a") as f:
            f.write(str(args.__dict__) + '\n')
