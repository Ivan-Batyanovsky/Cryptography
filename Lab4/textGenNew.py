import string
import random


def textParser(file):
    wordSet = set()
    origText = list()
    for line in file:
        for word in line.split(sep="\n"):
            origText.append(word)
        for word in line.split():
            wordSet.add(word)
    return wordSet, origText


def getRigOfPunctuation(wordList):
    newList = []
    for word in wordList:
        newList.append(word.translate(str.maketrans('', '', string.punctuation)))
    return newList


def randomSymbolsGen(N, lang):
    return ''.join(random.choices(finalLang, k=N))


def fromListToStr(wordList):
    newStr = str()
    for word in wordList:
        newStr += word
    return newStr


def randomWordsGen(N, wordList):
    return random.choices(wordList, k=N)


def countTheDifferences(textA, textB):
    counter = 0
    for i in range(len(textA)):
        if textA[i] == textB[i]:
            counter += 1
    return counter


string.punctuation += '”' + '“'  # этих символов нет по умолчанию

random.seed(11)

WAPF = open("WarAndPeaceFull", encoding='utf-8', mode="r")  # reading txt
TBKF = open("The Brothers Karamazov", encoding='utf-8', mode="r")  # reading txt

charCounter = 0
allWordsSetWAPF, origWAPF = textParser(WAPF)  # taking unique set of words and orig text
allWordsSetTBKF, origTBKF = textParser(TBKF)  # taking unique set of words and orig text

allWordsSetWAPF = sorted(allWordsSetWAPF)  # sorting set
allWordsSetTBKF = sorted(allWordsSetTBKF)  # sorting set

allWordsSetWAPF = getRigOfPunctuation(allWordsSetWAPF) + [" "]  # getting rid of punctuation
allWordsSetTBKF = getRigOfPunctuation(allWordsSetTBKF) + [" "]  # getting rid of punctuation

# print(string.punctuation)  # checking punctuation symbols

WAPF.close()  # closing file
TBKF.close()  # closing file

origWAPF = fromListToStr(origWAPF)  # convert list to str
origTBKF = fromListToStr(origTBKF)  # convert list to str

setup = set()
for symb in origWAPF[:]:
    setup.add(symb)

finalLang = str()
for symbol in setup:
    finalLang += symbol

rWordsWAPF = fromListToStr(randomWordsGen(100000, allWordsSetWAPF))
rWordsTBKF = fromListToStr(randomWordsGen(100000, allWordsSetTBKF))
rSymbolsWAPF = randomSymbolsGen(1000000, finalLang)
rSymbolsTBKF = randomSymbolsGen(1000000, finalLang)
croppedOriginalTextWAPF = origWAPF
croppedOriginalTextTBKF = origTBKF


# Ниже процесс можно заменить функцией, но у меня уже нет сил сегодня это доделывать, а времени нет
numberOfSymbols = 1000
print("-" * 100)
print("Для текстов, размер которых равен", numberOfSymbols, "символов")
print("1)", countTheDifferences(origWAPF[:numberOfSymbols], origTBKF[:numberOfSymbols]))
print("2)", countTheDifferences(origWAPF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("3)", countTheDifferences(origWAPF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))
print("4)", countTheDifferences(rSymbolsTBKF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("5)", countTheDifferences(rWordsTBKF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))
print("-" * 100)

numberOfSymbols = 10000
print("-" * 100)
print("Для текстов, размер которых равен", numberOfSymbols, "символов")
print("1)", countTheDifferences(origWAPF[:numberOfSymbols], origTBKF[:numberOfSymbols]))
print("2)", countTheDifferences(origWAPF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("3)", countTheDifferences(origWAPF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))
print("4)", countTheDifferences(rSymbolsTBKF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("5)", countTheDifferences(rWordsTBKF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))

numberOfSymbols = 100000
print("-" * 100)
print("Для текстов, размер которых равен", numberOfSymbols, "символов")
print("1)", countTheDifferences(origWAPF[:numberOfSymbols], origTBKF[:numberOfSymbols]))
print("2)", countTheDifferences(origWAPF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("3)", countTheDifferences(origWAPF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))
print("4)", countTheDifferences(rSymbolsTBKF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("5)", countTheDifferences(rWordsTBKF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))
print("-" * 100)

numberOfSymbols = 500000
print("-" * 100)
print("Для текстов, размер которых равен", numberOfSymbols, "символов")
print("1)", countTheDifferences(origWAPF[:numberOfSymbols], origTBKF[:numberOfSymbols]))
print("2)", countTheDifferences(origWAPF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("3)", countTheDifferences(origWAPF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))
print("4)", countTheDifferences(rSymbolsTBKF[:numberOfSymbols], rSymbolsWAPF[:numberOfSymbols]))
print("5)", countTheDifferences(rWordsTBKF[:numberOfSymbols], rWordsWAPF[:numberOfSymbols]))
print("-" * 100)

print(rWordsWAPF[:60])
print(rSymbolsWAPF[:60])
print(origWAPF[:60])











