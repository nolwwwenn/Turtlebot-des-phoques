from tkinter import * 

from tkinter.messagebox import *

fenetre = Tk()
fenetre2= Tk()
#fenetre3=Tk()






#label = Label(fenetre, text="Hello World")
#label.pack()

# bouton de sortie
#bouton=Button(fenetre, text="Fermer", command=fenetre.quit)


#confirmation de fermeture fenêtre
def callback():
    if askyesno('Titre 1', 'Voulez vous quittez?'):
        fenetre.destroy()
    else:
        showinfo('Titre 3', 'La navigation continue!')
#width=fenetre.size
#
#Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)

"""value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable="string", width=30)
entree.pack()"""
canvas = Canvas(fenetre2, width=250, height=250, bg="ivory")
# coordonnées initiales
coords = (125, 125)
# création du rectangle
rectangle = canvas.create_rectangle(0,0,25,25,fill="violet")
#canvas = Canvas(deplacement, width=150, height=120, background='yellow')


#zone de texte
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable="string", width=30)
entree.pack(side=TOP, padx=5, pady=50)

vlin = DoubleVar()
vang = DoubleVar()
scale1 = Scale(fenetre,variable=vlin)
scale2 = Scale(fenetre,variable=vang)
monAffichage1 = Label(fenetre, text = "Vitesse linéaire", width=10)
monAffichage1.pack(side=RIGHT, padx=5, pady=5)
scale1.pack(side=RIGHT, padx=5, pady=20)

monAffichage2 = Label(fenetre, text = "Vitesse angulaire", width=12)
monAffichage2.pack(side=RIGHT, padx=5, pady=5)
scale2.pack(side=RIGHT, padx=5, pady=20)

#Création d'un lien entre le clavier et les déplacements d'un carré
def clavier(event):
    global coords

    touche = event.keysym

    if touche == "Up":
        coords = (coords[0], coords[1] - 10)
    elif touche == "Down":
        coords = (coords[0], coords[1] + 10)
    elif touche == "Right":
        coords = (coords[0] + 10, coords[1])
    elif touche == "Left":
        coords = (coords[0] -10, coords[1])
    # changement de coordonnées pour le rectangle
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)

#Création d'un lien entre le déplacement d'un carré et les touches de déplacement
def change1():
    global coords

    if forward.cget('relief') == RAISED:
        coords = (coords[0], coords[1] - 10)
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)
def change2():
    global coords
    if backward.cget('relief')== RAISED:
        coords = (coords[0], coords[1] + 10)
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)
def change3():
    global coords
    if right.cget('relief') == RAISED:
        coords = (coords[0] + 10, coords[1])
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)
def change4():
    global coords
    if left.cget('relief') == RAISED:
        coords = (coords[0] -10, coords[1])
    canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)

#Création des différents boutons de notre interface
start=Button(fenetre, text ='START', fg='green',).pack(side=LEFT, padx=5, pady=20)
fermer=Button(fenetre, text ='Fermer',command=callback).pack(side=RIGHT, padx=5, pady=20)
stop=Button(fenetre, text ='STOP',fg='red')
stop.pack(side=LEFT, padx=5, pady=20)
forward=Button(fenetre, text ='Forward',relief=RAISED,command=change1)
forward.pack(side=TOP, padx=5, pady=20)
left=Button(fenetre,text='Left',relief=RAISED,command=change4)
left.pack(side=LEFT,padx=10,pady=10)
backward=Button(fenetre,text='Backward',relief=RAISED,command=change2)
backward.pack(side=LEFT,padx=10,pady=10)
right=Button(fenetre, text="Right",relief=RAISED,command=change3)
right.pack(side=LEFT, padx=5, pady=20)

#Création de slider





# création du canvas

canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()

fenetre.mainloop()

