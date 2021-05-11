extraFile1 = open('Sample1.txt')
extraFile2 = open('Sample2.txt')

data_1 = extraFile1.read()
data_2 = extraFile2.read()

fileThree = open('extraFile1.txt', 'w')
fileFour = open('extraFile2.txt', 'w')

print('Original')
print('File 1: ' + data_1)
print('File 2: ' + data_2)


def swapData():
    fileThree.write(data_2)
    fileFour.write(data_1)
    print('Reversed')
    print('File 1: ' + data_2)
    print('File 2: ' + data_1)


swapData()