#Algorytm Boyera Moore'a
#Mateusz Adamczyk

def badCharTab(pattern):
    tTab = {}
    for i in range(len(pattern)):
        tTab[pattern[i]] = i
    return tTab


def correctSuffixTab(pattern):
    patternLen = len(pattern)
    tTab = [0] * (patternLen + 1)
    suffix = [0] * (patternLen + 1)

    lastPrefixPos = patternLen
    for i in range(patternLen, 0, -1):
        if isPrefix(pattern, i):
            lastPrefixPos = i
        tTab[patternLen - i] = lastPrefixPos - i + patternLen
    for i in range(patternLen):
        suffixLength = suffix[i]
        if i > suffixLength:
            tTab[patternLen - suffixLength] = patternLen - i + suffixLength
    return tTab


def isPrefix(pattern, p):
    patternLength = len(pattern)
    suffixLength = patternLength - p
    for i in range(suffixLength):
        if pattern[i] != pattern[p + i]:
            return False
    return True


def correctSuffixTab(pattern):
    patternLen = len(pattern)
    tTab = [0] * (patternLen + 1)
    suffix = [0] * (patternLen + 1)

    lastPrefixPos = patternLen
    for i in range(patternLen, 0, -1):
        if isPrefix(pattern, i):
            lastPrefixPos = i
        tTab[patternLen - i] = lastPrefixPos - i + patternLen
    for i in range(patternLen):
        suffixLength = suffix[i]
        if i > suffixLength:
            tTab[patternLen - suffixLength] = patternLen - i + suffixLength
    return tTab


def boyer_moore(text, pattern):
    textLen = len(text)
    patternLen = len(pattern)
    if patternLen == 0:
        return [0]
    badChar = badCharTab(pattern)
    correctSuffix = correctSuffixTab(pattern)
    i = 0
    tabOfIndexOfPatternOccurence = []

    while i <= textLen - patternLen:
        j = patternLen - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            tabOfIndexOfPatternOccurence.append(i)
            if i + patternLen < textLen:
                i += patternLen - min(correctSuffix[j + 1], badChar.get(text[i + patternLen], -1))
            else:
                i += 1
        else:
            i += max(1, j - badChar.get(text[i + j], -1))
    return tabOfIndexOfPatternOccurence


print("Znalezione hasła są na indeksach:", 
boyer_moore("""Stoi na stacji lokomotywa,
Ciężka, ogromna i pot z niej spływa
Tłusta oliwa.
Stoi i sapie, dyszy i dmucha,
Żar z rozgrzanego jej brzucha bucha
Buch - jak gorąco!
Uch - jak gorąco!
Puff - jak gorąco!
Uff - jak gorąco!
Już ledwo sapie, już ledwo zipie,
A jeszcze palacz wegiel w nią sypie.""", 
"gorąco"))
