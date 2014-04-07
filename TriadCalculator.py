__author__ = 'Julio'

from ConfigureInput import *

import itertools

chordDictionary = {  #major chords
                     'c e g': 'C major', 'c# e# g#': 'C# major', 'db f ab': 'Db major',
                     'd f# a': 'D major', 'd# g a#': 'D# major','eb g bb': 'Eb major',
                     'e g# b': 'E major', 'f a c': 'F major', 'f# a# c#': 'F# major',
                     'gb bb db': 'Gb major', 'g b d': 'G major', 'g# b# d#': 'G# major',
                     'ab c eb': 'Ab major', 'a c# e': 'A major', 'a# d e#': 'A# major',
                     'bb d f': 'Bb major','b d# f#': 'B major',
                     #minor chords
                     'c eb g': 'C minor', 'c# e g#': 'C# minor', 'db fb ab': 'Db minor',
                     'd f a': 'D minor', 'd# f# a#': 'D# minor','eb gb bb': 'Eb minor',
                     'e g b': 'E minor', 'e# g# b#': 'E# minor', 'f ab c': 'F minor',
                     'f# a c#': 'F# minor', 'gb a db': 'Gb minor', 'g bb d': 'G minor',
                     'g# b d#': 'G# minor','ab cb eb': 'Ab minor', 'a c e': 'A minor',
                     'a# c# e#': 'A# minor', 'bb db f': 'Bb minor','b d f#': 'B minor',
                     #diminished chords
                     'c eb gb': 'C diminished', 'c# e g': 'C# diminished', 'db fb g': 'Db diminished',
                     'd f ab': 'D diminished', 'd# f# a': 'D# diminished', 'eb gb a': 'Eb Diminished',
                     'e g bb': 'E diminished', 'f ab cb': 'F diminished', 'f# a c': 'F# diminished',
                     'gb a c': 'Gb diminished', 'g bb db': 'G diminished', 'g# b d': 'G# diminished',
                     'ab cb d': 'Ab diminished', 'a c eb': 'A diminished', 'a# c# e': 'A# diminished',
                     'bb db fb': 'Bb diminished', 'b d f': 'B diminished',
                     #augmented chords
                     'c e g#': 'C augmented', 'c# e# a': 'C# augmented','db f a': 'Db augmented',
                     'd f# a#': 'D augmented', 'd# g b': 'D# augmented','eb g b': 'Eb augmented',
                     'e g# b#': 'E augmented', 'f a c#': 'F augmented','f# a# d': 'F# augmented',
                     'gb bb d': 'Gb augmented', 'g b d#': 'G augmented','ab c e': 'Ab augmented',
                     'a c# e#': 'A augmented', 'bb d f#': 'Bb augmented', 'b d# g': 'B augmented',
                     #sus2 chords
                     'c d g': 'C sus2', 'c# d# g#': 'C# sus2', 'db eb ab': 'Db sus2',
                     'd eb a': 'D sus2', 'd# e a#': 'D# sus2','eb f bb': 'Eb sus2',
                     'e f# b': 'E sus2', 'f g c': 'F sus2', 'f# g# c#': 'F# sus2',
                     'gb ab db': 'Gb sus2', 'g a d': 'G sus2', 'g# a# d#': 'G# sus2',
                     'ab bb eb': 'Ab sus2', 'a b e': 'A sus2', 'a# c e#': 'A# sus2',
                     'bb c f': 'Bb sus2','b c# f#': 'B sus2',
                     #sus4 chords
                     'c f g': 'C sus4', 'c# f# g#': 'C# sus4', 'db gb ab': 'Db sus4',
                     'd g a': 'D sus4', 'd# g# a#': 'D# sus4','eb ab bb': 'Eb sus4',
                     'e a b': 'E sus4', 'f bb c': 'F sus4', 'f# b c#': 'F# sus4',
                     'gb cb db': 'Gb sus4', 'g c d': 'G sus4', 'g# c# d#': 'G# sus4',
                     'ab db eb': 'Ab sus4', 'a d e': 'A sus4', 'a# d# e#': 'A# sus4',
                     'bb eb f': 'Bb sus4','b e f#': 'B sus4'
                    }

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
    if chordString in chordDictionary:
        chordType += chordDictionary[chordString]
        break
    elif alternateChordString in chordDictionary:
        chordType += chordDictionary[alternateChordString]
        break

chordBass = chordType[0:2]
chordBass = chordBass.lower()
chordBass = chordBass.rstrip()
