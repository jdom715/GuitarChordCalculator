__author__ = 'Julio'

triadChordDictionary = {
    #major chords
    'ceg': 'C major', 'c#e#g#': 'C# major',
    'dbfab': 'Db major', 'df#a': 'D major', 'd#ga#': 'D# major',
    'ebgbb': 'Eb major', 'eg#b': 'E major',
    'fac': 'F major', 'f#a#c#': 'F# major',
    'gbbbdb': 'Gb major', 'gbd': 'G major', 'g#b#d#': 'G# major',
    'abceb': 'Ab major', 'ac#e': 'A major', 'a#de#': 'A# major',
    'bbdf': 'Bb major', 'bd#f#': 'B major',

    #minor chords
    'cebg': 'C minor', 'c#eg#': 'C# minor',
    'dbfbab': 'Db minor', 'dfa': 'D minor', 'd#f#a#': 'D# minor',
    'ebgbbb': 'Eb minor', 'egb': 'E minor', 'e#g#b#': 'E# minor',
    'fabc': 'F minor', 'f#ac#': 'F# minor',
    'gbadb': 'Gb minor', 'gbbd': 'G minor',
    'abcbeb': 'Ab minor', 'ace': 'A minor', 'a#c#e#': 'A# minor',
    'bbdbf': 'Bb minor', 'bdf#': 'B minor',

    #dim chords
    'cebgb': 'C dim', 'c#eg': 'C# dim',
    'dbfbg': 'Db dim', 'dfab': 'D dim', 'd#f#a': 'D# dim',
    'ebgba': 'Eb dim', 'egbb': 'E dim',
    'fabcb': 'F dim', 'f#ac': 'F# dim',
    'gbac': 'Gb dim', 'gbbdb': 'G dim', 'g#bd': 'G# dim',
    'abcbd': 'Ab dim', 'aceb': 'A dim', 'a#c#e': 'A# dim',
    'bbdbfb': 'Bb dim', 'bdf': 'B dim',

    #aug chords
    'ceg#': 'C aug', 'c#e#a': 'C# aug',
    'dbfa': 'Db aug', 'df#a#': 'D aug', 'd#gb': 'D# aug',
    'ebgb': 'Eb aug', 'eg#b#': 'E aug',
    'fac#': 'F aug', 'f#a#d': 'F# aug',
    'gbbbd': 'Gb aug', 'gbd#': 'G aug', 'abce': 'Ab aug',
    'ac#e#': 'A aug', 'bbdf#': 'Bb aug', 'bd#g': 'B aug',

    #sus2 chords
    'cdg': 'C sus2', 'c#d#g#': 'C# sus2',
    'dbebab': 'Db sus2', 'deba': 'D sus2', 'd#ea#': 'D# sus2',
    'ebfbb': 'Eb sus2', 'ef#b': 'E sus2',
    'fgc': 'F sus2', 'f#g#c#': 'F# sus2',
    'gbabdb': 'Gb sus2', 'gad': 'G sus2', 'g#a#d#': 'G# sus2',
    'abbbeb': 'Ab sus2', 'abe': 'A sus2', 'a#ce#': 'A# sus2',
    'bbcf': 'Bb sus2', 'bc#f#': 'B sus2',

    #sus4 chords
    'cfg': 'C sus4', 'c#f#g#': 'C# sus4',
    'dbgbab': 'Db sus4', 'dga': 'D sus4', 'd#g#a#': 'D# sus4',
    'ebabbb': 'Eb sus4', 'eab': 'E sus4',
    'fbbc': 'F sus4', 'f#bc#': 'F# sus4',
    'gbcbdb': 'Gb sus4', 'gcd': 'G sus4', 'g#c#d#': 'G# sus4',
    'abdbeb': 'Ab sus4', 'ade': 'A sus4', 'a#d#e#': 'A# sus4',
    'bbebf': 'Bb sus4', 'bef#': 'B sus4'
}

seventhChordDictionary = {
    #maj7 chords
    'cegb': 'C maj7', 'c#e#g#b#': 'C# maj7',
    'dbfabc': 'Db maj7','df#ac#': 'D maj7', 'd#ga#d': 'D# maj7',
    'ebgbbd': 'Eb maj7','eg#bd#': 'E maj7',
    'face': 'F maj7', 'f#a#c#e#': 'F# maj7',
    'gbbbdbf': 'Gb maj7', 'gbdf#': 'G maj7', 'g#b#d#g': 'G# maj7',
    'abcebg': 'Ab maj7', 'ac#eg#': 'A maj7', 'a#de#a': 'A# maj7',
    'bbdfa': 'Bb maj7', 'bd#f#a#': 'B maj7',

    #min7 chords
    'cebgbb': 'C min7', 'c#eg#b': 'C# min7',
    'dbfbabcb': 'Db min7','dfac': 'D min7', 'd#f#a#c#': 'D# min7',
    'ebgbbbdb': 'Eb min7','egbd': 'E min7',
    'fabceb': 'F min7','f#ac#e': 'F# min7',
    'gbadbfb': 'Gb min7', 'gbbdf': 'G min7','g#bd#f#': 'G# min7',
    'abcbebgb': 'Ab min7','aceg': 'A min7','a#c#e#g#': 'A# min7',
    'bbdbfab': 'Bb min7', 'bdf#a': 'B min7',

    #dominant seventh chords
    'cegbb': 'C 7', 'c#e#g#b': 'C# 7',
    'dbfabcb': 'Db 7','df#ac': 'D 7', 'd#ga#c#': 'D# 7',
    'ebgbbdb': 'Eb 7','eg#bd': 'E 7',
    'faceb': 'F 7', 'f#a#c#e': 'F# 7',
    'gbbbdbfb': 'Gb 7', 'gbdf': 'G 7', 'g#b#d#gb': 'G# 7',
    'abcebgb': 'Ab 7', 'ac#eg': 'A 7', 'a#de#g#': 'A# 7',
    'bbdfab': 'Bb 7', 'bd#f#a': 'B 7',

    #dim seventh chords
    'cebgba': 'C dim7', 'c#egbb': 'C# dim7',
    'dbfbgbb': 'Db dim7','dfabcb': 'D dim7', 'd#f#ac': 'D# dim7',
    'ebgbac': 'Eb dim7','egbbdb': 'E dim7',
    'fabcbd': 'F dim7', 'f#aceb': 'F# dim7',
    'gbaceb': 'Gb dim7', 'gbbdbfb': 'G dim7', 'g#bdf': 'G# dim7',
    'abcbdf': 'Ab dim7', 'acebgb': 'A dim7', 'a#c#eg': 'A# dim7',
    'bbdbfbg': 'Bb dim7', 'bdfab': 'B dim7',

    #half-dim seventh chords
    'cebgbbb': 'C min7b5', 'c#egb': 'C# min7b5',
    'dbfbgcb': 'Db min7b5','dfabc': 'D min7b5','d#f#ac#': 'D# min7b5',
    'ebgbadb': 'Eb min7b5','egbbd': 'E min7b5',
    'fabcbeb': 'F min7b5','f#ace': 'F# min7b5',
    'gbacfb': 'Gb min7b5', 'gbbdbf': 'G min7b5','g#bdf#': 'G# min7b5',
    'abcbdgb': 'Ab min7b5','acebg': 'A min7b5','a#c#eg#': 'A# min7b5',
    'bbdbfbab': 'Bb min7b5', 'bdfa': 'B min7b5',

    #dim major seventh chords
    'cebgbb': 'C dim Maj7', 'c#egb#': 'C# dim Maj7',
    'dbfbgc': 'Db dim Maj7','dfabc#': 'D dim Maj7',
    'd#f#ad': 'D# dim Maj7',
    'ebgbad': 'Eb dim Maj7','egbbd#': 'E dim Maj7',
    'fabcbe': 'F dim Maj7','f#ace#': 'F# dim Maj7',
    'gbacf': 'Gb dim Maj7', 'gbbdbf#': 'G dim Maj7',
    'g#bdg': 'G# dim Maj7',
    'abcbdg': 'Ab dim Maj7', 'acebg#': 'A dim Maj7',
    'a#c#ea': 'A# dim Maj7',
    'bbdbfba': 'Bb min7b5', 'bdfa#': 'B dim Maj7',

    #aug chords
    'ceg#': 'C aug', 'c#e#a': 'C# aug',
    'dbfa': 'Db aug','df#a#': 'D aug', 'd#gb': 'D# aug',
    'ebgb': 'Eb aug','eg#b#': 'E aug',
    'fac#': 'F aug', 'f#a#d': 'F# aug',
    'gbbbd': 'Gb aug', 'gbd#': 'G aug',
    'abce': 'Ab aug','ac#e#': 'A aug',
    'bbdf#': 'Bb aug', 'bd#g': 'B aug'

'''
    #sus2 chords
    'cdg': 'C sus2', 'c#d#g#': 'C# sus2',
    'dbebab': 'Db sus2','deba': 'D sus2', 'd#ea#': 'D# sus2',
    'ebfbb': 'Eb sus2','ef#b': 'E sus2',
    'fgc': 'F sus2', 'f#g#c#': 'F# sus2',
    'gbabdb': 'Gb sus2', 'gad': 'G sus2', 'g#a#d#': 'G# sus2',
    'abbbeb': 'Ab sus2', 'abe': 'A sus2', 'a#ce#': 'A# sus2',
    'bbcf': 'Bb sus2', 'bc#f#': 'B sus2',

    #sus4 chords
    'cfg': 'C sus4', 'c#f#g#': 'C# sus4',
    'dbgbab': 'Db sus4','dga': 'D sus4', 'd#g#a#': 'D# sus4',
    'ebabbb': 'Eb sus4', 'eab': 'E sus4',
    'fbbc': 'F sus4', 'f#bc#': 'F# sus4',
    'gbcbdb': 'Gb sus4', 'gcd': 'G sus4', 'g#c#d#': 'G# sus4',
    'abdbeb': 'Ab sus4', 'ade': 'A sus4', 'a#d#e#': 'A# sus4',
    'bbebf': 'Bb sus4', 'bef#': 'B sus4'
'''
}
