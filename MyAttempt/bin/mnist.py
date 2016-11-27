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
    # print len(inputLayer)
    layer = convLayerActivation(inputLayer)
    poolLayerActivation(layer)


def parseData():
    inputLayer = createLayer()

    print "Parsing Data..."

    with open('resources/mnist_train.csv', 'rb') as csvfile:
        # Parse string values for numbers into int types
        for line in csvfile:
            row = line.split(",")
            image = []
            index = int(row[0])

            for unit in xrange (len(row)-1): # Store all data values except initial tag
                image.append(int(row[unit+1]))

            inputLayer[index].append(image)

    # total = 0
    # for index in inputLayer:
    #     print len(index)
    #     total += len(index)
    # print total

    return inputLayer


def convLayerActivation(inputLayer):
    imageWidth = int(np.sqrt(len(inputLayer[0][0])))
    kernel = (([1,0,1,0,1]),([1,0,1,0,1]),([1,0,1,0,1]),([1,0,1,0,1]),([1,0,1,0,1]))

    print "Convolving Layers..."

    kernelHeight =  len(kernel)
    kernelWidth =  len(kernel[0]) # Index is arbitrary

    # Assumes input picture is a square
    convLayerLength = int(np.sqrt(len(inputLayer[0][0]))) -len(kernel) + 1

    # print "In Conv Layer"
    # print int(np.sqrt(len(inputLayer[0][0]))) -len(kernel) + 1

    convLayer = createLayer()

    for index in xrange (0, len(inputLayer)): # For each set of image data in the master 0-9 array
        for image in inputLayer[index]: # For each image in the labelled index
            convolvedImage = []
            for convolvedRowNumber in xrange(convLayerLength): # The current row the convolution starts at
            # for convolvedRowNumber in range(0, convLayerLength): # The current row the convolution starts at
                for convolvedColumnNumber in xrange(convLayerLength):  # Tbe current column the convolution starts at
                    # Convolve over a single receptive field
                    convolvedUnit = 0.0
                    for i in xrange(kernelHeight):  # Kernel height/row
                        for j in xrange(kernelWidth):  # Kernel width/column
                            # Moves the kernel along the input layer
                            convolvedUnit += kernel[i][j] * image[((i + convolvedRowNumber) * imageWidth) + (j + convolvedColumnNumber)]
                    # convolvedImage.append(convolvedUnit)# Adds to the conv layer
                    convolvedImage.append(normalize(convolvedUnit))  # performs normalization and nonlinear function to convolved unit

            convLayer[index].append(convolvedImage)
    # print "good so far"
    # print inputLayer[imageNumber][0]
    return convLayer

def poolLayerActivation(inputLayer):
    poolHeight = 2
    poolWidth = 2
    # poolWindow = np.array([])
    # poolLayer = np.array([]))


    print "Pooling Layers..."

    imageLength = int(np.sqrt(len(inputLayer[0][0]))) # Width and Height of input image

    poolLayer = createLayer()
    for label in xrange(len(inputLayer)):
        for image in inputLayer[label]:

            poolImage = []
            # Assumes image is a square
            for row in range (0, imageLength/poolHeight):
                for column in range (0, imageLength/poolWidth):
                    poolWindow = []
                    for i in range (0,poolWidth):
                        for j in range(0, poolHeight):
                            poolWindow.append(image[((i+(row*poolHeight))*imageLength)+(j+(column*poolWidth))])

                    # print poolWindow
                    poolImage.append(np.max(poolWindow))
                    # print len(poolImage)

            poolLayer[label].append(poolImage)
            # print len(poolLayer)

    total = 0
    for index in poolLayer:
        print len(index)
        total += len(index)
    print total


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



main()
