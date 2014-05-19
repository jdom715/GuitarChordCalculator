__author__ = 'Julio'

triadChordDictionary = {
    #major chords
    'c e g': 'C major', 'c# e# g#': 'C# major',
    'db f ab': 'Db major', 'd f# a': 'D major', 'd# g a#': 'D# major',
    'eb g bb': 'Eb major', 'e g# b': 'E major',
    'f a c': 'F major', 'f# a# c#': 'F# major',
    'gb bb db': 'Gb major', 'g b d': 'G major', 'g# b# d#': 'G# major',
    'ab c eb': 'Ab major', 'a c# e': 'A major', 'a# d e#': 'A# major',
    'bb d f': 'Bb major', 'b d# f#': 'B major',

    #minor chords
    'c eb g': 'C minor', 'c# e g#': 'C# minor',
    'db fb ab': 'Db minor', 'd f a': 'D minor', 'd# f# a#': 'D# minor',
    'eb gb bb': 'Eb minor', 'e g b': 'E minor', 'e# g# b#': 'E# minor',
    'f ab c': 'F minor', 'f# a c#': 'F# minor',
    'gb a db': 'Gb minor', 'g bb d': 'G minor',
    'ab cb eb': 'Ab minor', 'a c e': 'A minor', 'a# c# e#': 'A# minor',
    'bb db f': 'Bb minor', 'b d f#': 'B minor',

    #dim chords
    'c eb gb': 'C dim', 'c# e g': 'C# dim',
    'db fb g': 'Db dim', 'd f ab': 'D dim', 'd# f# a': 'D# dim',
    'eb gb a': 'Eb dim', 'e g bb': 'E dim',
    'f ab cb': 'F dim', 'f# a c': 'F# dim',
    'gb a c': 'Gb dim', 'g bb db': 'G dim', 'g# b d': 'G# dim',
    'ab cb d': 'Ab dim', 'a c eb': 'A dim', 'a# c# e': 'A# dim',
    'bb db fb': 'Bb dim', 'b d f': 'B dim',

    #aug chords
    'c e g#': 'C aug', 'c# e# a': 'C# aug',
    'db f a': 'Db aug', 'd f# a#': 'D aug', 'd# g b': 'D# aug',
    'eb g b': 'Eb aug', 'e g# b#': 'E aug',
    'f a c#': 'F aug', 'f# a# d': 'F# aug',
    'gb bb d': 'Gb aug', 'g b d#': 'G aug', 'ab c e': 'Ab aug',
    'a c# e#': 'A aug', 'bb d f#': 'Bb aug', 'b d# g': 'B aug',

    #sus2 chords
    'c d g': 'C sus2', 'c# d# g#': 'C# sus2',
    'db eb ab': 'Db sus2', 'd eb a': 'D sus2', 'd# e a#': 'D# sus2',
    'eb f bb': 'Eb sus2', 'e f# b': 'E sus2',
    'f g c': 'F sus2', 'f# g# c#': 'F# sus2',
    'gb ab db': 'Gb sus2', 'g a d': 'G sus2', 'g# a# d#': 'G# sus2',
    'ab bb eb': 'Ab sus2', 'a b e': 'A sus2', 'a# c e#': 'A# sus2',
    'bb c f': 'Bb sus2', 'b c# f#': 'B sus2',

    #sus4 chords
    'c f g': 'C sus4', 'c# f# g#': 'C# sus4',
    'db gb ab': 'Db sus4', 'd g a': 'D sus4', 'd# g# a#': 'D# sus4',
    'eb ab bb': 'Eb sus4', 'e a b': 'E sus4',
    'f bb c': 'F sus4', 'f# b c#': 'F# sus4',
    'gb cb db': 'Gb sus4', 'g c d': 'G sus4', 'g# c# d#': 'G# sus4',
    'ab db eb': 'Ab sus4', 'a d e': 'A sus4', 'a# d# e#': 'A# sus4',
    'bb eb f': 'Bb sus4', 'b e f#': 'B sus4'
}

seventhChordDictionary = {
    #maj7 chords
    'c e g b': 'C maj7', 'c# e# g# b#': 'C# maj7',
    'db f ab c': 'Db maj7','d f# a c#': 'D maj7', 'd# g a# d': 'D# maj7',
    'eb g bb d': 'Eb maj7','e g# b d#': 'E maj7',
    'f a c e': 'F maj7', 'f# a# c# e#': 'F# maj7',
    'gb bb db f': 'Gb maj7', 'g b d f#': 'G maj7', 'g# b# d# g': 'G# maj7',
    'ab c eb g': 'Ab maj7', 'a c# e g#': 'A maj7', 'a# d e# a': 'A# maj7',
    'bb d f a': 'Bb maj7', 'b d# f# a#': 'B maj7',

    #min7 chords
    'c eb g bb': 'C min7', 'c# e g# b': 'C# min7',
    'db fb ab cb': 'Db min7','d f a c': 'D min7', 'd# f# a# c#': 'D# min7',
    'eb gb bb db': 'Eb min7','e g b d': 'E min7',
    'f ab c eb': 'F min7','f# a c# e': 'F# min7',
    'gb a db fb': 'Gb min7', 'g bb d f': 'G min7','g# b d# f#': 'G# min7',
    'ab cb eb gb': 'Ab min7', 'a c e g': 'A min7','a# c# e# g#': 'A# min7',
    'bb db f ab': 'Bb min7', 'b d f# a': 'B min7',

    #dominant seventh chords
    'c e g bb': 'C 7', 'c# e# g# b': 'C# 7',
    'db f ab cb': 'Db 7','d f# a c': 'D 7', 'd# g a# c#': 'D# 7',
    'eb g bb db': 'Eb 7','e g# b d': 'E 7',
    'f a c eb': 'F 7', 'f# a# c# e': 'F# 7',
    'gb bb db fb': 'Gb 7', 'g b d f': 'G 7', 'g# b# d# gb': 'G# 7',
    'ab c eb gb': 'Ab 7', 'a c# e g': 'A 7', 'a# d e# g#': 'A# 7',
    'bb d f ab': 'Bb 7', 'b d# f# a': 'B 7',

    #dim seventh chords
    'c eb gb a': 'C dim7', 'c# e g bb': 'C# dim7',
    'db fb g bb': 'Db dim7','d f ab cb': 'D dim7', 'd# f# a c': 'D# dim7',
    'eb gb a c': 'Eb dim7','e g bb db': 'E dim7',
    'f ab cb d': 'F dim7', 'f# a c eb': 'F# dim7',
    'gb a c eb': 'Gb dim7', 'g bb db fb': 'G dim7', 'g# b d f': 'G# dim7',
    'ab cb d f': 'Ab dim7', 'a c eb gb': 'A dim7', 'a# c# e g': 'A# dim7',
    'bb db fb g': 'Bb dim7', 'b d f ab': 'B dim7',

    #half-dim seventh chords
    'c eb gb bb': 'C min7b5', 'c# e g b': 'C# min7b5',
    'db fb g cb': 'Db min7b5','d f ab c': 'D min7b5','d# f# a c#': 'D# min7b5',
    'eb gb a db': 'Eb min7b5','e g bb d': 'E min7b5',
    'f ab cb eb': 'F min7b5','f# a c e': 'F# min7b5',
    'gb a c fb': 'Gb min7b5', 'g bb db f': 'G min7b5','g# b d f#': 'G# min7b5',
    'ab cb d gb': 'Ab min7b5','a c eb g': 'A min7b5','a# c# e g#': 'A# min7b5',
    'bb db fb ab': 'Bb min7b5', 'b d f a': 'B min7b5',

    #dim major seventh chords
    'c eb gb b': 'C dim Maj7', 'c# e g b#': 'C# dim Maj7',
    'db fb g c': 'Db dim Maj7','d f ab c#': 'D dim Maj7',
    'd# f# a d': 'D# dim Maj7',
    'eb gb a d': 'Eb dim Maj7','e g bb d#': 'E dim Maj7',
    'f ab cb e': 'F dim Maj7','f# a c e#': 'F# dim Maj7',
    'gb a c f': 'Gb dim Maj7', 'g bb db f#': 'G dim Maj7',
    'g# b d g': 'G# dim Maj7',
    'ab cb d g': 'Ab dim Maj7', 'a c eb g#': 'A dim Maj7',
    'a# c# e a': 'A# dim Maj7',
    'bb db fb a': 'Bb min7b5', 'b d f a#': 'B dim Maj7',

    #aug chords
    'ceg#': 'C aug', 'c#e#a': 'C# aug',
    'dbfa': 'Db aug','df#a#': 'D aug', 'd#gb': 'D# aug',
    'ebgb': 'Eb aug','eg#b#': 'E aug',
    'fac#': 'F aug', 'f#a#d': 'F# aug',
    'gbbbd': 'Gb aug', 'gbd#': 'G aug',
    'abce': 'Ab aug','ac#e#': 'A aug',
    'bbdf#': 'Bb aug', 'bd#g': 'B aug',

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
}