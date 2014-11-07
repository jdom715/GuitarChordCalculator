import wx
from ConfigureInput import configureInput
from TriadCalculator import triadCalculator
from SeventhCalculator import seventhCalculator

#Main frame where input is given
class MainFrame(wx.Frame):
    def __init__(self, statusText="Check the FAQ if you have questions!",
                 button="notesButton", title="Guitar Chord Calculator"):
        #Constructor
        wx.Frame.__init__(self, parent=None, size=(300, 500))
        self.SetTitle(title)
        self.MainPanel = MainPanel(self)
        trueButton = getattr(self.MainPanel, button)
        trueButton.SetValue(True)
        self.CreateStatusBar()
        self.SetStatusText(statusText)
        self.Center()

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()

        menu1.Append(1, "&FAQ", "Click this for all your questions!")
        menu1.AppendSeparator()

        menu1.Append(2, "E&xit", "Exit the application.")

        menuBar.Append(menu1, "File")

        self.SetMenuBar(menuBar)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent

        #CREATE THE GENERAL SIZER
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        #ADD WELCOME TEXT
        welcomeString = "Let's figure out your chord!"
        welcomeText = wx.StaticText(self, -1, welcomeString, size=(-1, -1))
        font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL)
        welcomeText.SetFont(font)

        self.sizer.Add(welcomeText, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        #ADD CHOICE BUTTONS
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.notesButton = wx.RadioButton(self, -1,
                                          "Notes", style=wx.RB_GROUP)
        self.notesButton.Bind(wx.EVT_RADIOBUTTON, self.onNotes)
        self.notesButton.SetValue(True)

        self.fretsButton = wx.RadioButton(self, -1, "Frets")
        self.fretsButton.Bind(wx.EVT_RADIOBUTTON, self.onFrets)
        self.fretsButton.SetValue(False)

        self.buttonSizer.AddMany([(self.notesButton, 0,
                                   wx.ALIGN_CENTER | wx.BOTTOM |
                                   wx.RIGHT | wx.TOP, 10),

                                  (self.fretsButton, 0,
                                   wx.ALIGN_RIGHT | wx.BOTTOM |
                                   wx.RIGHT | wx.LEFT | wx.TOP, 10)])

        self.sizer.Add(self.buttonSizer, 0, wx.CENTER)

        #CREATE GRID SIZER FOR ALMOST EVERYTHING ELSE
        self.gridSizer = wx.FlexGridSizer(rows=100, cols=3)

        #make fret choices list
        choices = []
        choices.append('x')
        for i in range(0, 25):
            choices.append('{0}'.format(i))

        #E String
        EStringChoiceList = ['e', 'f', 'f#', 'g', 'g#', 'a',
                             'b', 'c', 'c#', 'd', 'd#', 'x']
        self.EStringLabel = wx.StaticText(self, -1, "E: ")
        self.EStringNotesChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=EStringChoiceList)
        self.EStringFretsChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=choices)
        self.gridSizer.Add(self.EStringLabel, 0,
                           wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.EStringNotesChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.EStringFretsChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.EStringFretsChoice.Hide()

        #A String
        AStringChoiceList = ['a', 'b', 'c', 'c#', 'd', 'd#',
                             'e', 'f', 'f#', 'g', 'g#', 'x']
        self.AStringLabel = wx.StaticText(self, -1, "A: ")
        self.AStringNotesChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=AStringChoiceList)
        self.AStringFretsChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=choices)
        self.gridSizer.Add(self.AStringLabel, 0,
                           wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.AStringNotesChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.AStringFretsChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.AStringFretsChoice.Hide()

        #D String
        DStringChoiceList = ['d', 'd#', 'e', 'f', 'f#', 'g',
                             'g#', 'a', 'b', 'c', 'c#', 'x']
        self.DStringLabel = wx.StaticText(self, -1, "D: ")
        self.DStringNotesChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=DStringChoiceList)
        self.DStringFretsChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=choices)
        self.gridSizer.Add(self.DStringLabel, 0,
                           wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.DStringNotesChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.DStringFretsChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.DStringFretsChoice.Hide()

        #G String
        GStringChoiceList = ['g', 'g#', 'a', 'b', 'c', 'c#',
                             'd', 'd#', 'e', 'f', 'f#', 'x']
        self.GStringLabel = wx.StaticText(self, -1, "G: ")
        self.GStringNotesChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=GStringChoiceList)
        self.GStringFretsChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=choices)
        self.gridSizer.Add(self.GStringLabel, 0,
                           wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.GStringNotesChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.GStringFretsChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.GStringFretsChoice.Hide()

        #B String
        BStringChoiceList = ['b', 'c', 'c#', 'd', 'd#', 'e',
                             'f', 'f#', 'g', 'g#', 'a', 'x']
        self.BStringLabel = wx.StaticText(self, -1, "B: ")
        self.BStringNotesChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=BStringChoiceList)
        self.BStringFretsChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=choices)
        self.gridSizer.Add(self.BStringLabel, 0,
                           wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.BStringNotesChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.BStringFretsChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.BStringFretsChoice.Hide()

        #e String
        self.eStringLabel = wx.StaticText(self, -1, "e: ")
        self.eStringNotesChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=EStringChoiceList)
        self.eStringFretsChoice = wx.Choice(self, -1, size=(70, -1),
                                            choices=choices)
        self.gridSizer.Add(self.eStringLabel, 0,
                           wx.TOP | wx.LEFT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.eStringNotesChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.gridSizer.Add(self.eStringFretsChoice, 0,
                           wx.TOP | wx.RIGHT | wx.BOTTOM | wx.ALIGN_LEFT, 10)
        self.eStringFretsChoice.Hide()


        #ADD GRIDSIZER TO ENTIRE SIZER
        self.sizer.Add(self.gridSizer, 0, wx.ALIGN_CENTER)

        #ADD SEARCH BUTTON
        self.submitButton = wx.Button(self, 10, "Search")
        self.Bind(wx.EVT_BUTTON, self.OnSubmit, self.submitButton)
        self.sizer.Add(self.submitButton, 0,
                       wx.ALIGN_CENTER | wx.TOP | wx.LEFT | wx.BOTTOM, 10)

        self.SetSizer(self.sizer)

    def onFrets(self, event):
        #HIDE NOTE CHOICES AND REVEAL FRET CHOICES

        #E String
        self.EStringNotesChoice.Hide()
        self.EStringFretsChoice.Show()

        #A String
        self.AStringNotesChoice.Hide()
        self.AStringFretsChoice.Show()

        #D String
        self.DStringNotesChoice.Hide()
        self.DStringFretsChoice.Show()

        #G String
        self.GStringNotesChoice.Hide()
        self.GStringFretsChoice.Show()

        #B String
        self.BStringNotesChoice.Hide()
        self.BStringFretsChoice.Show()

        #e String
        self.eStringNotesChoice.Hide()
        self.eStringFretsChoice.Show()

        self.sizer.Layout()

    def onNotes(self, event):
        #HIDE FRET CHOICES AND REVEAL NOTE CHOICES

        #E String
        self.EStringFretsChoice.Hide()
        self.EStringNotesChoice.Show()

        #A String
        self.AStringFretsChoice.Hide()
        self.AStringNotesChoice.Show()

        #D String
        self.DStringFretsChoice.Hide()
        self.DStringNotesChoice.Show()

        #G String
        self.GStringFretsChoice.Hide()
        self.GStringNotesChoice.Show()

        #B String
        self.BStringFretsChoice.Hide()
        self.BStringNotesChoice.Show()

        #e String
        self.eStringFretsChoice.Hide()
        self.eStringNotesChoice.Show()

        self.sizer.Layout()

    def OnSubmit(self, event):
        isNotes = False
        #IF NOTES
        if self.notesButton.GetValue():
            noteList = [self.EStringNotesChoice.GetStringSelection(),
                        self.AStringNotesChoice.GetStringSelection(),
                        self.DStringNotesChoice.GetStringSelection(),
                        self.GStringNotesChoice.GetStringSelection(),
                        self.BStringNotesChoice.GetStringSelection(),
                        self.eStringNotesChoice.GetStringSelection()]

            isNotes = True

        else:
            noteList = [self.EStringFretsChoice.GetStringSelection(),
                        self.AStringFretsChoice.GetStringSelection(),
                        self.DStringFretsChoice.GetStringSelection(),
                        self.GStringFretsChoice.GetStringSelection(),
                        self.BStringFretsChoice.GetStringSelection(),
                        self.eStringFretsChoice.GetStringSelection()]
        
        # CONFIGURE INPUT
        inputList = configureInput(noteList, isNotes)
        noteList = inputList[0]
        alternateNoteList = inputList[1]
        bassNote = inputList[2]
        alternateBassNote = inputList[3]

        # CALCULATE CHORD
        chordList = []
        if len(noteList) == 3:
            chordList = triadCalculator(noteList, alternateNoteList)
        elif len(noteList) == 4:
            chordList = seventhCalculator(noteList, alternateNoteList)

        chordString = chordList[0]
        chordBass = chordList[1]
        chordType = chordList[2]
        print chordString
        print chordBass
        print chordType

        # PRINT RESULTS
        if bassNote == chordBass:
            print('\nYour chord is {0}!'.format(chordType))
        else:
            print('\nYour chord is {0} with {1} in the bass.'.format(
                chordType, bassNote.upper()))
                

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()

