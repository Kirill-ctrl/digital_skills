def gen_fibonacci(limit: int, pr_digit: int = 0, digit: int = 1):
    """Функция - генератор для чисел фибоначчи"""
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
