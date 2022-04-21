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

streamReadingsLimit = 50

def readConsoleOutput():
    lines = [sys.stdin.readline() for i in range(streamReadingsLimit)]
    return lines

def getReadingsFromString(lines):
    for line in lines:
        for parameter in BMSReadings:
            reading = re.search(BMSReadings[parameter]['searchPattern'], line).group(1)
            BMSReadings[parameter]['readings'].append(float(reading))
    return BMSReadings

def getMinReading(readings):
    return min(readings)

def getMaxReading(readings):
    return max(readings)

def calculateMovingAverage(readings, windowSize):
    movingAverages = []
    i =0
    while i < len(readings) - windowSize + 1:
        window = readings[i : i + windowSize]
        windowAverage = round(sum(window) / windowSize, 2)
        movingAverages.append(windowAverage)
        i += 1
    return movingAverages

def receiverStreamData(consoleOutLines,windowSize):
    receiverOutput = ''
    readings = getReadingsFromString(consoleOutLines)
    for param in readings:
        minReading = getMinReading(readings[param]['readings'])
        maxReading = getMaxReading(readings[param]['readings'])
        movingAverages = calculateMovingAverage(readings[param]['readings'] , windowSize)
        receiverOutput += '{0} - {{ min : {1}, max : {2}, moving averages : {3}}}\n'.format(param,minReading,maxReading,movingAverages)
                
    print(receiverOutput)
    return receiverOutput

if __name__ == "__main__":
    consoleOutLines = readConsoleOutput()
    receiverStreamData(consoleOutLines,5)
