import time
from datetime import datetime
import random
import sys

streamReadingsLimit = 50

class sensorStub():
    def __init__(self):
        self.temperatureMaxVal = 60.0
        self.temperatureMinVal = 0.0
        self.currentMaxVal = 12.0
        self.currentMinVal =  0.0
    def temperatureSensorStub(self):
        return(round(random.uniform(self.temperatureMinVal, self.temperatureMaxVal), 1))

    def currentSensorStub(self):
        return(round(random.uniform(self.currentMinVal, self.currentMaxVal), 2))

class sender_receiver_stream():
    def __init__(self,time_format,sensorObject):
        self.time_format = time_format
        self.sensorObject = sensorObject
        self.readingsString = ""
        self.readingNumber = 0
    
    def sendDataToReceiver(self):
        sys.stdout.write(self.readingsString)
        #print(self.readingsString)
        return(self.readingsString)
    
    def fetchReadings(self):
        self.readingsString = ""
        self.currentTime = str(datetime.now().strftime(self.time_format))
        self.readingsString= "{ReadingNumber} - {CurrentTime} - Temperature: {temperatureVal} - CurrentInAmperes: {CurrentAmp} \n".format(ReadingNumber = self.readingNumber+1, CurrentTime = self.currentTime,temperatureVal = str(self.sensorObject.temperatureSensorStub()),CurrentAmp = str(self.sensorObject.currentSensorStub()))
        return(self.readingsString)

    def runSender(self,streamReadingsLimit):
        #while(True)
        senderText_AllReadings = ""
        for readingsNumber in range(streamReadingsLimit):
            self.readingNumber = readingsNumber
            self.fetchReadings()
            senderText_AllReadings += self.readingsString
            self.sendDataToReceiver()
        return(senderText_AllReadings)

def senderStreamData():
    time_format = r"%d/%m/%Y %H:%M:%S"
    sensor_stub = sensorStub()
    senderToReceiverStream = sender_receiver_stream(time_format,sensor_stub)
    senderToReceiverStream.runSender(streamReadingsLimit)

if __name__ == "__main__":
    senderStreamData()


