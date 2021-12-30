import glob, os,json

def main():
    print("==menu==")
    print("1. mengubah ke json")
    print("2. mengubah ke txt")
    pilih = input("masukan pilihan = ")

    if pilih == "1":
        toJson()
    elif pilih =="2":
        toTxt()

def daftarFile():
    os.chdir("/var/log")
    for file in glob.glob("*.log"):
        print(file)
def toJson():
    dict1 = []
    print("kepada txt")
    daftarFile()
    inputFile = input("masukan nama file = ")

    with open(inputFile) as fh:
        for line in fh:
            description = line.strip()

            dict1.append(description)

        save_path = input("masukan directory = ")
        splitName = inputFile.split('.', 99)
        formalName = splitName[0] + ".json"

        output_save_path = os.path.join(save_path, formalName)

        out_file = open(output_save_path, "w")
        out_file.write(str(dict1))

        out_file.close()

    #creating txt file


def toTxt():
    dict1 = []
    print("kepada txt")
    daftarFile()
    inputFile = input("masukan nama file = ")

    # with open(inputFile) as fh:
    #     for line in fh:
    #         description = line.strip()
    #
    #         dict1.append(description)
    f = open(inputFile, 'r')

    save_path = input("masukan directory = ")
    splitName = inputFile.split('.', 99)
    formalName = splitName[0] + ".txt"

    output_save_path = os.path.join(save_path, formalName)

    out_file = open(output_save_path, "w")
    out_file.write(f.read())

    out_file.close()
if __name__ == '__main__':
    main()