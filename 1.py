import math
import matplotlib.pyplot as plt
import numpy as np
import time
import _thread

class Predictor():
    sX = []
    bX = []
    predX = []

    sY = []
    bY = []
    predY = []

    originalData = []
    def __init__(self, x, y):
        self.x = x
        self.sX.append(x[0])
        self.bX.append(x[1] - x[0])

        self.y = y
        self.sY.append(y[0])
        self.bY.append(y[1] - y[0])
        # self.bX.append((x[3] - x[0])/3)
        # self.desiredI = desiredI

    def sXCal(self, i, alpha):
        if (alpha > 1 or alpha < 0):
            print("Error")
        else:
            sum = (alpha * self.x[i]) + (1 - alpha) * (self.sX[i - 1] + self.bX[i - 1])
            self.sX.append(sum)

    def bXCal(self, i, gamma):
        if (gamma > 1 or gamma < 0):
            print("Error")
        else:
            sum = gamma * (self.sX[i] - self.sX[i - 1]) + (1 - gamma) * self.bX[i - 1]
            self.bX.append(sum)

    def predictX(self, m):
        self.predX.append((self.sX[len(self.sX) - 1] + m * self.bX[len(self.sX) - 1]))

    def handlerX(self, i, alpha, gamma, predictionThresh):

        for cnt in range(1, i + 1):
            self.sXCal(cnt, alpha)
            self.bXCal(cnt, gamma)
        for cnt in range(1, predictionThresh + 1):
            self.predictX(cnt)

    def drawPlotX(self):
        i = []
        for cnt in range(len(self.predX)):
            i.append(cnt + len(self.sX))
        plt.plot(i, self.predX, 'ro')
        plt.axis([31, 90, 800, 10000])
        xAxis = range(31, 90)
        yAxis = []
        for x in xAxis:
            yAxis.append(pow(x, 2))
        plt.plot(xAxis, yAxis, linewidth = 2)
        #t = np.arange(11., 16., 0.2)
        plt.show()

    def sYCal(self, i, alpha):
        if (alpha > 1 or alpha < 0):
            print("Error")
        else:
            sum = (alpha * self.y[i]) + (1 - alpha) * (self.sY[i - 1] + self.bY[i - 1])
            self.sY.append(sum)

    def bYCal(self, i, gamma):
        if (gamma > 1 or gamma < 0):
            print("Error")
        else:
            sum = gamma * (self.sY[i] - self.sY[i - 1]) + (1 - gamma) * self.bY[i - 1]
            self.bY.append(sum)

    def predictY(self, m):
        self.predY.append((self.sY[len(self.sY) - 1] + m * self.bY[len(self.sY) - 1]))

    def handlerY(self, i, alpha, gamma, predictionThresh):

        for cnt in range(1, i + 1):
            self.sYCal(cnt, alpha)
            self.bYCal(cnt, gamma)
        for cnt in range(1, predictionThresh + 1):
            self.predictY(cnt)

    def drawPlotY(self, thresh, cut):
        predictedPlot = []
        '''
        for cnt in range(len(self.predY)):
            predictedPlot.append(cnt + len(self.sY))
        plt.plot(predictedPlot, self.predY, 'ro')
        plt.axis([10, 50, 50, 200])
        xAxis = range(1, 20)
        xAxis = []
        plt.plot(xAxis, self.originalData, linewidth = 2)
        plt.show()
        '''
        for cnt in range(len(self.predY)):
            predictedPlot.append(cnt + 1 + len(self.sY))
        plt.plot(predictedPlot, self.predY, 'ro')
        plt.axis([1, 20, 0, 20])
        xAxis = range(cut + 1, thresh + 1)
        #yAxis = []
        plt.plot(xAxis, self.originalData[0][cut:], linewidth = 2)
        plt.show()

    def addOriginalData(self, data):
        self.originalData.append(data)


def mainHandler(address, thresh, cut):
    aux = []
    myFile = open(address, 'r')
    for cnt in range(thresh):
        aux.append(float(myFile.readline()))
        myFile.seek(0)
        time.sleep(0.1)

        if(cnt == cut):
            myPredictor = Predictor(aux, aux)
            _thread.start_new_thread(myPredictor.handlerY, (cut, 0.3623, 1.0, thresh - cut))
    myPredictor.addOriginalData(aux)
    print(myPredictor.predY)
    print(myPredictor.originalData[0][cut:])
    #print(myPredictor.originalData)
    myPredictor.drawPlotY(thresh, cut)


def main():
    ans = []
    mStart = time.time()
    for cnt in range(31):
        ans.append(math.pow(cnt, 2))
    myPredictor = Predictor(ans, ans)

    for cnt in range(1, 31):
        myPredictor.sXCal(cnt, 0.3623)
        myPredictor.bXCal(cnt, 1.0)

        myPredictor.sYCal(cnt, 0.3623)
        myPredictor.bYCal(cnt, 1.0)
    pStart = time.time()
    for cnt in range(1, 60):
        myPredictor.predictX(cnt)
        myPredictor.predictY(cnt)
    mStop = time.time()

    myPredictor.drawPlotX()
    print(myPredictor.predX)
    #print(myPredictor.predY)

def main2():
    mainHandler('Files/1.txt', 20, 5)

if __name__ == "__main__":
    main2()
