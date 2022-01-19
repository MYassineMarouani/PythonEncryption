# NB : tout ce code est faite ligne par ligne par Mohamed Yassine Marouani
# objet du programme : cryptage de hill
from tkinter import *
from math import *
import numpy as np
import numpy.linalg as alg
from sympy import mod_inverse
# fonction cryptage
def cryptage():
    MSG = zt1.get()
    a = zt2.get()
    b = zt3.get()
    c = zt4.get()
    d = zt5.get()
    final=""
    i=0
    j=2
    while j<(len(MSG)+1):
        B1=MSG[i:j]
        PB1=ord(B1[0])-64
        PB2=ord(B1[1])-64
        C1=(((int(a)*PB1)+(int(b)*PB2))%26)
        C2=(((int(c)*PB1)+(int(d)*PB2))%26)
        B1cryp=chr(C1+64)+chr(C2+64)
        final=final+B1cryp
        i=i+2
        j=j+2
        e=int(d)
        f=-int(b) 
        g=-int(c)
        h=int(a)
        CHINV=(int(a)*int(d))-(int(b)*int(c))
        x=int(mod_inverse(CHINV,26))
        a1=(x*e)%26
        b2=(x*f)%26
        c2=(x*g)%26
        d2=(x*h)%26
        CHAINE = a1 , " " , b2, "  , ", c2 , "   " , d2
                
        
        
    zt6.delete(0,END)
    zt6.insert(0,final)
    zt7.delete(0,END)
    zt7.insert(0,CHAINE)
    return final

# ------ fin fonction
def decryptage():
    final = cryptage()
    a = zt2.get()
    b = zt3.get()
    c = zt4.get()
    d = zt5.get()
    e=int(d)
    f=-int(b)
    g=-int(c)
    h=int(a)
    CHINV=(int(a)*int(d))-(int(b)*int(c))
    x=int(mod_inverse(CHINV,26))
    a1=(x*e)%26
    b2=(x*f)%26
    c2=(x*g)%26
    d2=(x*h)%26
    final2=""
    ii=0
    jj=2
    while jj<(len(final)+1):
        B11=final[ii:jj]
        K1=ord(B11[0])-64
        K2=ord(B11[1])-64
        C11=(((int(a1)*K1)+(int(b2)*K2))%26)
        C22=(((int(c2)*K1)+(int(d2)*K2))%26)
        saye=chr(C11+64)+chr(C22+64)
        final2=final2+saye
        ii=ii+2
        jj=jj+2
    
    zt8.delete(0,END)
    zt8.insert(0,final2)
# Création d'un objet "fenêtre"
fenetre = Tk()  # nouvelle instance de Tk
fenetre.title("cryptage de hill")
fenetre.geometry("600x600")

fenetre.config(bg ="green")
for i in range(1,5):
    fenetre.rowconfigure(i, pad =20)
fenetre.columnconfigure(1,pad = 20)
fenetre.columnconfigure(2, pad =20)

# pour saisir le message a crypter

e1 = Label(fenetre, text = " message a crypter ? ")
e1.grid(row=1, column=1)
zt1 = Entry(fenetre, width=30)
zt1.grid(row=1, column=2)

# pour saisir la matrice clé


e2 = Label(fenetre, text = " M[1,1] ?  ")
e2.grid(row=2, column=1)
zt2 = Entry(fenetre, width=30)
zt2.grid(row=2, column=2)
e3 = Label(fenetre, text = " M[1,2] ?  ")
e3.grid(row=3, column=1)
zt3 = Entry(fenetre, width=30)
zt3.grid(row=3, column=2)
e4 = Label(fenetre, text = " M[2,1] ?  ")
e4.grid(row=4, column=1)
zt4 = Entry(fenetre, width=30)
zt4.grid(row=4, column=2)
e5 = Label(fenetre, text = " M[2,2] ?  ")
e5.grid(row=6, column=1)
zt5 = Entry(fenetre, width=30)
zt5.grid(row=6, column=2)
b1 = Button(fenetre, text = "Crypter", command=cryptage)
b1.grid(row=8, column=3)


b2 = Button(fenetre, text = "decrypter", command=decryptage)
b2.grid(row=100, column=3)
e6 = Label(fenetre, text = "message decrypter = ")
e6.grid(row=110, column=1)
zt8 = Entry(fenetre, width=30)
zt8.grid(row=110, column=2)

e6 = Label(fenetre, text = "message crypté = ")
e6.grid(row=13, column=1)
zt6 = Entry(fenetre, width=30)
zt6.grid(row=13, column=2)
e7 = Label(fenetre, text = "matrice de decryptage = ")
e7.grid(row=30, column=1)
zt7 = Entry(fenetre, width=30)
zt7.grid(row=30, column=2)

fenetre.mainloop()
