import unittest
from pkg.filter import Filter

class File:
    def __init__(self, key):
        self.key = key


class FilterTest(unittest.TestCase):

    def setUp(self):
        self.filter = Filter()
        self.files = [
            File('2024-04-05/01.txt'),
            File('2024-04-05/03.txt'),
            File('2024-04-05/09.txt'),
            File('2024-04-05/11.txt'),
            File('2024-04-06/01.txt'),
        ]


    def testInRange(self):
        expectedFiles = ['2024-04-05/01.txt', '2024-04-05/03.txt', '2024-04-05/09.txt', '2024-04-05/11.txt']
        filteredFiles = self.filter.filterFilesOnTimeRange(self.files,1712275200, 1712361599)
        filteredFiles = [ file.key for file in filteredFiles ]
        self.assertEqual(expectedFiles, filteredFiles)

    def testAtBoundary(self):
        expectedFiles = ['2024-04-06/01.txt']
        filteredFiles = self.filter.filterFilesOnTimeRange(self.files, 1712361599, 1712422348)
        filteredFiles = [ file.key for file in filteredFiles ]
        self.assertEqual(expectedFiles, filteredFiles)

    def testOutOfRange(self):
        expectedFiles = []
        filteredFiles = self.filter.filterFilesOnTimeRange(self.files, 1712422348, 1712622348)
        filteredFiles = [ file.key for file in filteredFiles ]
        self.assertEqual(expectedFiles, filteredFiles)

if __name__ == '__main__':
    unittest.main()

