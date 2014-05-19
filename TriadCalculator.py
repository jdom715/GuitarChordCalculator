__author__ = 'Julio'

from ConfigureInput import *

from ChordDictionaries import triadChordDictionary

import itertools

#for triads

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

chordBass = chordType[0:2]
chordBass = chordBass.lower()
chordBass = chordBass.rstrip()
