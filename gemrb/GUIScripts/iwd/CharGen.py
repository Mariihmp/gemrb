#Character Generation
import GemRB


CharGenWindow = 0
CharGenState = 0
TextArea = 0
PortraitButton = 0

GenderButton = 0
GenderWindow = 0
GenderTextArea = 0
GenderDoneButton = 0

Portrait = 0
PortraitTable = 0
PortraitPortraitButton = 0

RaceButton = 0
RaceWindow = 0
RaceTable = 0
RaceTextArea = 0
RaceDoneButton = 0

ClassButton = 0
ClassWindow = 0
ClassTable = 0
ClassTextArea = 0
ClassDoneButton = 0

AlignmentButton = 0
AlignmentWindow = 0
AlignmentTable = 0
AlignmentTextArea = 0
AlignmentDoneButton = 0

AbilitiesButton = 0
AbilitiesWindow = 0
AbilitiesTable = 0
AbilitiesRaceAddTable = 0
AbilitiesRaceReqTable = 0
AbilitiesClassReqTable = 0
AbilitiesMinimum = 0
AbilitiesMaximum = 0
AbilitiesModifier = 0
AbilitiesTextArea = 0
AbilitiesRecallButton = 0
AbilitiesDoneButton = 0

SkillsButton = 0
SkillsWindow = 0
SkillsTable = 0
SkillsTextArea = 0
SkillsDoneButton = 0
SkillsPointsLeft = 0
SkillsState = 0

ProficienciesWindow = 0
ProficienciesTable = 0
ProfsMaxTable = 0
ProficienciesTextArea = 0
ProficienciesDoneButton = 0
ProficienciesPointsLeft = 0

MageSpellsWindow = 0
MageSpellsTextArea = 0
MageSpellsDoneButton = 0

AppearanceButton = 0
AppearanceWindow = 0
AppearanceTable = 0
AppearanceDoneButton = 0

BiographyButton = 0
BiographyWindow = 0
BiographyDoneButton = 0

NameButton = 0
NameWindow = 0
NameDoneButton = 0


def OnLoad():
	global CharGenWindow, CharGenState, TextArea, PortraitButton
	global GenderButton, RaceButton, ClassButton, AlignmentButton, AbilitiesButton, SkillsButton, AppearanceButton, BiographyButton, NameButton

	GemRB.LoadWindowPack("GUICG")
	CharGenWindow = GemRB.LoadWindow(0)
	CharGenState = 0

        GenderButton = GemRB.GetControl(CharGenWindow, 0)
	GemRB.SetButtonState(CharGenWindow, GenderButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharGenWindow, GenderButton, IE_GUI_BUTTON_ON_PRESS, "GenderPress")
	GemRB.SetText(CharGenWindow, GenderButton, 11956)

        RaceButton = GemRB.GetControl(CharGenWindow, 1)
	GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, RaceButton, IE_GUI_BUTTON_ON_PRESS, "RacePress")
	GemRB.SetText(CharGenWindow, RaceButton, 11957)

        ClassButton = GemRB.GetControl(CharGenWindow, 2)
	GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, ClassButton, IE_GUI_BUTTON_ON_PRESS, "ClassPress")
	GemRB.SetText(CharGenWindow, ClassButton, 11959)

        AlignmentButton = GemRB.GetControl(CharGenWindow, 3)
	GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentPress")
	GemRB.SetText(CharGenWindow, AlignmentButton, 11958)

        AbilitiesButton = GemRB.GetControl(CharGenWindow, 4)
	GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesPress")
	GemRB.SetText(CharGenWindow, AbilitiesButton, 11960)

        SkillsButton = GemRB.GetControl(CharGenWindow, 5)
	GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, SkillsButton, IE_GUI_BUTTON_ON_PRESS, "SkillsPress")
	GemRB.SetText(CharGenWindow, SkillsButton, 11983)

        AppearanceButton = GemRB.GetControl(CharGenWindow, 6)
	GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_ON_PRESS, "AppearancePress")
	GemRB.SetText(CharGenWindow, AppearanceButton, 11961)

        BiographyButton = GemRB.GetControl(CharGenWindow, 16)
	GemRB.SetButtonState(CharGenWindow, BiographyButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, BiographyButton, IE_GUI_BUTTON_ON_PRESS, "BiographyPress")
	GemRB.SetText(CharGenWindow, BiographyButton, 18003)

        NameButton = GemRB.GetControl(CharGenWindow, 7)
	GemRB.SetButtonState(CharGenWindow, NameButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, NameButton, IE_GUI_BUTTON_ON_PRESS, "NamePress")
	GemRB.SetText(CharGenWindow, NameButton, 11963)

	BackButton = GemRB.GetControl(CharGenWindow, 11)
	GemRB.SetButtonState(CharGenWindow, BackButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharGenWindow, BackButton, IE_GUI_BUTTON_ON_PRESS, "BackPress")

	PortraitButton = GemRB.GetControl(CharGenWindow, 12)
	GemRB.SetButtonFlags(CharGenWindow, PortraitButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_NO_IMAGE, OP_SET)

	ImportButton = GemRB.GetControl(CharGenWindow, 13)
	GemRB.SetButtonState(CharGenWindow, ImportButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetText(CharGenWindow, ImportButton, 13955)
	GemRB.SetEvent(CharGenWindow, ImportButton, IE_GUI_BUTTON_ON_PRESS, "ImportPress")

	CancelButton = GemRB.GetControl(CharGenWindow, 15)
	GemRB.SetButtonState(CharGenWindow, CancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetText(CharGenWindow, CancelButton, 13727)
	GemRB.SetEvent(CharGenWindow, CancelButton, IE_GUI_BUTTON_ON_PRESS, "CancelPress")

	BackButton = GemRB.GetControl(CharGenWindow, 11)
	GemRB.SetButtonState(CharGenWindow, BackButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(CharGenWindow, BackButton, IE_GUI_BUTTON_ON_PRESS, "BackPress")

	AcceptButton = GemRB.GetControl(CharGenWindow, 8)
	GemRB.SetButtonState(CharGenWindow, AcceptButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetText(CharGenWindow, AcceptButton, 11962)
	GemRB.SetEvent(CharGenWindow, AcceptButton, IE_GUI_BUTTON_ON_PRESS, "AcceptPress")

	TextArea = GemRB.GetControl(CharGenWindow, 9)
	GemRB.SetText(CharGenWindow, TextArea, 16575)

	GemRB.SetVisible(CharGenWindow, 1)
	return

def BackPress():
	global CharGenWindow, CharGenState
	global GenderButton, RaceButton, ClassButton, AlignmentButton, AbilitiesButton, SkillsButton, AppearanceButton, BiographyButton, NameButton
	if CharGenState > 0:
		CharGenState = CharGenState - 1
	if CharGenState == 0:
		GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, GenderButton, IE_GUI_BUTTON_ENABLED)
	elif CharGenState == 1:
		GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_ENABLED)
	elif CharGenState == 2:
		GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_ENABLED)
	elif CharGenState == 3:
		GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_ENABLED)
	elif CharGenState == 4:
		GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_ENABLED)
	elif CharGenState == 5:
		GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_ENABLED)
	elif CharGenState == 6:
		GemRB.SetButtonState(CharGenWindow, NameButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, BiographyButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_ENABLED)
	SetCharacterDescription()
	return

def SetCharacterDescription():
	global CharGenWindow, TextArea, CharGenState, ClassTable, RaceTable, AlignmentTable, AbilitiesTable, ProficienciesTable
	GemRB.TextAreaClear(CharGenWindow, TextArea)
	if CharGenState > 0:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 12135)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		if GemRB.GetVar("Gender") == 1:
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 1050)
		else:
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 1051)
	if CharGenState > 2:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 12136, -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(ClassTable, GemRB.GetVar("Class") - 1, 2) )
	if CharGenState > 1:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 1048, -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(RaceTable, GemRB.GetVar("Race") - 1, 2) )
	if CharGenState > 3:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 1049, -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, ": ")
		GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(AlignmentTable, GemRB.GetVar("Alignment") - 1, 2) )
	if CharGenState > 4:
		GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
		for i in range(0, 6):
			GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(AbilitiesTable, i, 2), -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Ability" + str(i + 1))) )
	if CharGenState > 5:
		ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
		if ClassName == "THIEF" or ClassName == "FIGHTER_THIEF" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF" or ClassName == "CLERIC_THIEF":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 8442, -1)
			for i in range (0, 4):
				GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(SkillsTable, i, 2), -1)
				GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
				GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Skill" + str(i))) )
		if ClassName == "RANGER":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 8442, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(SkillsTable, 0, 2), -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Skill0")) )
		if ClassName == "BARD":
			GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, 8442, -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(SkillsTable, 2, 2), -1)
			GemRB.TextAreaAppend(CharGenWindow, TextArea, ": " )
			GemRB.TextAreaAppend(CharGenWindow, TextArea, str(GemRB.GetVar("Skill2")) )

		GemRB.TextAreaAppend(CharGenWindow, TextArea, "", -1)
		GemRB.TextAreaAppend(CharGenWindow, TextArea, 9466, -1)
		for i in range(0,15):
			ProficiencyValue = GemRB.GetVar("Proficiency" + str(i) )
			if ProficiencyValue > 0:
				GemRB.TextAreaAppend(CharGenWindow, TextArea, GemRB.GetTableValue(ProficienciesTable, i, 2), -1)
				j = 0
				while j < ProficiencyValue:
					GemRB.TextAreaAppend(CharGenWindow, TextArea, "+")
					j = j + 1
	return


# Gender Selection

def GenderPress():
	global CharGenWindow, GenderWindow, GenderDoneButton, GenderTextArea
	GemRB.SetVisible(CharGenWindow, 0)
	GenderWindow = GemRB.LoadWindow(1)
	GemRB.SetVar("Gender", 0)

	MaleButton = GemRB.GetControl(GenderWindow, 2)
	GemRB.SetButtonState(GenderWindow, MaleButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(GenderWindow, MaleButton, IE_GUI_BUTTON_ON_PRESS, "MalePress")

	FemaleButton = GemRB.GetControl(GenderWindow, 3)
	GemRB.SetButtonState(GenderWindow, FemaleButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(GenderWindow, FemaleButton, IE_GUI_BUTTON_ON_PRESS, "FemalePress")

	GenderTextArea = GemRB.GetControl(GenderWindow, 5)
	GemRB.SetText(GenderWindow, GenderTextArea, 17236)

	GenderDoneButton = GemRB.GetControl(GenderWindow, 0)
	GemRB.SetButtonState(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_ON_PRESS, "GenderDonePress")
	GemRB.SetText(GenderWindow, GenderDoneButton, 11973)
	GemRB.SetButtonFlags(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	GenderCancelButton = GemRB.GetControl(GenderWindow, 6)
	GemRB.SetButtonState(GenderWindow, GenderCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(GenderWindow, GenderCancelButton, IE_GUI_BUTTON_ON_PRESS, "GenderCancelPress")
	GemRB.SetText(GenderWindow, GenderCancelButton, 13727)
	
	GemRB.SetVisible(GenderWindow, 1)
	return

def MalePress():
	global GenderWindow, GenderDoneButton, GenderTextArea
	GemRB.SetVar("Gender", 1)
	GemRB.SetText(GenderWindow, GenderTextArea, 13083)
	GemRB.SetButtonState(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def FemalePress():
	global GenderWindow, GenderDoneButton, GenderTextArea
	GemRB.SetVar("Gender", 2)
	GemRB.SetText(GenderWindow, GenderTextArea, 13084)
	GemRB.SetButtonState(GenderWindow, GenderDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def GenderDonePress():
	global CharGenWindow, GenderWindow
	GemRB.UnloadWindow(GenderWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	PortraitSelect()
	return
	
def GenderCancelPress():
	global CharGenWindow, GenderWindow, Gender
	GemRB.SetVar("Gender", 0)
	GemRB.UnloadWindow(GenderWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return

def PortraitSelect():
	global CharGenWindow, PortraitWindow, Portrait, PortraitPortraitButton, PortraitTable
	GemRB.SetVisible(CharGenWindow, 0)
	PortraitWindow = GemRB.LoadWindow(11)

	# this is not the correct one, but I don't know which is
	PortraitTable = GemRB.LoadTable("PICTURES")
	Portrait = 0;
	
	PortraitPortraitButton = GemRB.GetControl(PortraitWindow, 1)
	GemRB.SetButtonFlags(PortraitWindow, PortraitPortraitButton, IE_GUI_BUTTON_PICTURE|IE_GUI_BUTTON_NO_IMAGE, OP_SET)

	PortraitLeftButton = GemRB.GetControl(PortraitWindow, 2)
	GemRB.SetButtonState(PortraitWindow, PortraitLeftButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitLeftButton, IE_GUI_BUTTON_ON_PRESS, "PortraitLeftPress")
	
	PortraitRightButton = GemRB.GetControl(PortraitWindow, 3)
	GemRB.SetButtonState(PortraitWindow, PortraitRightButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitRightButton, IE_GUI_BUTTON_ON_PRESS, "PortraitRightPress")

	PortraitCustomButton = GemRB.GetControl(PortraitWindow, 6)
	GemRB.SetButtonState(PortraitWindow, PortraitCustomButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitCustomButton, IE_GUI_BUTTON_ON_PRESS, "PortraitCustomPress")
	GemRB.SetText(PortraitWindow, PortraitCustomButton, 17545)

	PortraitDoneButton = GemRB.GetControl(PortraitWindow, 0)
	GemRB.SetButtonState(PortraitWindow, PortraitDoneButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitDoneButton, IE_GUI_BUTTON_ON_PRESS, "PortraitDonePress")
	GemRB.SetText(PortraitWindow, PortraitDoneButton, 11973)
	GemRB.SetButtonFlags(PortraitWindow, PortraitDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	PortraitCancelButton = GemRB.GetControl(PortraitWindow, 5)
	GemRB.SetButtonState(PortraitWindow, PortraitCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(PortraitWindow, PortraitCancelButton, IE_GUI_BUTTON_ON_PRESS, "PortraitCancelPress")
	GemRB.SetText(PortraitWindow, PortraitCancelButton, 13727)

	while GemRB.GetTableValue(PortraitTable, Portrait, 0) != GemRB.GetVar("Gender"):
		Portrait = Portrait + 1
	GemRB.SetButtonPicture(PortraitWindow, PortraitPortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "G")

	GemRB.SetVisible(PortraitWindow, 1)
	return

def PortraitLeftPress():
	global PortraitWindow, Portrait, PortraitTable, PortraitPortraitButton
	while True:
		Portrait = Portrait - 1
		if Portrait < 0:
			Portrait = GemRB.GetTableRowCount(PortraitTable) - 1
		if GemRB.GetTableValue(PortraitTable, Portrait, 0) == GemRB.GetVar("Gender"):
			GemRB.SetButtonPicture(PortraitWindow, PortraitPortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "G")
			return
	
def PortraitRightPress():
	global PortraitWindow, Portrait, PortraitTable, PortraitPortraitButton
	while True:
		Portrait = Portrait + 1
		if Portrait == GemRB.GetTableRowCount(PortraitTable):
			Portrait = 0
		if GemRB.GetTableValue(PortraitTable, Portrait, 0) == GemRB.GetVar("Gender"):
			GemRB.SetButtonPicture(PortraitWindow, PortraitPortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "G")
			return

def PortraitCustomPress():
	return

def PortraitDonePress():
	global CharGenWindow, CharGenState, PortraitWindow, PortraitButton, PortraitTable, Portrait, GenderButton, RaceButton
	GemRB.UnloadWindow(PortraitWindow)
	GemRB.SetButtonPicture(CharGenWindow, PortraitButton, GemRB.GetTableRowName(PortraitTable, Portrait) + "L")
	GemRB.SetButtonState(CharGenWindow, GenderButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_ENABLED)
	CharGenState = 1
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def PortraitCancelPress():
	global CharGenWindow, PortraitWindow
	GemRB.UnloadWindow(PortraitWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Race Selection

def RacePress():
	global CharGenWindow, RaceWindow, RaceDoneButton, RaceTable, RaceTextArea
	GemRB.SetVisible(CharGenWindow, 0)
	RaceWindow = GemRB.LoadWindow(8)
	RaceTable = GemRB.LoadTable("RACES")
	GemRB.SetVar("Race", 0)

	for i in range(2, 8):
		RaceSelectButton = GemRB.GetControl(RaceWindow, i)
		GemRB.SetButtonFlags(RaceWindow, RaceSelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_OR)
	
	for i in range(2, 8):
		RaceSelectButton = GemRB.GetControl(RaceWindow, i)
		GemRB.SetButtonState(RaceWindow, RaceSelectButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(RaceWindow, RaceSelectButton, IE_GUI_BUTTON_ON_PRESS, "RaceSelectPress")
		GemRB.SetText(RaceWindow, RaceSelectButton, GemRB.GetTableValue(RaceTable, i - 2, 0))
		GemRB.SetVarAssoc(RaceWindow, RaceSelectButton, "Race", i - 1)

	RaceTextArea = GemRB.GetControl(RaceWindow, 8)
	GemRB.SetText(RaceWindow, RaceTextArea, 17237)

	RaceDoneButton = GemRB.GetControl(RaceWindow, 0)
	GemRB.SetButtonState(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_ON_PRESS, "RaceDonePress")
	GemRB.SetText(RaceWindow, RaceDoneButton, 11973)
	GemRB.SetButtonFlags(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	RaceCancelButton = GemRB.GetControl(RaceWindow, 10)
	GemRB.SetButtonState(RaceWindow, RaceCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(RaceWindow, RaceCancelButton, IE_GUI_BUTTON_ON_PRESS, "RaceCancelPress")
	GemRB.SetText(RaceWindow, RaceCancelButton, 13727)

	GemRB.SetVisible(RaceWindow, 1)
	return

def RaceSelectPress():
        global RaceWindow, RaceDoneButton, RaceTable, RaceTextArea
	Race = GemRB.GetVar("Race") - 1
	GemRB.SetText(RaceWindow, RaceTextArea, GemRB.GetTableValue(RaceTable, Race, 1) )
        GemRB.SetButtonState(RaceWindow, RaceDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def RaceDonePress():
	global CharGenWindow, CharGenState, RaceWindow, RaceButton, ClassButton
	GemRB.UnloadWindow(RaceWindow)
	GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_ENABLED)
	CharGenState = 2
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def BackToRacePress():
	GemRB.SetVar("Race", 0)
	GemRB.SetButtonState(CharGenWindow, RaceButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(CharGenWindow, BackButton, IE_GUI_BUTTON_ON_PRESS, "OnLoad")
	return

def RaceCancelPress():
	global CharGenWindow, RaceWindow
	GemRB.SetVar("Race", 0)
	GemRB.UnloadWindow(RaceWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return

# Class Selection

def ClassPress():
	global CharGenWindow, ClassWindow, ClassTable, ClassTextArea, ClassDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	ClassWindow = GemRB.LoadWindow(2)
	ClassTable = GemRB.LoadTable("CLASSES")
	ClassCount = GemRB.GetTableRowCount(ClassTable)
	RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
	GemRB.SetVar("Class", 0)

	for i in range(2, 10):
		ClassSelectButton = GemRB.GetControl(ClassWindow, i)
		GemRB.SetButtonFlags(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_SET)

	HasMulti = 0
	for i in range(0, ClassCount):
		Allowed = GemRB.GetTableValue(ClassTable, GemRB.GetTableRowName(ClassTable, i), RaceName)
		if GemRB.GetTableValue(ClassTable, i, 4):
			if Allowed != 0:
				HasMulti = 1
		else:
			ClassSelectButton = GemRB.GetControl(ClassWindow, i + 2)
			if Allowed > 0:
				GemRB.SetButtonState(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_ENABLED)
			else:
				GemRB.SetButtonState(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetEvent(ClassWindow, ClassSelectButton, IE_GUI_BUTTON_ON_PRESS,  "ClassSelectPress")
			GemRB.SetText(ClassWindow, ClassSelectButton, GemRB.GetTableValue(ClassTable, i, 0) )
			GemRB.SetVarAssoc(ClassWindow, ClassSelectButton , "Class", i + 1)

        ClassMultiButton = GemRB.GetControl(ClassWindow, 10)
	if HasMulti == 0:
		GemRB.SetButtonState(ClassWindow, ClassMultiButton, IE_GUI_BUTTON_DISABLED)
	else:
		GemRB.SetButtonState(ClassWindow, ClassMultiButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassWindow, ClassMultiButton, IE_GUI_BUTTON_ON_PRESS, "ClassMultiPress")
	GemRB.SetText(ClassWindow, ClassMultiButton, 11993)
	
        ClassSpecialButton = GemRB.GetControl(ClassWindow, 11)
	GemRB.SetButtonState(ClassWindow, ClassSpecialButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassWindow, ClassSpecialButton, IE_GUI_BUTTON_ON_PRESS, "ClassSpecialPress")
	GemRB.SetText(ClassWindow, ClassSpecialButton, 11994)

	ClassDoneButton = GemRB.GetControl(ClassWindow, 0)
	GemRB.SetButtonState(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_ON_PRESS, "ClassDonePress")
	GemRB.SetText(ClassWindow, ClassDoneButton, 11973)
	GemRB.SetButtonFlags(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	ClassCancelButton = GemRB.GetControl(ClassWindow, 14)
	GemRB.SetButtonState(ClassWindow, ClassCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ClassWindow, ClassCancelButton, IE_GUI_BUTTON_ON_PRESS, "ClassCancelPress")
	GemRB.SetText(ClassWindow, ClassCancelButton, 13727)

	ClassTextArea = GemRB.GetControl(ClassWindow, 13)
	GemRB.SetText(ClassWindow, ClassTextArea, 17242)

	GemRB.SetVisible(ClassWindow, 1)
	return

def ClassSelectPress():
	global ClassWindow, ClassTable, ClassTextArea, ClassDoneButton
	Class = GemRB.GetVar("Class") - 1
	GemRB.SetText(ClassWindow, ClassTextArea, GemRB.GetTableValue(ClassTable, Class, 1) )
	GemRB.SetButtonState(ClassWindow, ClassDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def ClassMultiPress():
	return

def ClassSpecialPress():
	return

def ClassDonePress():
	global CharGenWindow, CharGenState, ClassWindow, ClassButton, AlignmentButton
	GemRB.UnloadWindow(ClassWindow)
	GemRB.SetButtonState(CharGenWindow, ClassButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_ENABLED)
	CharGenState = 3
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def ClassCancelPress():
	global CharGenWindow, ClassWindow
	GemRB.UnloadWindow(ClassWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Alignment Selection

def AlignmentPress():
	global CharGenWindow, AlignmentWindow, AlignmentTable, AlignmentTextArea, AlignmentDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	AlignmentWindow = GemRB.LoadWindow(3)
	AlignmentTable = GemRB.LoadTable("ALIGNS")
	ClassAlignmentTable = GemRB.LoadTable("ALIGNMNT")
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	GemRB.SetVar("Alignment", 0)
	
	for i in range (2, 11):
		AlignmentSelectButton = GemRB.GetControl(AlignmentWindow, i)
		GemRB.SetButtonFlags(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_RADIOBUTTON, OP_OR)

	for i in range (0, 9):
		AlignmentSelectButton = GemRB.GetControl(AlignmentWindow, i + 2)
		if GemRB.GetTableValue(ClassAlignmentTable, ClassName, GemRB.GetTableValue(AlignmentTable, i, 4)) == 0:
			GemRB.SetButtonState(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_DISABLED)
		else:
			GemRB.SetButtonState(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AlignmentWindow, AlignmentSelectButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentSelectPress")
		GemRB.SetText(AlignmentWindow, AlignmentSelectButton, GemRB.GetTableValue(AlignmentTable, i, 0) )
		GemRB.SetVarAssoc(AlignmentWindow, AlignmentSelectButton, "Alignment", i + 1)

	AlignmentTextArea = GemRB.GetControl(AlignmentWindow, 11)
	GemRB.SetText(AlignmentWindow, AlignmentTextArea, 9602)

	AlignmentDoneButton = GemRB.GetControl(AlignmentWindow, 0)
	GemRB.SetButtonState(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentDonePress")
	GemRB.SetText(AlignmentWindow, AlignmentDoneButton, 11973)
	GemRB.SetButtonFlags(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	AlignmentCancelButton = GemRB.GetControl(AlignmentWindow, 13)
	GemRB.SetButtonState(AlignmentWindow, AlignmentCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AlignmentWindow, AlignmentCancelButton, IE_GUI_BUTTON_ON_PRESS, "AlignmentCancelPress")
	GemRB.SetText(AlignmentWindow, AlignmentCancelButton, 13727)

	GemRB.SetVisible(AlignmentWindow, 1)
	return


def AlignmentSelectPress():
	global AlignmentWindow, AlignmentTable, AlignmentTextArea, AlignmentDoneButton
	Alignment = GemRB.GetVar("Alignment") - 1 
	GemRB.SetText(AlignmentWindow, AlignmentTextArea, GemRB.GetTableValue(AlignmentTable, Alignment, 1))
	GemRB.SetButtonState(AlignmentWindow, AlignmentDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def AlignmentDonePress():
	global CharGenWindow, CharGenState, AlignmentWindow, AlignmentButton, AbilitiesButton
	GemRB.UnloadWindow(AlignmentWindow)
	GemRB.SetButtonState(CharGenWindow, AlignmentButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_ENABLED)
	CharGenState = 4
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def AlignmentCancelPress():
	global CharGenWindow, AlignmentWindow
	GemRB.UnloadWindow(AlignmentWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Abilities Selection

def AbilitiesPress():
	global CharGenWindow, AbilitiesWindow, AbilitiesTable, AbilitiesRaceAddTable, AbilitiesRaceReqTable, AbilitiesClassReqTable, AbilitiesTextArea, AbilitiesRecallButton, AbilitiesDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	AbilitiesWindow = GemRB.LoadWindow(4)
	AbilitiesTable = GemRB.LoadTable("ABILITY")
	AbilitiesRaceAddTable = GemRB.LoadTable("ABRACEAD")
	AbilitiesRaceReqTable = GemRB.LoadTable("ABRACERQ")
	AbilitiesClassReqTable = GemRB.LoadTable("ABCLASRQ")

	PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
	GemRB.SetLabelUseRGB(AbilitiesWindow, PointsLeftLabel, 1)
	
	for i in range (0, 6):
		AbilitiesLabelButton = GemRB.GetControl(AbilitiesWindow, 30 + i)
		GemRB.SetButtonState(AbilitiesWindow, AbilitiesLabelButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AbilitiesWindow, AbilitiesLabelButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesLabelPress")
		GemRB.SetVarAssoc(AbilitiesWindow, AbilitiesLabelButton, "AbilityIndex", i + 1)

		AbilitiesPlusButton = GemRB.GetControl(AbilitiesWindow, 16 + i * 2)
		GemRB.SetButtonState(AbilitiesWindow, AbilitiesPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AbilitiesWindow, AbilitiesPlusButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesPlusPress")
		GemRB.SetVarAssoc(AbilitiesWindow, AbilitiesPlusButton, "AbilityIndex", i + 1)

		AbilitiesMinusButton = GemRB.GetControl(AbilitiesWindow, 17 + i * 2)
		GemRB.SetButtonState(AbilitiesWindow, AbilitiesMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(AbilitiesWindow, AbilitiesMinusButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesMinusPress")
		GemRB.SetVarAssoc(AbilitiesWindow, AbilitiesMinusButton, "AbilityIndex", i + 1)

		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + i)
		GemRB.SetLabelUseRGB(AbilitiesWindow, AbilityLabel, 1)

	AbilitiesRerollPress()

	AbilitiesStoreButton = GemRB.GetControl(AbilitiesWindow, 37)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesStoreButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesStoreButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesStorePress")
	GemRB.SetText(AbilitiesWindow, AbilitiesStoreButton, 17373)
	
	AbilitiesRecallButton = GemRB.GetControl(AbilitiesWindow, 38)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesRecallButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesRecallButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesRecallPress")
	GemRB.SetText(AbilitiesWindow, AbilitiesRecallButton, 17374)
	
	AbilitiesRerollButton = GemRB.GetControl(AbilitiesWindow,2)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesRerollButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesRerollButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesRerollPress")
	GemRB.SetText(AbilitiesWindow, AbilitiesRerollButton, 11982)

	AbilitiesTextArea = GemRB.GetControl(AbilitiesWindow, 29)
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, 17247)

	AbilitiesDoneButton = GemRB.GetControl(AbilitiesWindow, 0)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesDoneButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesDoneButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesDonePress")
	GemRB.SetText(AbilitiesWindow, AbilitiesDoneButton, 11973)
	GemRB.SetButtonFlags(AbilitiesWindow, AbilitiesDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	AbilitiesCancelButton = GemRB.GetControl(AbilitiesWindow, 36)
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AbilitiesWindow, AbilitiesCancelButton, IE_GUI_BUTTON_ON_PRESS, "AbilitiesCancelPress")
	GemRB.SetText(AbilitiesWindow, AbilitiesCancelButton, 13727)

	GemRB.SetVisible(AbilitiesWindow, 1)
	return

def AbilitiesCalcLimits(Index):
	global RaceTable, AbilitiesRaceReqTable, AbilitiesRaceAddTable, ClassTable, AbilitiesClassReqTable
	global AbilitiesMinimum, AbilitiesMaximum, AbilitiesModifier
	RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
	Race = GemRB.GetTableRowIndex(AbilitiesRaceReqTable, RaceName)
	AbilitiesMinimum = GemRB.GetTableValue(AbilitiesRaceReqTable, Race, Index * 2)
	AbilitiesMaximum = GemRB.GetTableValue(AbilitiesRaceReqTable, Race, Index * 2 + 1)
	AbilitiesModifier = GemRB.GetTableValue(AbilitiesRaceAddTable, Race, Index)

	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	Class = GemRB.GetTableRowIndex(AbilitiesClassReqTable, ClassName)
	Min = GemRB.GetTableValue(AbilitiesClassReqTable, Class, Index)
	if Min > 0 and AbilitiesMinimum < Min:
		AbilitiesMinimum = Min

	AbilitiesMinimum = AbilitiesMinimum + AbilitiesModifier
	AbilitiesMaximum = AbilitiesMaximum + AbilitiesModifier
	return

def AbilitiesLabelPress():
	global AbilitiesWindow, AbilitiesTable, AbilitiesTextArea
	AbilityIndex = GemRB.GetVar("AbilityIndex") - 1
	AbilitiesCalcLimits(AbilityIndex)
	GemRB.SetToken("MINIMUM", str(AbilitiesMinimum) )
	GemRB.SetToken("MAXIMUM", str(AbilitiesMaximum) )
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, GemRB.GetTableValue(AbilitiesTable, AbilityIndex, 1) )
	return

def AbilitiesPlusPress():
	global AbilitiesWindow, AbilitiesTable, AbilitiesTextArea, AbilitiesMinimum, AbilitiesMaximum
	AbilityIndex = GemRB.GetVar("AbilityIndex") - 1
	AbilitiesCalcLimits(AbilityIndex)
	GemRB.SetToken("MINIMUM", str(AbilitiesMinimum) )
	GemRB.SetToken("MAXIMUM", str(AbilitiesMaximum) )
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, GemRB.GetTableValue(AbilitiesTable, AbilityIndex, 1) )
	PointsLeft = GemRB.GetVar("Ability0")
	Ability = GemRB.GetVar("Ability" + str(AbilityIndex + 1) )
	if PointsLeft > 0 and Ability < AbilitiesMaximum:
		PointsLeft = PointsLeft - 1
		GemRB.SetVar("Ability0", PointsLeft)
		PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
		GemRB.SetText(AbilitiesWindow, PointsLeftLabel, str(PointsLeft) )
		Ability = Ability + 1
		GemRB.SetVar("Ability" + str(AbilityIndex + 1), Ability)
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + AbilityIndex)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(Ability) )
		if PointsLeft == 0:
			GemRB.SetButtonState(AlignmentWindow, AbilitiesDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def AbilitiesMinusPress():
	global AbilitiesWindow, AbilitiesTable, AbilitiesTextArea, AbilitiesMinimum, AbilitiesMaximum
	AbilityIndex = GemRB.GetVar("AbilityIndex") - 1
	AbilitiesCalcLimits(AbilityIndex)
	GemRB.SetToken("MINIMUM", str(AbilitiesMinimum) )
	GemRB.SetToken("MAXIMUM", str(AbilitiesMaximum) )
	GemRB.SetText(AbilitiesWindow, AbilitiesTextArea, GemRB.GetTableValue(AbilitiesTable, AbilityIndex, 1) )
	PointsLeft = GemRB.GetVar("Ability0")
	Ability = GemRB.GetVar("Ability" + str(AbilityIndex + 1) )
	if Ability > AbilitiesMinimum:
		Ability = Ability - 1
		GemRB.SetVar("Ability" + str(AbilityIndex + 1), Ability)
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + AbilityIndex)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(Ability) )
		PointsLeft = PointsLeft + 1
		GemRB.SetVar("Ability0", PointsLeft)
		PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
		GemRB.SetText(AbilitiesWindow, PointsLeftLabel, str(PointsLeft) )
		GemRB.SetButtonState(AlignmentWindow, AbilitiesDoneButton, IE_GUI_BUTTON_DISABLED)
	return

def AbilitiesStorePress():
	global AbilitiesWindow, AbilitiesRecallButton
	for i in range(0, 7):
		GemRB.SetVar("Stored" + str(i), GemRB.GetVar("Ability" + str(i)))
	GemRB.SetButtonState(AbilitiesWindow, AbilitiesRecallButton, IE_GUI_BUTTON_ENABLED)
	return

def AbilitiesRecallPress():
	global AbilitiesWindow
	GemRB.InvalidateWindow(AbilitiesWindow)
	for i in range(0, 7):
		GemRB.SetVar("Ability" + str(i), GemRB.GetVar("Stored" + str(i)) )
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002 + i)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(GemRB.GetVar("Ability" + str(i))) )
	return

def AbilitiesRerollPress():
	global AbilitiesWindow, AbilitiesMinimum, AbilitiesMaximum, AbilitiesModifier
	GemRB.InvalidateWindow(AbilitiesWindow)
	GemRB.SetVar("Ability0", 0)
	PointsLeftLabel = GemRB.GetControl(AbilitiesWindow, 0x10000002)
	GemRB.SetText(AbilitiesWindow, PointsLeftLabel, "0")
	Dices = 3
	Sides = 6
	for i in range(0, 6):
		AbilitiesCalcLimits(i)
		Value = GemRB.Roll(Dices, Sides, AbilitiesModifier)
		if Value < AbilitiesMinimum:
			Value = AbilitiesMinimum
		if Value > AbilitiesMaximum:
			Value = AbilitiesMaximum
		GemRB.SetVar("Ability" + str(i + 1), Value)
		AbilityLabel = GemRB.GetControl(AbilitiesWindow, 0x10000003 + i)
		GemRB.SetText(AbilitiesWindow, AbilityLabel, str(Value) )
	return

def AbilitiesDonePress():
	global CharGenWindow, CharGenState, AbilitiesWindow, AbilitiesButton, SkillsButton, SkillsState
	GemRB.UnloadWindow(AbilitiesWindow)
	GemRB.SetButtonState(CharGenWindow, AbilitiesButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_ENABLED)
	CharGenState = 5
	SkillsState = 0
	SetCharacterDescription()
	GemRB.SetVisible(CharGenWindow, 1)
	return

def AbilitiesCancelPress():
	global CharGenWindow, AbilitiesWindow
	GemRB.UnloadWindow(AbilitiesWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Skills Selection

def SkillsPress():
	global CharGenWindow, SkillsWindow, ClassTable, RaceTable, SkillsState
	
	# For now, readability is preferred over speed. This could be optimized later.
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	if SkillsState == 0:
		RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
		if ClassName == "THIEF" or ClassName == "FIGHTER_THIEF" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF" or ClassName == "CLERIC_THIEF":
			SkillsSelect()
		elif ClassName == "RANGER":
			SkillRaceTable = GemRB.LoadTable("SKILLRAC")
			SkillDexterityTable = GemRB.LoadTable("SKILLDEX")
			Dexterity = str(GemRB.GetVar("Ability2") )
			GemRB.SetVar("Skill0", GemRB.GetTableValue(SkillRaceTable, RaceName, "STEALTH") + GemRB.GetTableValue(SkillDexterityTable, Dexterity, "STEALTH") + GemRB.GetTableValue(GemRB.LoadTable("SKILLRNG"), "1", "STEALTH"))
			RacialEnemySelect()
		elif ClassName == "BARD":
			SkillRaceTable = GemRB.LoadTable("SKILLRAC")
			SkillDexterityTable = GemRB.LoadTable("SKILLDEX")
			Dexterity = str(GemRB.GetVar("Ability2") )
			GemRB.SetVar("Skill2", GemRB.GetTableValue(SkillRaceTable, RaceName, "PICK_POCKETS") + GemRB.GetTableValue(SkillDexterityTable, Dexterity, "PICK_POCKETS") + GemRB.GetTableValue(GemRB.LoadTable("SKILLBRD"), "1", "PICK_POCKETS"))
			SkillsState = 1

	if SkillsState == 1:
		ProficienciesSelect()

	if SkillsState == 2:
		if ClassName == "MAGE" or ClassName == "FIGHTER_MAGE" or ClassName == "FIGHTER_MAGE_THIEF" or ClassName == "MAGE_THIEF" or ClassName == "CLERIC_MAGE" or ClassName == "FIGHTER_MAGE_CLERIC":
			MageSpellsSelect()
		else:
			SkillsState = 3

	if SkillsState == 3:
		GemRB.SetButtonState(CharGenWindow, SkillsButton, IE_GUI_BUTTON_DISABLED)
		GemRB.SetButtonState(CharGenWindow, AppearanceButton, IE_GUI_BUTTON_ENABLED)
		CharGenState = 6
		SetCharacterDescription()
	return


def SkillsSelect():
	global CharGenWindow, SkillsWindow, SkillsTextArea, SkillsTable, SkillsDoneButton, RaceTable, SkillsPointsLeft
	GemRB.SetVisible(CharGenWindow, 0)
	SkillsWindow = GemRB.LoadWindow(6)
	RaceName = GemRB.GetTableRowName(RaceTable, GemRB.GetVar("Race") - 1)
	Dexterity = str(GemRB.GetVar("Ability2") )
	SkillsTable = GemRB.LoadTable("SKILLS")
	SkillRaceTable = GemRB.LoadTable("SKILLRAC")
	SkillDexterityTable = GemRB.LoadTable("SKILLDEX")

	SkillsPointsLeft = 30
	SkillsPointsLeftLabel = GemRB.GetControl(SkillsWindow, 0x10000005)
	GemRB.SetLabelUseRGB(SkillsWindow, SkillsPointsLeftLabel, 1)
	GemRB.SetText(SkillsWindow, SkillsPointsLeftLabel, str(SkillsPointsLeft))
	GemRB.SetToken("number", str(SkillsPointsLeft) )

	for i in range (0, 4):
		SkillsLabelButton = GemRB.GetControl(SkillsWindow, 21 + i)
		GemRB.SetButtonState(SkillsWindow, SkillsLabelButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(SkillsWindow, SkillsLabelButton, IE_GUI_BUTTON_ON_PRESS, "SkillsLabelPress")
		GemRB.SetVarAssoc(SkillsWindow, SkillsLabelButton, "SkillIndex", i)

		SkillsPlusButton = GemRB.GetControl(SkillsWindow, 11 + i * 2)
		GemRB.SetButtonState(SkillsWindow, SkillsPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(SkillsWindow, SkillsPlusButton, IE_GUI_BUTTON_ON_PRESS, "SkillsPlusPress")
		GemRB.SetVarAssoc(SkillsWindow, SkillsPlusButton, "SkillIndex", i)

		SkillsMinusButton = GemRB.GetControl(SkillsWindow, 12 + i * 2)
		GemRB.SetButtonState(SkillsWindow, SkillsMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(SkillsWindow, SkillsMinusButton, IE_GUI_BUTTON_ON_PRESS, "SkillsMinusPress")
		GemRB.SetVarAssoc(SkillsWindow, SkillsMinusButton, "SkillIndex", i)

		SkillName = GemRB.GetTableRowName(SkillsTable, i)
		SkillValue = GemRB.GetTableValue(SkillRaceTable, RaceName, SkillName)
		SkillValue = SkillValue + GemRB.GetTableValue(SkillDexterityTable, Dexterity, SkillName)
		GemRB.SetVar("Skill" + str(i), SkillValue)
		GemRB.SetVar("SkillBase" + str(i), SkillValue)
		SkillLabel = GemRB.GetControl(SkillsWindow, 0x10000001 + i)
		GemRB.SetLabelUseRGB(SkillsWindow, SkillLabel, 1)
		GemRB.SetText(SkillsWindow, SkillLabel, str(SkillValue))

	SkillsTextArea = GemRB.GetControl(SkillsWindow, 19)
	GemRB.SetText(SkillsWindow, SkillsTextArea, 17248)

	SkillsDoneButton = GemRB.GetControl(SkillsWindow, 0)
	GemRB.SetButtonState(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_ON_PRESS, "SkillsDonePress")
	GemRB.SetText(SkillsWindow, SkillsDoneButton, 11973)
	GemRB.SetButtonFlags(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	SkillsCancelButton = GemRB.GetControl(SkillsWindow, 25)
	GemRB.SetButtonState(SkillsWindow, SkillsCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(SkillsWindow, SkillsCancelButton, IE_GUI_BUTTON_ON_PRESS, "SkillsCancelPress")
	GemRB.SetText(SkillsWindow, SkillsCancelButton, 13727)

	GemRB.SetVisible(SkillsWindow, 1)
	return

def SkillsLabelPress():
	global SkillsWindow, SkillsTextArea, SkillsTable
	SkillIndex = GemRB.GetVar("SkillIndex")
	GemRB.SetText(SkillsWindow, SkillsTextArea, GemRB.GetTableValue(SkillsTable, SkillIndex, 1) )
	return

def SkillsPlusPress():
	global SkillsWindow, SkillsTextArea, SkillsTable, SkillsPointsLeft
	SkillIndex = GemRB.GetVar("SkillIndex")
	SkillValue = GemRB.GetVar("Skill" + str(SkillIndex))
	GemRB.SetText(SkillsWindow, SkillsTextArea, GemRB.GetTableValue(SkillsTable, SkillIndex, 1) )
	if SkillValue < 99 and SkillsPointsLeft > 0:
		SkillsPointsLeft = SkillsPointsLeft - 1
		SkillsPointsLeftLabel = GemRB.GetControl(SkillsWindow, 0x10000005)
		GemRB.SetText(SkillsWindow, SkillsPointsLeftLabel, str(SkillsPointsLeft))
		SkillValue = SkillValue + 1
		GemRB.SetVar("Skill" + str(SkillIndex), SkillValue)
		SkillLabel = GemRB.GetControl(SkillsWindow, 0x10000001 + SkillIndex)
		GemRB.SetText(SkillsWindow, SkillLabel, str(SkillValue))
		if SkillsPointsLeft == 0:
			GemRB.SetButtonState(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_ENABLED)
	return

def SkillsMinusPress():
	global SkillsWindow, SkillsTextArea, SkillsTable, SkillsPointsLeft
	SkillIndex = GemRB.GetVar("SkillIndex")
	SkillValue = GemRB.GetVar("Skill" + str(SkillIndex))
	GemRB.SetText(SkillsWindow, SkillsTextArea, GemRB.GetTableValue(SkillsTable, SkillIndex, 1) )
	if SkillValue > GemRB.GetVar("SkillBase" + str(SkillIndex)):
		SkillValue = SkillValue - 1
		GemRB.SetVar("Skill" + str(SkillIndex), SkillValue)
		SkillLabel = GemRB.GetControl(SkillsWindow, 0x10000001 + SkillIndex)
		GemRB.SetText(SkillsWindow, SkillLabel, str(SkillValue))
		SkillsPointsLeft = SkillsPointsLeft + 1
		SkillsPointsLeftLabel = GemRB.GetControl(SkillsWindow, 0x10000005)
		GemRB.SetText(SkillsWindow, SkillsPointsLeftLabel, str(SkillsPointsLeft))
		GemRB.SetButtonState(SkillsWindow, SkillsDoneButton, IE_GUI_BUTTON_DISABLED)
	return

def SkillsDonePress():
	global CharGenWindow, SkillsWindow, SkillsState
	GemRB.UnloadWindow(SkillsWindow)
	SkillsState = 1
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def SkillsCancelPress():
	global CharGenWindow, SkillsWindow
	GemRB.UnloadWindow(SkillsWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Racial Enemy Selection

def RacialEnemySelect():
	return


# Weapon Proficiencies Selection

def ProficienciesSelect():
	global CharGenWindow, ProficienciesWindow, ProficienciesTable, ProficienciesTextArea, ProficienciesPointsLeft, ProficienciesDoneButton, ClassTable, ProfsMaxTable
	GemRB.SetVisible(CharGenWindow, 0)
	ProficienciesWindow = GemRB.LoadWindow(9)
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	ProficienciesTable = GemRB.LoadTable("PROFCNCS")
	ProfsTable = GemRB.LoadTable("PROFS")
	ProfsMaxTable = GemRB.LoadTable("PROFSMAX")
	ClassWeaponsTable = GemRB.LoadTable("CLASWEAP")

	Class = GemRB.GetTableRowIndex(ProfsTable, ClassName)
	ProficienciesPointsLeft = GemRB.GetTableValue(ProfsTable, Class, 0)
	PointsLeftLabel = GemRB.GetControl(ProficienciesWindow, 0x10000009)
	GemRB.SetLabelUseRGB(ProficienciesWindow, PointsLeftLabel, 1)
	GemRB.SetText(ProficienciesWindow, PointsLeftLabel, str(ProficienciesPointsLeft))
	GemRB.SetToken("number", str(ProficienciesPointsLeft) )

	for i in range (0,8):
		ProficienciesLabel = GemRB.GetControl(ProficienciesWindow, 69 + i)
		GemRB.SetButtonState(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ON_PRESS, "ProficienciesLabelPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesLabel, "ProficienciesIndex", i + 1)

		for j in range (0, 5):
			ProficienciesMark = GemRB.GetControl(ProficienciesWindow, 27 + i * 5 + j)
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_OR)

		Allowed = GemRB.GetTableValue(ClassWeaponsTable, ClassName, GemRB.GetTableRowName(ProficienciesTable, i))

		ProficienciesPlusButton = GemRB.GetControl(ProficienciesWindow, 11 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesPlusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesPlusButton, "ProficienciesIndex", i + 1)

		ProficienciesMinusButton = GemRB.GetControl(ProficienciesWindow, 12 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesMinusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesMinusButton, "ProficienciesIndex", i + 1)

	for i in range (0,7):
		ProficienciesLabel = GemRB.GetControl(ProficienciesWindow, 85 + i)
		GemRB.SetButtonState(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesLabel, IE_GUI_BUTTON_ON_PRESS, "ProficienciesLabelPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesLabel, "ProficienciesIndex", i + 9)

		for j in range (0, 5):
			ProficienciesMark = GemRB.GetControl(ProficienciesWindow, 92 + i * 5 + j)
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_OR)

		Allowed = GemRB.GetTableValue(ClassWeaponsTable, ClassName, GemRB.GetTableRowName(ProficienciesTable, i + 8))
		
		ProficienciesPlusButton = GemRB.GetControl(ProficienciesWindow, 127 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesPlusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesPlusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesPlusButton, "ProficienciesIndex", i + 9)

		ProficienciesMinusButton = GemRB.GetControl(ProficienciesWindow, 128 + i * 2)
		if Allowed == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_DISABLED)
			GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		else:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ENABLED)
		GemRB.SetEvent(ProficienciesWindow, ProficienciesMinusButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesMinusPress")
		GemRB.SetVarAssoc(ProficienciesWindow, ProficienciesMinusButton, "ProficienciesIndex", i + 9)

	for i in range(1, 16):
		GemRB.SetVar("Proficiency" + str(i), 0)

	ProficienciesTextArea = GemRB.GetControl(ProficienciesWindow, 68)
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, 9588)

	ProficienciesDoneButton = GemRB.GetControl(ProficienciesWindow, 0)
	GemRB.SetButtonState(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesDonePress")
	GemRB.SetText(ProficienciesWindow, ProficienciesDoneButton, 11973)
	GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	ProficienciesCancelButton = GemRB.GetControl(ProficienciesWindow, 77)
	GemRB.SetButtonState(ProficienciesWindow, ProficienciesCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ProficienciesWindow, ProficienciesCancelButton, IE_GUI_BUTTON_ON_PRESS, "ProficienciesCancelPress")
	GemRB.SetText(ProficienciesWindow, ProficienciesCancelButton, 13727)

	GemRB.SetVisible(ProficienciesWindow, 1)
	return

def ProficienciesLabelPress():
	global ProficienciesWindow, ProficienciesTable, ProficienciesTextArea
	ProficienciesIndex = GemRB.GetVar("ProficienciesIndex") - 1
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, GemRB.GetTableValue(ProficienciesTable, ProficienciesIndex, 1) )
	return

def ProficienciesPlusPress():
	global ProficienciesWindow, ProficienciesTable, ProficienciesTextArea, ProficienciesPointsLeft, ProfsMaxTable
	
	ProficienciesIndex = GemRB.GetVar("ProficienciesIndex") - 1
	ProficienciesValue = GemRB.GetVar("Proficiency" + str(ProficienciesIndex) )
	ClassName = GemRB.GetTableRowName(ClassTable, GemRB.GetVar("Class") - 1)
	Class = GemRB.GetTableRowIndex(ProfsMaxTable, ClassName)
	if ProficienciesPointsLeft > 0 and ProficienciesValue < GemRB.GetTableValue(ProfsMaxTable, Class, 0):
		ProficienciesPointsLeft = ProficienciesPointsLeft - 1
		PointsLeftLabel = GemRB.GetControl(ProficienciesWindow, 0x10000009)
		GemRB.SetText(ProficienciesWindow, PointsLeftLabel, str(ProficienciesPointsLeft))
		if ProficienciesPointsLeft == 0:
			GemRB.SetButtonState(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_ENABLED)
		
		ProficienciesValue = ProficienciesValue + 1
		GemRB.SetVar("Proficiency" + str(ProficienciesIndex), ProficienciesValue)
		if ProficienciesIndex < 8:
			ControlID = 26 + ProficienciesIndex * 5 + ProficienciesValue
		else:
			ControlID = 51 + ProficienciesIndex * 5 + ProficienciesValue
		ProficienciesMark = GemRB.GetControl(ProficienciesWindow, ControlID)
		# TODO: get this right
		GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_NAND)
		
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, GemRB.GetTableValue(ProficienciesTable, ProficienciesIndex, 1) )
	return

def ProficienciesMinusPress():
	global ProficienciesWindow, ProficienciesTable, ProficienciesTextArea, ProficienciesPointsLeft
	
	ProficienciesIndex = GemRB.GetVar("ProficienciesIndex") - 1
	ProficienciesValue = GemRB.GetVar("Proficiency" + str(ProficienciesIndex) )
	if ProficienciesValue > 0:
		ProficienciesValue = ProficienciesValue - 1
		GemRB.SetVar("Proficiency" + str(ProficienciesIndex), ProficienciesValue)
		if ProficienciesIndex < 8:
			ControlID = 27 + ProficienciesIndex * 5 + ProficienciesValue
		else:
			ControlID = 52 + ProficienciesIndex * 5 + ProficienciesValue
		ProficienciesMark = GemRB.GetControl(ProficienciesWindow, ControlID)
		GemRB.SetButtonFlags(ProficienciesWindow, ProficienciesMark, IE_GUI_BUTTON_NO_IMAGE, OP_OR)
		
		ProficienciesPointsLeft = ProficienciesPointsLeft + 1
		PointsLeftLabel = GemRB.GetControl(ProficienciesWindow, 0x10000009)
		GemRB.SetText(ProficienciesWindow, PointsLeftLabel, str(ProficienciesPointsLeft))
		GemRB.SetButtonState(ProficienciesWindow, ProficienciesDoneButton, IE_GUI_BUTTON_DISABLED)
		
	GemRB.SetText(ProficienciesWindow, ProficienciesTextArea, GemRB.GetTableValue(ProficienciesTable, ProficienciesIndex, 1) )
	return

def ProficienciesDonePress():
	global CharGenWindow, ProficienciesWindow, SkillsState
	GemRB.SetVisible(ProficienciesWindow, 0)
	GemRB.UnloadWindow(ProficienciesWindow)
	SkillsState = 2
	GemRB.SetVisible(CharGenWindow, 1)
	SkillsPress()
	return

def ProficienciesCancelPress():
	global CharGenWindow, ProficienciesWindow, SkillsState
	GemRB.UnloadWindow(ProficienciesWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Spells Selection

def MageSpellsSelect():
	global CharGenWindow, MageSpellsWindow
	GemRB.SetVisible(CharGenWindow, 0)
	MageSpellsWindow = GemRB.LoadWindow(7)

	MageSpellsTextArea = GemRB.GetControl(MageSpellsWindow, 27)
	GemRB.SetText(MageSpellsWindow, MageSpellsTextArea, 17250)

	MageSpellsDoneButton = GemRB.GetControl(MageSpellsWindow, 0)
	GemRB.SetButtonState(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_ON_PRESS, "MageSpellsDonePress")
	GemRB.SetText(MageSpellsWindow, MageSpellsDoneButton, 11973)
	GemRB.SetButtonFlags(MageSpellsWindow, MageSpellsDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	MageSpellsCancelButton = GemRB.GetControl(MageSpellsWindow, 29)
	GemRB.SetButtonState(MageSpellsWindow, MageSpellsCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(MageSpellsWindow, MageSpellsCancelButton, IE_GUI_BUTTON_ON_PRESS, "MageSpellsCancelPress")
	GemRB.SetText(MageSpellsWindow, MageSpellsCancelButton, 13727)

	GemRB.SetVisible(MageSpellsWindow, 1)
	return

def MageSpellsDonePress():
	return

def MageSpellsCancelPress():
	global CharGenWindow, MageSpellsWindow, SkillsState
	GemRB.UnloadWindow(MageSpellsWindow)
	SkillsState = 0
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Appearance Selection

def AppearancePress():
	global CharGenWindow, AppearanceWindow, AppearanceTable, AppearanceDoneButton, PortraitTable, Portrait
	GemRB.SetVisible(CharGenWindow, 0)
	AppearanceWindow = GemRB.LoadWindow(13)
	PortraitName = GemRB.GetTableRowName(PortraitTable, Portrait) + "L"
	AppearanceTable = GemRB.LoadTable("PORTCOLR")

	AppearanceDoneButton = GemRB.GetControl(AppearanceWindow, 0)
	GemRB.SetButtonState(AppearanceWindow, AppearanceDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceDoneButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceDonePress")
	GemRB.SetText(AppearanceWindow, AppearanceDoneButton, 11973)
	GemRB.SetButtonFlags(AppearanceWindow, AppearanceDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	AppearanceCancelButton = GemRB.GetControl(AppearanceWindow, 13)
	GemRB.SetButtonState(AppearanceWindow, AppearanceCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(AppearanceWindow, AppearanceCancelButton, IE_GUI_BUTTON_ON_PRESS, "AppearanceCancelPress")
	GemRB.SetText(AppearanceWindow, AppearanceCancelButton, 13727)

	GemRB.SetVisible(AppearanceWindow, 1)
	return

def AppearanceDonePress():
	return

def AppearanceCancelPress():
	global CharGenWindow, AppearanceWindow
	GemRB.UnloadWindow(AppearanceWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Biography Selection

def BiographyPress():
	global CharGenWindow, BiographyWindow, BiographyDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	BiographyWindow = GemRB.LoadWindow(51)

	BiographyDoneButton = GemRB.GetControl(BiographyWindow, 5)
	GemRB.SetButtonState(BiographyWindow, BiographyDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(BiographyWindow, BiographyDoneButton, IE_GUI_BUTTON_ON_PRESS, "BiographyDonePress")
	GemRB.SetText(BiographyWindow, BiographyDoneButton, 11973)
	GemRB.SetButtonFlags(BiographyWindow, BiographyDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	BiographyCancelButton = GemRB.GetControl(BiographyWindow, 1)
	GemRB.SetButtonState(BiographyWindow, BiographyCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(BiographyWindow, BiographyCancelButton, IE_GUI_BUTTON_ON_PRESS, "BiographyCancelPress")
	GemRB.SetText(BiographyWindow, BiographyCancelButton, 13727)

	GemRB.SetVisible(BiographyWindow, 1)
	return

def BiographyDonePress():
	return

def BiographyCancelPress():
	global CharGenWindow, BiographyWindow
	GemRB.UnloadWindow(BiographyWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Name Selection

def NamePress():
	global CharGenWindow, NameWindow, NameDoneButton
	GemRB.SetVisible(CharGenWindow, 0)
	NameWindow = GemRB.LoadWindow(5)

	NameDoneButton = GemRB.GetControl(NameWindow, 0)
	GemRB.SetButtonState(NameWindow, NameDoneButton, IE_GUI_BUTTON_DISABLED)
	GemRB.SetEvent(NameWindow, NameDoneButton, IE_GUI_BUTTON_ON_PRESS, "NameDonePress")
	GemRB.SetText(NameWindow, NameDoneButton, 11973)
	GemRB.SetButtonFlags(NameWindow, NameDoneButton, IE_GUI_BUTTON_DEFAULT, OP_OR)

	NameCancelButton = GemRB.GetControl(NameWindow, 3)
	GemRB.SetButtonState(NameWindow, NameCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(NameWindow, NameCancelButton, IE_GUI_BUTTON_ON_PRESS, "NameCancelPress")
	GemRB.SetText(NameWindow, NameCancelButton, 13727)

	GemRB.SetVisible(NameWindow, 1)
	return

def NameDonePress():
	return

def NameCancelPress():
	global CharGenWindow, NameWindow
	GemRB.UnloadWindow(NameWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


# Import Character

def ImportPress():
	global CharGenWindow, ImportWindow
	GemRB.SetVisible(CharGenWindow, 0)
	ImportWindow = GemRB.LoadWindow(20)

	ImportCancelButton = GemRB.GetControl(ImportWindow, 1)
	GemRB.SetButtonState(ImportWindow, ImportCancelButton, IE_GUI_BUTTON_ENABLED)
	GemRB.SetEvent(ImportWindow, ImportCancelButton, IE_GUI_BUTTON_ON_PRESS, "ImportCancelPress")
	GemRB.SetText(ImportWindow, ImportCancelButton, 13727)

	GemRB.SetVisible(ImportWindow, 1)
	return

def ImportCancelPress():
	global CharGenWindow, ImportWindow
	GemRB.UnloadWindow(ImportWindow)
	GemRB.SetVisible(CharGenWindow, 1)
	return


def CancelPress():
	global CharGenWindow
	GemRB.UnloadWindow(CharGenWindow)
	GemRB.SetNextScript("PartyFormation")
	return

def AcceptPress():
	return

