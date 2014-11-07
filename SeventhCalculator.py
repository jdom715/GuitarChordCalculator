__author__ = 'Julio'

#import seventh chord dictionary
from ChordDictionaries import seventhChordDictionary

#import itertools for permutations
import itertools

def seventhCalculator(noteList, alternateNoteList):
    chordType = '' 

    for i in list(itertools.permutations(range(4))):
        chordString = ''
        alternateChordString = ''
        for j in i:

            chordString += noteList[j] + ' '
            alternateChordString += alternateNoteList[j] + ' '

            chordString = chordString.rstrip()
            alternateChordString = alternateChordString.rstrip()
            
        if chordString in seventhChordDictionary:
            chordType += seventhChordDictionary[chordString]
            break
        elif alternateChordString in seventhChordDictionary:
            chordType += seventhChordDictionary[alternateChordString]
            break

    chordBass = chordType[0:2]
    chordBass = chordBass.lower()
    chordBass = chordBass.rstrip()

    chordList = [chordString, chordBass, chordType]
    return chordList
