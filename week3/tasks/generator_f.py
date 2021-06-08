def gen_fibonacci(limit, pr_digit=0, digit=1):
    while limit > 0:
        pr_digit, digit = digit, pr_digit + digit
        limit -= 1
        yield digit


if __name__ == '__main__':
    gen_iter = gen_fibonacci(limit=10)
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
