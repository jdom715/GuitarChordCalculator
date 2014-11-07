__author__ = 'Julio'

def configureInput(noteList, isNotes):

    # If we're dealing with fret numbers
    if not isNotes:
        # makes every input that's a stringed integer an integer
        for i in range(len(noteList)):
            if noteList[i] != 'x':
                noteList[i] = int(noteList[i])
                    
                if noteList[i] in range(12, 25):
                    noteList[i] -= 12

        # change integers in noteList to corresponding notes on string
        chromaticList = ['e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b',
                         'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a',
                         'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g',
                         'g#', 'a', 'a#', 'b', 'c', 'c#', 'd', 'd#']

        for i in range(len(noteList)):
            if isinstance(noteList[i], int):
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
    tempDict = {
        'a#': 'bb',
        'c#': 'db',
        'd#': 'eb',
        'f#': 'gb',
        'g#': 'ab'}

    invTempDict = {v: k for k, v in tempDict.items()}
    accidentalDict = dict(tempDict)
    accidentalDict.update(invTempDict)

    alternateNoteList = []
    for i in noteList:
        if i in accidentalDict.keys():
            alternateNoteList.append(accidentalDict[i])
        else:
            alternateNoteList.append(i)

    #remove x from noteList
    noteList = [i for i in noteList if i != 'x']

    #saves bass note in case it will be needed later
    bassNote = noteList[0]
    alternateBassNote = alternateNoteList[0]

    #remove duplicates
    setNoteList = set(noteList)
    noteList = [i for i in setNoteList]

    setNoteList = set(alternateNoteList)
    alternateNoteList = [i for i in setNoteList]
    
    # return list consisting of noteList, alternate noteList, and baseNote
    inputList = [noteList, alternateNoteList, bassNote, alternateBassNote]
    return inputList
