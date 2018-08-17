# coding=utf-8
# 散列表在python 中是字典
voted = {}


def check_voter(name):
    if voted.get(name):
        print("kick them out !")
    else:
        voted[name] = True
        print("let them vote!")


if __name__ == "__main__":
    check_voter("liu")
    check_voter("liu")
    check_voter("liu")
