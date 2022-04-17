import sys
import re

BMSReadings = {
    'temperature' : {
        'readings'      : [],
        'searchPattern' : 'Temperature: (.+?) -' 
    },
    'current' : {
        'readings'      : [],
        'searchPattern' : 'CurrentInAmperes: (.+?) '
    }
}

def readConsoleOutput():
    lines = sys.stdin.readlines()
    return lines

def getReadingsFromString(lines):
    for line in lines:
        for parameter in BMSReadings:
            reading = re.search(BMSReadings[parameter]['searchPattern'], line).group(1)
            BMSReadings[parameter]['readings'].append(reading)   
    return BMSReadings

def getMinReading(readings):
    return min(readings,key=lambda x:float(x))

def getMaxReading(readings):
    return max(readings,key=lambda x:float(x))

def getSumOfWindow(readings):
    return sum(float(reading) for reading in readings)

def calculateMovingAverage(readings, windowSize):
    movingAverages = []
    i =0
    while i < len(readings) - windowSize + 1:
        window = readings[i : i + windowSize]
        windowAverage = round(getSumOfWindow(window) / windowSize, 2)
        movingAverages.append(windowAverage)
        i += 1
    return movingAverages

def receiverStreamData(windowSize):
    consoleOutLines = readConsoleOutput()
    readings = getReadingsFromString(consoleOutLines)
    for param in readings:
        minReading = getMinReading(readings[param]['readings'])
        maxReading = getMaxReading(readings[param]['readings'])
        movingAverages = calculateMovingAverage(readings[param]['readings'] , windowSize)
        print("{0} - {{ min : {1}, max : {2}, moving averages : {3}}}".format(param,minReading,maxReading,movingAverages))
    

if __name__ == "__main__":
    receiverStreamData(5)
    
