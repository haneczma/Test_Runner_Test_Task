from subprocess import PIPE, Popen


def SendCommand(p, cmd_name: str) -> str:
    # sends command name to open process and returns stdout of that process
    p.stdin.write(cmd_name + "\n")
    p.stdin.flush()
    response = p.stdout.readline()
    return response.strip()


if __name__ == "__main__":
    # open program A as a process
    p = Popen(["python", "-u", "A.py"], stdin=PIPE, stdout=PIPE, text=True)
    # verify if Hi commannd gives a correct response
    response = SendCommand(p, "Hi")
    if response != "Hi":
        raise AssertionError("Program A does not give the correct response.")
    else:
        print("Program A gives a correct response.")
    # retrive 100 random integers
    random_data = list()
    for i in range(0, 100):
        random_data.append(int(SendCommand(p, "GetRandom")))
    # terminate program A gracefully
    print(SendCommand(p, "Shutdown"))
    # sort and print retrieved data
    random_data.sort()
    print(random_data)
    # calculate and print median and average
    median = (random_data[49] + random_data[50]) / 2
    average = sum(random_data) / 100
    print(median)
    print(average)
