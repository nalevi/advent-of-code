def main():

    file = open("input.txt","r")
    data = list()
    for line in file:
        data.append(int(line))

    file.close()

    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    print(str(i*j*k))
                    return


if __name__ == '__main__':
    main()