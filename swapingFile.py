from ast import Store


def swappingFile():
    dataA=input("Please entre a file: ")
    dataB=input("Please entre a file: ")

    #opening the given file in read mode ('r') and storing it in variable file
    with open(dataA,'r') as data1:
        a=data1.read()
    with open(dataB,'r') as data2:
        b=data2.read()

    with open(dataA,'w') as data1:
        data1.write(b)
    with open(dataB,'w') as data2:
        data2.write(a)

swappingFile ()