import unittest
import receiver_streamLine

class receiver_test(unittest.TestCase):

    def test_getReadingsFromString(self):
        testConsoleOutString = ['1 - 17/04/2022 13:53:35 - Temperature: 52.8 - CurrentInAmperes: 5.96 \n','2 - 17/04/2022 13:53:35 - Temperature: 40.9 - CurrentInAmperes: 2.31 \n']
        bmsReadings = receiver_streamLine.getReadingsFromString(testConsoleOutString) 
        self.assertTrue(bmsReadings['temperature']['readings'] == [52.8, 40.9])
        self.assertTrue(bmsReadings['current']['readings'] == [5.96, 2.31])
    
    def test_calculateMovingAverage(self):
        self.assertTrue(receiver_streamLine.calculateMovingAverage([1, 2, 3, 7, 9],3) == [2.0, 4.0, 6.33])
        self.assertTrue(receiver_streamLine.calculateMovingAverage([1, 2.44, 3.12, 4, 5.6, 6, 7, 9.9],5) == [3.23, 4.23, 5.14, 6.5])

    def test_getMinAndMaxReading(self):
        self.assertTrue(receiver_streamLine.getMinReading([1.2, 1.11, 1.01, 2.4, 2.5]) == 1.01)
        self.assertTrue(receiver_streamLine.getMinReading([0, 0, 0, -0.02]) == -0.02)
        self.assertTrue(receiver_streamLine.getMaxReading([0, 0, 0, -0.02]) == 0)
        self.assertTrue(receiver_streamLine.getMaxReading([1.2, 1.11, 1.01, 2.4, 2.5]) == 2.5)

    def test_receiverStreamData(self):
        testConsoleOutString = ['1 - 17/04/2022 13:53:35 - Temperature: 52.8 - CurrentInAmperes: 5.96 \n','2 - 17/04/2022 13:53:35 - Temperature: 40.9 - CurrentInAmperes: 2.31 \n']
        self.assertTrue(receiver_streamLine.receiverStreamData(testConsoleOutString,2) == 'temperature - { min : 40.9, max : 52.8, moving averages : [46.85, 46.85, 46.85]}\ncurrent - { min : 2.31, max : 5.96, moving averages : [4.13, 4.13, 4.13]}\n')

if __name__ == '__main__':
    unittest.main()
