#FILENAME = "seq.dat"
FILENAME = "seq_long.dat"


def readfile(filename):
    try:
        with open(filename) as myfile:
            file = myfile.readlines()
        return file
    except OSError as error:
        print(f"Whoops we have a problem in here\n{error}")
        exit(0)


def main():
    file = readfile(FILENAME)
    sequence_no = 1
    for lines in file:
        counter = 1
        elements = lines.split(" ")
        elements[-1] = elements[-1].replace("\n", "")
        k = len(elements)
        for i in range(k-1):
            if int(elements[i]) % 2 == 0:
                if int(elements[i]) / 2 == int(elements[i+1]):
                    counter = counter + 1
            else:
                if (3 * int(elements[i])) + 1 == int(elements[i + 1]):
                    counter = counter + 1
        if counter == k:
            print(f"Sequence {sequence_no} a munodi sequence (lenght {k})")
        else:
            print(f"Sequence {sequence_no} not a munodi sequence (lenght {k})")
        sequence_no = sequence_no + 1


if __name__ == '__main__':
    main()
