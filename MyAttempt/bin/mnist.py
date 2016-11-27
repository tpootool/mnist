import csv
import tensorflow as tf
import numpy as np
# mnist image dimensions are 28x28


def main():
    kernelWidth = 5 #int
    kernelHeight = 5 #int

    kernel = ([1,0,1,0,1], [0,1,0,1,0,1],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1])
    testK = [1,0,1,0,1]

    inputLayer = parseData()
    print len(inputLayer)
    layer = convLayerActivation(inputLayer)
    poolLayerActivation(layer)


def convLayerActivation(inputLayer):
    imageWidth = 28;
    kernel = (([1,0,1,0,1]),([1,0,1,0,1]),([1,0,1,0,1]),([1,0,1,0,1]),([1,0,1,0,1]))

    # Assumes input picture is a square
    convLayerLength = int(np.sqrt(len(inputLayer[0][0])-1)) -len(kernel) + 1

    print int(np.sqrt(len(inputLayer[0][0])-1)) -len(kernel) + 1

    convLayer = createLayer()

    # for label in inputLayer:
    #     for image in label:
    #
    print len(inputLayer)
    # for imageNumber in range(0, len(inputLayer)):
    #     convolvedImage = []
    #
    #     for convolvedRowNumber in range(0,convLayerLength):
    #         for convolvedColumnNumber in range(0,convLayerLength): # Convolve over a single 'row'
    #             # Convolve over a single receptive field
    #             convolvedUnit = 0.0
    #             for i in range (0, 5): # Kernel height/row
    #                 for j in range (0,5): # Kernel width/column
    #                     # Moves the kernel along the input layer
    #                     convolvedUnit += kernel[i][j] * inputLayer[imageNumber][((i+convolvedRowNumber)*imageWidth)+1+(j+convolvedColumnNumber)]
    #                     # print ((i*imageWidth)+convolvedRowNumber)+1+(j+convolvedColumnNumber)
    #             # convolvedImage.append(convolvedUnit)# Adds to the conv layer
    #             convolvedImage.append(normalize(convolvedUnit))# performs normalization and nonlinear function to convolved unit


    for index in xrange (0, len(inputLayer)):
        for image in inputLayer[index]:
            convolvedImage = []
            for convolvedRowNumber in range(0, convLayerLength):
                for convolvedColumnNumber in range(0, convLayerLength):  # Convolve over a single 'row'
                    # Convolve over a single receptive field
                    convolvedUnit = 0.0
                    for i in range(0, 5):  # Kernel height/row
                        for j in range(0, 5):  # Kernel width/column
                            # Moves the kernel along the input layer
                            convolvedUnit += kernel[i][j] * image[((i + convolvedRowNumber) * imageWidth) + (j + convolvedColumnNumber)]
                            # convolvedUnit += kernel[i][j] * inputLayer[imageNumber][((i + convolvedRowNumber) * imageWidth) + 1 + (j + convolvedColumnNumber)]
                            # print ((i*imageWidth)+convolvedRowNumber)+1+(j+convolvedColumnNumber)
                    # convolvedImage.append(convolvedUnit)# Adds to the conv layer
                    convolvedImage.append(normalize(convolvedUnit))  # performs normalization and nonlinear function to convolved unit





        # print index
            convLayer[index].append(convolvedImage)
    print "good so far"
    # print inputLayer[imageNumber][0]
    return convLayer

def poolLayerActivation(inputLayer):
    poolHeight = 2
    poolWidth = 2
    poolWindow = []
    # poolWindow = np.array([])
    # poolLayer = np.array([]))
    poolLayer = []

    imageLength = int(np.sqrt(len(inputLayer[0][0])))


    # print len(inputLayer)

    createLayer()
    for label in inputLayer:
        for image in label:



            print np.sqrt(image)
            # Assumes image is a square
            for row in range (0, imageLength/poolHeight):
                for column in range (0, imageLength/poolWidth):
                    for i in range (0,poolWidth):
                        for j in range(0, poolHeight):
                            poolWindow.append(image[((i+(row*poolHeight))*imageLength)+(j+(column*poolWidth))])

                    print poolWindow
                    poolLayer.append(np.maximum(poolWindow))
                    print poolLayer[-1]



    print len(poolLayer)

def parseData():
    inputLayer = createLayer()

    i = 0
    with open('resources/mnist_train.csv', 'rb') as csvfile:
        dataSet = csv.reader(csvfile, delimiter=',', quotechar='|')
        # row = np.array([])
        row = []
        # Parse string values for numbers into int types
        for line in csvfile:
            row = line.split(",")
            image = []
            for unit in xrange (len(row)-1):
            # for unit in row:
                # image = np.append(image, unit.astype(np.int))
                # image = np.append(image, int(unit))
                image.append(int(row[unit+1]))
            # numRow = np.array([])
            # for unit in rows[-1]:
                # numRow = np.append(numRow, int(unit))
                # print int(unit)

            # inputLayer = np.append(inputLayer, row.astype(np.int))


            inputLayer[image[0]].append(image)
            print len(image)
            # inputLayer.append(image)
            # i +=1
            # if (i % 100 == 0):
            #     print len(inputLayer)

                # print len(inputLayer)

        # print len(inputLayer)
            # inputLayer = np.append(inputLayer, numRow)

    # print "Parse test"
    # print len(inputLayer[0])
    # print len(inputLayer)

    # total = 0
    # for index in inputLayer:
    #     print len(index)
    #     total += len(index)
    # print total


    return inputLayer

#
# def parseData():
#     inputLayer = np.empty([0,785])
#     i = 0
#     with open('resources/mnist_train.csv', 'rb') as csvfile:
#         dataSet = csv.reader(csvfile, delimiter=',', quotechar='|')
#         # row = np.array([])
#         row = np.array([])
#         # Parse string values for numbers into int types
#         for line in csvfile:
#             row = line.split(",")
#             image = np.array([])
#             for unit in row:
#                 # image = np.append(image, unit.astype(np.int))
#                 # image = np.append(image, int(unit))
#                 image = np.append(image, int(unit))
#             # numRow = np.array([])
#             # for unit in rows[-1]:
#                 # numRow = np.append(numRow, int(unit))
#                 # print int(unit)
#
#             # inputLayer = np.append(inputLayer, row.astype(np.int))
#
#             # inputLayer = np.vstack((inputLayer, image))
#                 inputLayer = np.vstack((inputLayer, image))
#             # inputLayer = np.append(inputLayer, image)
#             if (i % 1000 == 0):
#                 # print len(inputLayer)
#                 print type(inputLayer[-1])
#             i +=1
#             # if (i % 100 == 0):
#             #     print len(inputLayer)
#
#                 # print len(inputLayer)
#
#         # print len(inputLayer)
#             # inputLayer = np.append(inputLayer, numRow)
#
#     print len(inputLayer)
#
#
#
#     return inputLayer





def normalize(input):
    return (input-128)/128

def reLU(input):
    return np.maximum(0,input)

def createLayer():
    numberDimension = []
    # numberDimension = np.array([])
    for i in range (0, 10):
        numberDimension.append([])
        # numberDimension.append(np.array([]))

    # print len(numberDimension)
    return numberDimension

# def create2DMatrix(columns):
#     matrix = []
#     rowList = []
#     for i in range(0,columns):
#         matrix.append(rowList)
#     return matrix




main()
