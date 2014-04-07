__author__ = 'Julio'

#Get Input
bigEStringInput = input('What note is your big E string? ')
aStringInput = input('What note is your A string? ')
dStringInput = input('What note is your D string? ')
gStringInput = input('What note is your G string? ')
bStringInput = input('What note is your B string? ')
littleEStringInput = input('What note is your little e string? ')

#Put inputs into list of length 6
noteList = [bigEStringInput, aStringInput, dStringInput,
            gStringInput, bStringInput, littleEStringInput]

#Lowercase and strip everything
noteList = [i.lower() for i in noteList]
noteList = [i.strip() for i in noteList]

#convert double flats or sharps to regular notes using a dictionary
doubleAccidentalDictionary = {'abb': 'g',
                              'bbb': 'a',
                              'dbb': 'c',
                              'ebb': 'd',
                              'g##': 'a',
                              'f##': 'g',
                              'a##': 'b',
                              'c##': 'd',
                              'd##': 'e',
                              'e##': 'f#',
                              'f##': 'g'}

for i in noteList:
    if i in doubleAccidentalDictionary:
        i = doubleAccidentalDictionary[i]

#Acceptable input list
acceptList = ['a', 'a#', 'bb', 'b', 'c', 'c#', 'db', 'd', 'd#',
              'eb', 'e', 'f', 'f#', 'gb', 'g', 'g#', 'ab', 'x']

#adds every fret number to acceptable list
for i in range(25):
    acceptList.append(str(i))

#exits if poor input
for i in noteList:
    if i not in acceptList:
        import sys
        sys.exit('Incorrect Input!')

#creates a list of stringed integers 0-25
numbersStringList = [str(i) for i in range(25)]

#makes every input that's a stringed integer an integer
newNoteList = []
for i in range(len(noteList)):
    if noteList[i] == 'x':
        newNoteList.append('x')
    if noteList[i] in numbersStringList:
        noteList[i] = int(noteList[i])

    if noteList[i] in range(12, 25):
        noteList[i] -= 12
    newNoteList.insert(i, noteList[i])

if len(newNoteList) == len(noteList):
    noteList = newNoteList

#Change integers in noteList to corresponding notes on string
chromaticList = ['e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b',
                 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a',
                 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g',
                 'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#']

for i in range(len(noteList)):
    if isinstance(noteList[i], int) is True:
        if i == 0 or i == 5:
            noteList[i] = chromaticList[0 + noteList[i]]
        elif i == 1:
            noteList[i] = chromaticList[5 + noteList[i]]
        elif i == 2:
            noteList[i] = chromaticList[10 + noteList[i]]
        elif i == 3:
            noteList[i] = chromaticList[3 + noteList[i]]
        elif i == 4:
            noteList[i] = chromaticList[7 + noteList[i]]

#make accidental dictionary for switching later
tempDict = {'a#' : 'bb',
          'c#' : 'db',
          'd#' : 'eb',
          'f#' : 'gb',
          'g#' : 'ab'}

invTempDict = {v:k for k, v in tempDict.items()}
accidentalDict = dict(tempDict)
accidentalDict.update(invTempDict)

alternateNoteList = []
for i in noteList:
    if i in accidentalDict.keys():
        alternateNoteList.append(accidentalDict[i])
    else:
        alternateNoteList.append(i)

#Remove x from noteList
noteList = [i for i in noteList if i != 'x']

#saves bass note in case it will be needed later
bassNote = noteList[0]

#remove duplicates
setNoteList = set(noteList)
noteList = [i for i in setNoteList]

setNoteList = set(alternateNoteList)
alternateNoteList = [i for i in setNoteList]

print(noteList)
print(alternateNoteList)