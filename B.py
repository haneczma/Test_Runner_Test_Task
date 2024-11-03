from subprocess import PIPE, Popen


def SendCommand(cmd_name: str) -> str:
    p.stdin.write(cmd_name + "\n")
    p.stdin.flush()
    response = p.stdout.readline()
    return response.strip()


if __name__ == "__main__":
    # open program A as a process
    p = Popen(["python", "-u", "A.py"], stdin=PIPE, stdout=PIPE, text=True)
    # verify if Hi commannd gives a correct response
    response = SendCommand("Hi")
    if response != "Hi":
        raise AssertionError("Process A does not give the correct response.")
    # retrive 100 random integers
    random_data = list()
    for i in range(0, 100):
        random_data.append(int(SendCommand("GetRandom")))
    # terminate program A gracefully
    print(SendCommand("Shutdown"))
    # sort and print retrieved data
    random_data.sort()
    print(random_data)
    # calculate and print median and average
    median = (random_data[49] + random_data[50]) / 2
    average = sum(random_data) / 100
    print(median)
    print(average)
