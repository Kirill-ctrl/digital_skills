class IteratorFibonacci:
    def __init__(self, limit: int):
        self.digit = 1
        self.pr_digit = 0
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            self.pr_digit, self.digit = self.digit, self.pr_digit + self.digit
            return self.digit
        raise StopIteration


if __name__ == '__main__':
    f_iter_1 = IteratorFibonacci(100)
    for digit in f_iter_1:
        print(digit)
