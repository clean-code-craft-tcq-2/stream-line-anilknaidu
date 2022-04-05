import time
from datetime import datetime
import random
import sys

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
    def __init__(self,time_format,sensorObject,streamReadingsLimit):
        self.time_format = time_format
        self.sensorObject = sensorObject
        self.streamReadingsLimit = streamReadingsLimit
        self.readingsString = ""
    
    def sendDataToReceiver(self):
        sys.stdout.write(self.readingsString+"\n")
        return(self.readingsString+"\n")
    
    def fetchReadings(self):
        self.readingsString = ""
        for readingNumber in range(self.streamReadingsLimit):
            self.currentTime = str(datetime.now().strftime(self.time_format))
            self.readingsString+= "{ReadingNumber} - {CurrentTime} - Temperature: {temperatureVal} - CurrentInAmperes: {CurrentAmp} \n".format(ReadingNumber = readingNumber+1, CurrentTime = self.currentTime,temperatureVal = str(self.sensorObject.temperatureSensorStub()),CurrentAmp = str(self.sensorObject.currentSensorStub()))
            time.sleep(0.01)

    def runSender(self):
        #while(True)
        for readingsNumber in range(1):
            self.fetchReadings()
            return(self.sendDataToReceiver())


if __name__ == "__main__":
    time_format = r"%d/%m/%Y %H:%M:%S"
    streamReadingsLimit = 50
    sensor_stub = sensorStub()
    senderToReceiverStream = sender_receiver_stream(time_format,sensor_stub,streamReadingsLimit)
    senderToReceiverStream.runSender()