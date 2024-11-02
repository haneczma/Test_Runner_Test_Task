from subprocess import PIPE, Popen

if __name__ == "__main__":
    p = Popen(["python", "-u", "A.py"], stdin=PIPE, stdout=PIPE, text=True)
    p.stdin.write("Hi\n")
    p.stdin.flush()
    response = p.stdout.readline()
    print(response.strip())
    random_data = list()
    for i in range(0, 100):
        p.stdin.write("GetRandom\n")
        p.stdin.flush()
        response = p.stdout.readline()
        random_data.append(int(response))
    p.stdin.write("Shutdown\n")
    p.stdin.flush()
