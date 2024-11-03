import sys
from random import randint


def Hi():
    # prints "Hi" on stdout
    print("Hi")


def GetRandom():
    # prints a random integer on stdout
    print(randint(-sys.maxsize, sys.maxsize))


def Shutdown():
    # terminates the program gracefully
    print("Program A has been terminated.")
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
