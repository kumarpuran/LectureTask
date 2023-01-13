import re
import string
from collections import Counter


# Task Lecture 56

# Q1. try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count
# eg. [('puran', 7),....]

# Q2. try to perform a reduce opertaion to get count of all the word starting with same alphabet 
# eg. [(a,54),(b,32)....]

# Q3. try to filter out all the word from dataset
# eg. .001.abstract   here word is abstaract

# Q4. create a touple set of all  records available in five file then store it into sqlite DB 
# eg. t1 = (aah,susy 773, )  touple from file one 
#     t2 = (anh, ahag,)      touple from file two
#     t5 = (2992,eb)         touple from file five

#     hint use zip function 


try :
    
    fileOne   = open('vocab.enron.txt')
    fileTwo   = open('vocab.kos.txt')
    fileThree = open('vocab.nips.txt')
    fileFour  = open('vocab.nytimes.txt')
    fileFive  = open('vocab.pubmed.txt') 


    def getAllWordFromFile(list):

        listOfWord = [re.sub('[^a-zA-Z]+', '', x)  for x in list if type(x) == str]
        setOfWords = set(listOfWord)
        print("setOfWords size1: ",len(setOfWords))
        setOfWords = set(filter(None, setOfWords))
        
        print("setOfWords size2: ",len(setOfWords))

        return setOfWords

    def getListOfWordInFile(file):
        print("setOfWords file: ",file)
        listOfWord = list(map(lambda s: s.strip(), list(file)))
        return listOfWord

    listOfWordInFile1 = getListOfWordInFile(fileOne)
    listOfWordInFile2 = getListOfWordInFile(fileTwo)
    listOfWordInFile3 = getListOfWordInFile(fileThree)
    listOfWordInFile4 = getListOfWordInFile(fileFour)
    listOfWordInFile5 = getListOfWordInFile(fileFive)

    setOfWordInFile1 = getAllWordFromFile(listOfWordInFile1)
    setOfWordInFile2 = getAllWordFromFile(listOfWordInFile2)
    setOfWordInFile3 = getAllWordFromFile(listOfWordInFile3)
    setOfWordInFile4 = getAllWordFromFile(listOfWordInFile4)
    setOfWordInFile5 = getAllWordFromFile(listOfWordInFile5)


    def getListOfWordWithCount(setOfWord,listOfWord):
        l = []
        for val in setOfWord:
            times = listOfWord.count(val)
            l.append((val,times))

        return l

    
    alphabet = list(string.ascii_lowercase)
    print(alphabet)

    def getAlphbetCountOfWordsInList(alphabetList,list):

        listWithAlphabet = []
        for x in alphabet:
            wordsList = [ t for t in list if t.startswith(x) ]
            listWithAlphabet.append((x,len(wordsList)))
        return listWithAlphabet    


    print("Answer of startsWith Answer 2 file1  \n\n\n\n ",getAlphbetCountOfWordsInList(alphabet, listOfWordInFile1))
    print("Answer of startsWith Answer 2 file2 \n\n\n\n ",getAlphbetCountOfWordsInList(alphabet, listOfWordInFile2))
    print("Answer of startsWith Answer 2 file3 \n\n\n\n ",getAlphbetCountOfWordsInList(alphabet, listOfWordInFile3))
    print("Answer of startsWith Answer 2 file4 \n\n\n\n ",getAlphbetCountOfWordsInList(alphabet, listOfWordInFile4))
    print("Answer of startsWith Answer 2 file5 \n\n\n\n ",getAlphbetCountOfWordsInList(alphabet, listOfWordInFile5))
        

    # print("Answer of question 1 for file1 \n\n\n\n ",getListOfWordWithCount(setOfWordInFile1, listOfWordInFile1))
    # print("Answer of question 1 for file2 \n\n\n\n ",getListOfWordWithCount(setOfWordInFile2, listOfWordInFile2))
    # print("Answer of question 1 for file3 \n\n\n\n ",getListOfWordWithCount(setOfWordInFile3, listOfWordInFile3))
    # print("Answer of question 1 for file4 \n\n\n\n ",getListOfWordWithCount(setOfWordInFile4, listOfWordInFile4))
    # print("Answer of question 1 for file5 \n\n\n\n ",getListOfWordWithCount(setOfWordInFile5, listOfWordInFile5))
    
except Exception as e:
    
    print(f"exception occured while performing file operation error: {e} ")

finally:
        
    if fileOne!= None:
        fileOne.close()
    if fileTwo!= None:
        fileTwo.close()
    if fileThree!= None:
        fileThree.close()
    if fileFour!= None:
        fileFour.close()
    if fileFive!= None:
        fileFive.close()            

