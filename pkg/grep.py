


def grep(searchString, from, to):
        
    return { "result" : grepImplementation(ssearchString) }



def matchingFunctionality(searchTerm, line):
    return searchTerm in line


def grepImplementation(searchTerm, searchData):
    ans = []
    for line in searchData:
        if matchingFunctionality(searchTerm, line):        
            ans.append(line)
    return ans 


    
