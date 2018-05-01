def parse():
    inp = open("linreg.txt", "r")
    out = open("out.csv", "w")
    for line in inp:
        data = line.strip().split(" ")
        out.write(data[0] + ";" + data[1] + "\n")
    inp.close()
    out.close()
