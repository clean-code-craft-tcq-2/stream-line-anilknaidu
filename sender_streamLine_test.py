import unittest
from sender_streamLine import sender_receiver_stream
import random
import sys
import re

formatPattern = r"[\d ]+-[ \w/ :]+- Temperature:[ \w\. ]+- CurrentInAmperes: [ \w\. ]+"
class TypewiseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TypewiseTest, self).__init__(*args, **kwargs)
        self.readingsContent = senderToReceiverStream.runSender()
        self.maxDiff = None
    def test_readingsFormat(self):
        indexNum = int(random.uniform(1, streamReadingsLimit))
        readingsContent = self.readingsContent
        readingsContent = readingsContent.split("\n")[indexNum]
        self.assertTrue(re.match(formatPattern,readingsContent))
 
    def test_sensorValues(self):
        indexNum = int(random.uniform(1, streamReadingsLimit))
        dataSent = self.readingsContent
        temperatureReading = dataSent.split("\n")[0].split("-")[2].split(":")[1].strip()
        currentReading = dataSent.split("\n")[0].split("-")[3].split(":")[1].strip()
        self.assertEqual(float(currentReading),currentAmp)
        self.assertEqual(float(temperatureReading),temperatureDegCelcius)
        
    def test_indexLines(self):
        self.assertEqual(len(list(self.readingsContent.split("\n")))-2,streamReadingsLimit)

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
    senderToReceiverStream = sender_receiver_stream(time_format,sensor_stub,streamReadingsLimit)
    unittest.main()