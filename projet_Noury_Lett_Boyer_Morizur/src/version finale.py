from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count
import numpy as np

####################### Récupération des données sous forme de dictionnaires depuis le fichier trajectory.json ########################
import json
import numpy as np
with open("projet_Noury_Lett_Boyer_Morizur/src/trajectory.json", "r") as f:
    data = json.load(f)

############################ Initialisation et récupération des différents variables pour les graphiques ################################
t=0.5
coord_x= []
#data[1]["pose"]['position']['y']
coord_y=[]
vitesse_l=[]
vitesse_a=[]


for i in range(800):
    coord_x.append(data[i]["pose"]['position']['x'])
    coord_y.append(data[i]["pose"]['position']['y'])

for i in range(799):
    vitesse_l.append((((coord_x[i+1]-coord_x[i])/t) +((coord_y[i+1]-coord_y[i])/t))/2)
    if (coord_x[i+1]-coord_x[i])==0:
        vitesse_a.append(0)
    else:
        vitesse_a.append(np.arctan(((coord_y[i+1]-coord_y[i])/(coord_x[i+1]-coord_x[i])))/t)
vitesse_a.append(0)
vitesse_l.append(0)




##################################################### Choix des couleurs #########################################################################

couleur_bg="#fad8c2"                                                                            # couleur fond clair
couleur_foncé="#ff9c5c"                                                                         # couleur fond foncé

############################################# Création de la fenêtre principale #################################################################

fenetre_principale = Tk()
fenetredeplacement= Tk()
fenetre_principale.title("Turtlebot")                                                           # nom fenêtre
fenetre_principale.geometry("1000x700")                                                         # dimension fenetre
fenetre_principale.config(background=couleur_bg)                                                # couleur fond

################################################ Création de frames (zones) ######################################################################

frame_title= Frame(fenetre_principale,bg=couleur_bg)                                                                        # creation zone du titre

frame_commande= LabelFrame(fenetre_principale,text="Commande",bg=couleur_foncé,height=470,width=200)                        # creation zone de commande

frame_mouvement= LabelFrame(fenetre_principale,text="Mouvement du robot",bg=couleur_foncé,height=470,width=750)             # cration zone de mouvement

frame_connexion= LabelFrame(fenetre_principale,text="Connexion avec le robot",bg=couleur_foncé,height=150,width=300)        # creation zone de connexion

############################################### Ajout dans la zone titre ########################################################################

Label_title =Label (frame_title, text= "Bienvenue sur l'application turtlebot", font=("Courrier", 20),bg=couleur_bg,fg="black")
Label_title.pack()                                                                              # ajout du titre
Label_subtitle =Label (frame_title, text= "Nolwenn MORIZUR  |  Bastien LETT  |  Amelia NOURY  |  Paul BOYER", font=("Courrier", 9),bg=couleur_bg,fg="black")
Label_subtitle.pack()                                                                           # ajout du sous titre

################################# Création d'une nouvelle fenetre pour voir une simulation d'un déplacement à l'aide des buttons ###################
canvas = Canvas(fenetredeplacement, width=250, height=250, bg="ivory")
# coordonnées initiales
coords = (125, 125)
# création du rectangle
rectangle = canvas.create_rectangle(0,0,25,25,fill="violet")

############################################## Ajout dans la zone commande ##############################################################

vitesse_lineaire = DoubleVar()                                                                  # création d'un slider de vitesse lineaire
scale_v_lineaire = Scale(frame_commande,variable=vitesse_lineaire,label="Vitesse linéaire",bg=couleur_bg)
scale_v_lineaire.place(x=30, y=165)

vitesse_angulaire = DoubleVar()                                                                 # creation d'un slider de vitesse angulaire
scale_v_angulaire = Scale(frame_commande,variable=vitesse_angulaire, label="Vitesse angulaire",bg=couleur_bg)
scale_v_angulaire.place(x=25, y=285)

forward_button=Button(frame_commande,text="Forward", font=("Courrier", 10),bg=couleur_bg,fg="black")
forward_button.place(x=70, y=45)                                                                # création d'un boutton pour avancer

backward_button=Button(frame_commande,text="Backward", font=("Courrier", 10),bg=couleur_bg,fg="black")
backward_button.place(x=65, y=125)                                                              # création d'un bouton pour reculer

left_button=Button(frame_commande,text="Left", font=("Courrier", 10),bg=couleur_bg,fg="black")
left_button.place(x=35, y=80)                                                                   # création d'un bouton pour aller a gauche

right_button=Button(frame_commande,text="Right", font=("Courrier", 10),bg=couleur_bg,fg="black")
right_button.place(x=120, y=80)                                                                 # création d'un bouton pour aller a droite

############################################# Ajout dans la zone mouvement ##############################################################

#liste_vitesse_lineaire=[10,15,20,15,10,5,10,15,20,15]                                           # aquisition de la liste vitesse lineaire
#liste_vitesse_angulaire=[3,4,5,6,4,5,3,2,1,0]                                                   # aquisition de la liste de vitesse angulaire
#liste_position_x=[1,2,3,4,5,9,4,3,1,8]                                                          # aquisition de la liste position x
#liste_position_y=[9,6,3,2,5,8,7,4,1,7]                                                          # aquisition de la liste position y
#liste_temps=[1,2,3,4,5,6,7,8,9,10]                                                              # aquisition de la liste temps

liste_vitesse_lineaire=vitesse_l                                                                # aquisition de la liste vitesse lineaire
liste_vitesse_angulaire=vitesse_a                                                               # aquisition de la liste de vitesse angulaire
liste_position_x= coord_x                                                                       # aquisition de la liste position x
liste_position_y= coord_y     
liste_temps=[]     
for i in range(800):                                                                            # aquisition de la liste position y
  liste_temps.append(0.5*i)                                                                     # aquisition de la liste temps



# Création et animation du graphe de vitesse linéaire

x_lineaire=[]                                                                                   # creation de listes temporaires qui font l'animation
y_lineaire=[]
x_angulaire=[]                                                                                  # creation de listes temporaires qui font l'animation
y_angulaire=[]
x_position=[]
y_position=[]

graphe_vitesse_lineaire, ax_lineaire = plt.subplots(figsize=(3, 2), dpi=100)                    # Création de la figure et des axes

graphe_vitesse_angulaire, ax_angulaire = plt.subplots(figsize=(3, 2), dpi=100)                  # Création de la figure et des axes

graphe_position, ax_position = plt.subplots(figsize=(5, 6), dpi=70)


canvas_v_lineaire= FigureCanvasTkAgg(graphe_vitesse_lineaire, master=frame_mouvement)           # Intégration du graphe dans la zone mouvement
canvas_v_lineaire.draw()
canvas_v_lineaire.get_tk_widget().place(x=20, y=10)

canvas_v_angulaire= FigureCanvasTkAgg(graphe_vitesse_angulaire, master=frame_mouvement)         # Intégration du graphe dans la zone mouvement
canvas_v_angulaire.draw()
canvas_v_angulaire.get_tk_widget().place(x=20, y=230)
                                                                            
canvas_position = FigureCanvasTkAgg(graphe_position, master=frame_mouvement)                    # Intégration du graphe dans la zone mouvement
canvas_position.draw()
canvas_position.get_tk_widget().place(x=365, y=10)

counter=count(0,1)                                                                              # compteur pour l'animation

def update(i):                                                                                  # Fonction d'animation
    idx=next(counter)

    x_lineaire.append(liste_temps[i])
    y_lineaire.append(liste_vitesse_lineaire[i])
    plt.cla()
    ax_lineaire.plot(x_lineaire,y_lineaire, color ='b')
    ax_lineaire.set_xlabel('Temps (en s)')
    ax_lineaire.set_ylabel('Vitesse linéaire du robot (en rad/s)')

    x_angulaire.append(liste_temps[i])
    y_angulaire.append(liste_vitesse_angulaire[i])
    plt.cla()
    ax_angulaire.plot(x_angulaire,y_angulaire , color ='r')
    ax_angulaire.set_xlabel('Temps (en s)')
    ax_angulaire.set_ylabel('Vitesse angulaire du robot (en rad/s)')

    x_position.append(liste_position_x[i])
    y_position.append(liste_position_y[i])
    plt.cla()
    ax_position.plot(x_position,y_position , color ='g')
    ax_position.set_xlabel('Temps (en s)')
    ax_position.set_ylabel('Vitesse angulaire du robot (en rad/s)')

    canvas_v_lineaire.draw()
    canvas_v_angulaire.draw()
    canvas_position.draw()

# animation.func avec 3 graph en même temps
ani = animation.FuncAnimation(graphe_vitesse_lineaire, update, frames=10, interval=100, repeat=False) # Animation du graphique

#legend vitesse linéaire

Label_abscisse_lineaire =Label (frame_mouvement, text= "Temps (en s)", font=("Courrier", 7),bg=couleur_foncé,fg="black")
Label_abscisse_lineaire.place(x=130, y=210)                                                     # legend graphe abscisse

Label_ordonee_lineaire =Label (frame_mouvement, text= "Vitesse linéaire du robot (en rad/s)", font=("Courrier", 8),bg="white",fg="black")
Label_ordonee_lineaire.place(x=80, y=10)                                                        # titre graphe vitesse lineaire

#legend vitesse angulaire

Label_abscisse_angulaire =Label (frame_mouvement, text= "Temps (en s)", font=("Courrier", 7),bg=couleur_foncé,fg="black")
Label_abscisse_angulaire.place(x=130, y=430)                                                    # legend graphe abscisse

Label_ordonee_angulaire =Label (frame_mouvement, text= "Vitesse angulaire du robot (en rad/s)", font=("Courrier", 8),bg="white",fg="black")
Label_ordonee_angulaire.place(x=80, y=230)                                                      # titre graphe vitesse angulaire

#legend position

Label_ordonee_position =Label (frame_mouvement, text= "Position du robot", font=("Courrier", 10),bg="white",fg="black")
Label_ordonee_position.place(x=490, y=20)                                                       # titre graphe posistion


########################################### Ajout dans la zone connexion ###################################"###########################

titre_ROS_master_URI = Label(frame_connexion, text="ROS master URI",bg=couleur_foncé)           # ajout de la zone por entrer le ROS master URI
titre_ROS_master_URI.place(x=5, y=10)
ROS_master_URI = Entry(frame_connexion, bd =5)
ROS_master_URI.place(x=95, y=10)

titre_ROS_hostname = Label(frame_connexion, text="ROS_hostname",bg=couleur_foncé)               # ajout de la zone por entrer le ROS hostname
titre_ROS_hostname.place(x=5, y=45)
ROS_hostname = Entry(frame_connexion, bd =5)
ROS_hostname.place(x=95, y=45)

start_button=Button(frame_connexion,text="Start", font=("Courrier", 10),bg=couleur_bg,fg="black")# ajout du bouton start
start_button.place(x=80, y=80)

stop_button=Button(frame_connexion,text="Stop", font=("Courrier", 10),bg=couleur_bg,fg="black") # ajout du bouton stop
stop_button.place(x=130, y=80)

canvas = Canvas(frame_connexion, width=30, height=30, background=couleur_foncé ,borderwidth=0 ) # ajout du voyent de connexion
diam=28
A=(a,b)=(2, 2)
B=(a+diam, b+diam)
canvas.create_oval(A, B, fill='green',outline='green')
canvas.place(x=180, y=80)

############################################ Ajout sur la fenêtre principale ############################################################

frame_title.pack()                                                                              # ajout de la zone titre sur la fenêtre principale
frame_commande.place(x=10, y=225)                                                               # ajout de la zone commande sur la fenêtre principale
frame_mouvement.place(x=225, y=225)                                                             # ajout de la zone mouvement sur la fenêtre principale
frame_connexion.place(x=350, y=70)                                                              # ajout de la zone connexion sur la fenêtre principale

########################################## Affichage de la fenêtre principale #############################################################

fenetre_principale.mainloop()
