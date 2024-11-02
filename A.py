import sys
from random import randint


def Hi():
    print("Hi")


def GetRandom():
    print(randint(-sys.maxsize, sys.maxsize))


def Shutdown():
    sys.exit()


if __name__ == "__main__":
    func_dict = {
        "Hi": Hi,
        "GetRandom": GetRandom,
        "Shutdown": Shutdown,
    }
    while True:
        command = input()
        try:
            func_dict[command]()
        except KeyError:
            continue
