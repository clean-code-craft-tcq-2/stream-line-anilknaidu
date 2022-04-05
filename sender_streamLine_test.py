import unittest
from sender_streamLine import sender_receiver_stream
from sender_streamLine import senderStreamData
import random
import sys
import re
import time

formatPattern = r"[\d ]+-[ \w/ :]+- Temperature:[ \w\. ]+- CurrentInAmperes: [ \w\. ]+"
class TypewiseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TypewiseTest, self).__init__(*args, **kwargs)
        self.readingsContent = senderToReceiverStream.runSender(streamReadingsLimit)
        #print(self.readingsContent)
        self.maxDiff = None

    def test_readingsFormat(self):
        readingsContent = self.readingsContent.split("\n")[0]
        #print(readingsContent)
        self.assertTrue(re.match(formatPattern,readingsContent))
 
    def test_sensorValues(self):
        dataSent = self.readingsContent.split("\n")[0]
        #print(dataSent)
        temperatureReading = dataSent.split("-")[2].split(":")[1].strip()
        currentReading = dataSent.split("-")[3].split(":")[1].strip()
        self.assertEqual(float(currentReading),currentAmp)
        self.assertEqual(float(temperatureReading),temperatureDegCelcius)
    
    def test_receiverDataReceived(self):
        textRead =sys.stdin.read()
        print("Receiver Data Received")
        print(textRead)
        self.assertEqual(len(list(textRead.split("\n"))),streamReadingsLimit+1)

class sensorStub():
    def __init__(self,currentVal,temperatureVal):
        self.temperatureVal = temperatureVal
        self.currentVal = currentVal
    def temperatureSensorStub(self):
        return(self.currentVal)
    def currentSensorStub(self):
        return(self.temperatureVal)

if __name__ == "__main__":
    time_format = r"%d/%m/%Y %H:%M:%S"
    streamReadingsLimit = 50
    currentAmp = 3.1
    temperatureDegCelcius = 34
    sensor_stub = sensorStub(temperatureDegCelcius,currentAmp)
    senderToReceiverStream = sender_receiver_stream(time_format,sensor_stub)
    unittest.main()