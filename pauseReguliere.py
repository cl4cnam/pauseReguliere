from tkinter import *
from tkinter.font import Font

nbreSecondePeriodeTravail = 15*60
nbreSecondePause = 60
nbreSecondeDelaiAvertissement = 20
nbreSecondeDelaiAvertissementSansOK = 5*60
# ~ nbreSecondePeriodeTravail = 7
# ~ nbreSecondePause = 5
# ~ nbreSecondeDelaiAvertissement = 4
# ~ nbreSecondeDelaiAvertissementSansOK = 10

def petiteFenetre():
	root.geometry('400x300+20+20')
	lab['wraplength'] = 300

def grandeFenetre():
	root.geometry('1560x830+20+20')
	lab['wraplength'] = 0

def switchToAvertissement():
	root.state('normal')
	petiteFenetre()
	lab['text'] = 'Pause dans %s secondes !' % nbreSecondeDelaiAvertissement
	bouton['state'] = 'normal'
	bouton['bg'] = '#C0C0FF'
	bouton['command'] = switchToPrePause
	global delaiAnnulable
	delaiAnnulable = root.after(1000 * nbreSecondeDelaiAvertissementSansOK, switchToPause)

def switchToPrePause():
	global delaiAnnulable
	root.after_cancel(delaiAnnulable)
	root.state('withdrawn')
	root.after(1000 * nbreSecondeDelaiAvertissement, switchToPause)

def switchToPause():
	root.state('normal')
	grandeFenetre()
	lab['text'] = 'Maintenant : pause de %s secondes !' % nbreSecondePause
	bouton.pack_forget()
	root.after(1000 * nbreSecondePause, switchToPreRepriseTravail)

def switchToPreRepriseTravail():
	lab['text'] = 'C\'est parti pour une période de %s minutes !' % (nbreSecondePeriodeTravail // 60)
	bouton.pack()
	bouton['state'] = 'normal'
	bouton['bg'] = '#C0FFC0'
	bouton['command'] = switchToTravail

def switchToTravail():
	root.state('withdrawn')
	root.after(1000 * nbreSecondePeriodeTravail, switchToAvertissement)

root = Tk()
root.overrideredirect(1)
root.attributes("-topmost", True)

lab = Label()
lab['font'] = ("Arial", 16, "bold")
lab['fg'] = '#804000'
lab['padx'] = 100
lab['pady'] = 100
lab.pack()

bouton = Button(text='OK')
bouton['padx'] = 20
bouton['pady'] = 20
bouton.pack()

switchToTravail()

# root.mainloop()
while True:
	root.update_idletasks()
	root.update()
