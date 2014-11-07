__author__ = 'Julio'

#import the triad dictionary
from ChordDictionaries import triadChordDictionary

#used for permutations
import itertools

def triadCalculator(noteList, alternateNoteList):
    # make empty string variable
    chordType = ''

    for i in list(itertools.permutations(range(3))):
        chordString = ''
        alternateChordString = ''
        for j in i:
            chordString += noteList[j] + ' '
            alternateChordString += alternateNoteList[j] + ' '

            chordString = chordString.rstrip()
            alternateChordString = alternateChordString.rstrip()
            
        if chordString in triadChordDictionary:
            chordType += triadChordDictionary[chordString]
            break
        elif alternateChordString in triadChordDictionary:
            chordType += triadChordDictionary[alternateChordString]
            break

    # get bass for later
    chordBass = chordType[0:2]
    chordBass = chordBass.lower()
    chordBass = chordBass.rstrip()
    
    # return dictionary of chordString and chordBass
    chordList = [chordString, chordBass, chordType]
    return chordList


