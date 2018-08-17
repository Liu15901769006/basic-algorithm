# coding=utf-8


def fact(x):
    if x == 1:
        return 1
    else:
        t = fact(x-1)
        result = x * t
        return result


if __name__ == "__main__":
    print(fact(5))
