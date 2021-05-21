class ConsoleIterator:
    def __init__(self):
        self.stored_numbs = []
        self.no_error = True

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.stored_numbs:
                return self.stored_numbs.pop(0)
            elif self.no_error:
                current_numbs = input().split()
                for item in current_numbs:
                    try:
                        self.stored_numbs.append(float(item))
                    except (ValueError, KeyboardInterrupt):
                        self.no_error = False
            else:
                raise StopIteration


def test():
    total_sum = 0

    for number in ConsoleIterator():
        total_sum = total_sum + number

    print(f'Sum of entered numbers is {total_sum}')


if __name__ == '__main__':
    test()
