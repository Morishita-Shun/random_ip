import sys
import os
import random


DATA_PATH = "/Users/user/Desktop/"


def main():
    input_name = ""
    num = 0

    if len(sys.argv) == 3:
        input_name = sys.argv[1]
        num = int(sys.argv[2])
    else:
        print("Enter input_name:")
        input_name = sys.stdin.readline().strip()
        print("Enter num:")
        num = int(sys.stdin.readline().strip())

    name, ext = os.path.splitext(input_name)
    name = name + '_' + str(num)
    out_name = ""
    c = 1
    while True:
        if os.path.isfile(DATA_PATH + name + '_' + str(c) + ext):
            c += 1
        else:
            out_name = name + '_' + str(c) + ext
            break

    lines = []
    with open(DATA_PATH + input_name, "r") as f:
        lines = f.readlines()
    length = len(lines)

    with open(DATA_PATH + out_name, "w") as f:
        pass

    for i in range(num):
        lists = []
        with open(DATA_PATH + out_name, "r") as f:
            lists = f.readlines()
        lists = list(map(str.strip, lists))

        while True:
            r = random.randint(0, length - 1)
            line = lines[r].strip()
            if line not in lists:
                with open(DATA_PATH + out_name, "a") as f:
                    f.write(line + "\n")
                break


if __name__ == "__main__":
    main()
