__author__ = 'Julio'

#This is a copy of the chord calculator used for internship applications
#As of 03/31/14, it is incomplete but in progress.
#Only works for triads as of now.

'''
79 characters for reference
###############################################################################

MAIN PROCESS:

-Ask if instructions needed
	Give instructions for input if yes


-Get and Configure input

	-Put input in a list

	-Lowercase everything

	-Analyze input for correct input
    	Break if wrong, else continue

	-Put notes in note list

    -Remove x's

    -Save bass note

    -Remove duplicates


-Figure out the chord

###############################################################################
'''

#INTRODUCTION
import Introduction
Introduction

#GET AND CONFIGURE INPUT
import ConfigureInput
from ConfigureInput import *
ConfigureInput

#CALCULATE CHORD
if len(noteList) == 3:
    import TriadCalculator
    from TriadCalculator import *
    TriadCalculator
elif len(noteList) == 4:
    import SeventhCalculator
    from SeventhCalculator import *


#PRINT RESULTS
if bassNote == chordBass:
    print('\nYour chord is {0}!'.format(chordType))
else:
    print('\nYour chord is {0} with {1} in the bass.'.format(chordType, bassNote.upper()))