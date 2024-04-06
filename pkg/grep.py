from abc import abstractmethod
from pkg.filter import Filter


class GrepStrategy:
    @abstractmethod
    def match(self, searchTerm, searchLine) -> bool:
        pass


class ExactMatchGrepStrategy(GrepStrategy):
    def match(searchTerm, line):
        return searchTerm in line



class Grep:
    def __init__(self, strategy):
        self.strategy = strategy
        self.filter = Filter()

    def search(self, fileStore, searchString, fromDate, toDate):
        responsArr = []
        files = fileStore.getFiles()
        fileredFiles = self.filter.filterFilesOnTimeRange(files, fromDate, toDate)
        for file in fileredFiles:
            grepResult = self.__searchInFile(searchString, fileStore.getFile(file))
            responsArr.extend(grepResult)

        return {"result": responsArr}

    def __searchInFile(self, searchTerm, searchData):
        ans = []
        for line in searchData:
            if self.strategy.match(searchTerm, line):
                ans.append(line)
        return ans
