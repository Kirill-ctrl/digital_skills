def check_1():
    from module_1 import list_to_dict, strings_interspec, longest_ascending_seq

    print("\t", list_to_dict(['s', 's', 's', 2, 3, 4, 2, 4, 1, 5]))
    print("\t", strings_interspec("hello world, i am Kirill Pechurin, i live in Kazan",
                                  'hello, i am student. I am study in Kazan'))
    print("\t", longest_ascending_seq([1, 2, 3, 5, 6, 1, 7, 10, 6, 7, 8, 9, 10]))


def check_2():
    from module_1 import (list_to_dict, longest_ascending_seq, strings_interspec)

    print("\t", list_to_dict(["1", 2, 3, 5, hex(16), hex(16), bin(5), bin(2), 4, 2, 5]))
    print("\t", strings_interspec(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Duis et urna eget nulla rhoncus convallis. Aenean condimentum a ligula nec bibendum."
    ))
    print("\t", longest_ascending_seq([0, -1, -2, -5, -7, -10, 0]))


def check_3():
    import module_1
    arr_string = "Lorem Ipsum это текст - 'рыба' , часто используемый в печати и вэб-дизайне.".split()
    print("\t", module_1.list_to_dict([i for i in arr_string]))
    print("\t", module_1.strings_interspec("Python is easy to work with and easy to read",
                                           "Why we choose Python as a backend language"))
    print("\t", module_1.longest_ascending_seq([-6, -4, -2, 0, 1, 5, 8]))


if __name__ == '__main__':
    print("check 1: ")
    check_1()
    print("check 2: ")
    check_2()
    print("check 3: ")
    check_3()
