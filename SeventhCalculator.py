__author__ = 'Julio'

from ConfigureInput import *

from ChordDictionaries import seventhChordDictionary

import itertools

chordType = ''

for i in list(itertools.permutations(range(4))):
    chordString = ''
    alternateChordString = ''
    for j in i:
        chordString += noteList[j] + ' '
        alternateChordString += alternateNoteList[j] + ' '
    chordString = chordString.rstrip()
    alternateChordString = alternateChordString.rstrip()
    print(alternateChordString)

    if chordString in seventhChordDictionary:
        chordType += seventhChordDictionary[chordString]
        break
    elif alternateChordString in seventhChordDictionary:
        chordType += seventhChordDictionary[alternateChordString]
        break

chordBass = chordType[0:2]
chordBass = chordBass.lower()
chordBass = chordBass.rstrip()
