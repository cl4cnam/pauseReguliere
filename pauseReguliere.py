from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk

# programmer les temps
#---------------------
nbreSecondePeriodeTravail = 15*60
nbreSecondePause = 60
nbreSecondeDelaiAvertissement = 20
nbreSecondeDelaiAvertissement_default = 5*60

#====== pour test ====================
# ~ nbreSecondePeriodeTravail = 7 # affiche 0 secondes
# ~ nbreSecondePause = 5
# ~ nbreSecondeDelaiAvertissement = 4
# ~ nbreSecondeDelaiAvertissement_default = 10
#--------------------------------------------------

# textes
#--------
text_lancementPause = 'Démmarer la pause dans %s secondes' % nbreSecondeDelaiAvertissement
text_lancementpauseAutomatique = 'Pause automatique dans %s secondes' % nbreSecondeDelaiAvertissement_default

#graphisme
#--------------
couleur_text = 'black'
couleur_textBouton = 'white'
couleur_boutons = '#3283D3'
fond_fenetre_pause ='#ffff89'
fond_fenetre_pauseFini ='#92ff92'
fond_fenetre_alerte ='#ffccaa'

#images
img_sport = 'sport.jpg'
img_travail = 'travail.png'


# Fenêtre de mise en pause
#-------------------------
def petiteFenetre():
	root.geometry('400x300+20+20')
	texte['wraplength'] = 300

# Fenêtre de pause
#-------------------------
def grandeFenetre():
	root.geometry('1560x830+20+20')
	texte['wraplength'] = 0

# Basculer vers l'avertissement personnalisé
#-------------------------------------------
def switchToAvertissement():
	root.state('normal')
	root['bg']=fond_fenetre_alerte
	petiteFenetre()
	texte['text'] = text_lancementpauseAutomatique
	bouton['state'] = 'normal'
	bouton['text']=text_lancementPause
	bouton['bg'] = couleur_boutons
	bouton['command'] = switchToPrePause
	global delaiAnnulable
	delaiAnnulable = root.after(1000 * nbreSecondeDelaiAvertissement_default, switchToPause)

# lancer la pause
#-------------------
def switchToPrePause():
	global delaiAnnulable
	root['bg']=fond_fenetre_pause
	root.after_cancel(delaiAnnulable)
	root.state('withdrawn')
	root.after(1000 * nbreSecondeDelaiAvertissement, switchToPause)

def switchToPause():
	root.state('normal')
	grandeFenetre()
	texte['text'] = 'Maintenant : pause de %s secondes !' % nbreSecondePause
	# ~ img = Image.open(img_sport) 
	# ~ img_tk = ImageTk.PhotoImage(img)
	# ~ label = Label(root, image=img_tk) 
	# ~ label.pack()
	bouton.pack_forget()
	root.after(1000 * nbreSecondePause, switchToPreRepriseTravail)

def switchToPreRepriseTravail():
	root['bg']=fond_fenetre_pauseFini
	texte['text'] = 'C\'est parti pour une période de %s minutes !' % (nbreSecondePeriodeTravail // 60)
	bouton.pack()
	bouton['state'] = 'normal'
	bouton['text']='OK'
	bouton['bg'] = couleur_boutons
	bouton['command'] = switchToTravail

def switchToTravail():
	root.state('withdrawn')
	root.after(1000 * nbreSecondePeriodeTravail, switchToAvertissement)

# main
#==========
# Géré par TK
#--------------

# fabrication de la fenêtre
root = Tk() 
root.overrideredirect(1)
root.attributes("-topmost", True) # mise en avant plan de tous les programmes qui tournent


# fabrication d'un texte
texte = Label()
texte['font'] = ("Arial", 16, "bold")
texte['fg'] = couleur_text
# ~ texte['padx'] = 20 #padding
# ~ texte['pady'] = 20 #padding
# ~ texte['ipadx']= 50
# ~ texte['ipady']= 50

texte.pack(padx=40, pady=40, ipadx=20, ipady=20) # pour afficher sur la fenêtre

# fabrique un bouton
bouton = Button(text='')
bouton['padx'] = 20
bouton['pady'] = 20
bouton.pack()  # pour afficher sur la fenêtre

# lance le programme de pause
switchToTravail()

# root.mainloop()
while True:
	root.update_idletasks()
	root.update()
