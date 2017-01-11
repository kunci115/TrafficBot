#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:59:10 2017

@author: Rino Alfian
"""

import urllib2
import Tkinter
from ScrolledText import *

root = Tkinter.Tk()

# bikin frame
frame = Tkinter.Frame(root, width = 500, height = 500)
frame.pack()

#buat atur posisi window
w = 500
h = 500

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
o11="http://www.webproxyusa.com/browse.php?u=";
o22="http://free-proxyserver.com/browse.php?u=";
o44="http://www.pinproxy.com/browse.php?u=";
p55="http://covertproxy.com/browse.php?u=";
def inisialisasi(url1,bar):    
    url1 = str(E1.get())
    bar=int(E2.get())
def view():
    url2=E1.get()
    vt=int(E2.get())
    o1=o11
    o2=o22
    o4=o44
    if(vt % 2 != 0 and vt % 3 == 0):
        url = o1 + url2;
    elif(vt % 2 == 0 and vt % 4==0):
        url = o2 + url2;
    elif(vt % 2 ==0 or vt%4 ==0):
        url = o4 + url2;   
    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent',
'Mozilla/5.0')]
    usock = opener.open(url)
    url = usock.geturl()
    data = usock.read()
    usock.close() 
    print("Site Visited")

def calc():
    a=0
    while(a!=E2):
        a=a+1
        view()
def stop():
    root.exit('Dihentikan')
def Exit():
    root.destroy()

#bikin label perintah
L1 = Tkinter.Label(frame, text = "Masukkan Link  ")
L1.place(y = 70, width = 200, height = 35)
E1 = Tkinter.Entry(frame)
E1.place(y = 75, x = 150, width = 300, height = 25)
L2 = Tkinter.Label(frame, text = "Masukkan Jumlah Visitor  ")
L2.place(y = 100, width = 200, height = 35)
E2 = Tkinter.Entry(frame)
E2.place(y = 105, x = 200, width = 100, height = 25)
S1 = Tkinter.Button(frame, text = "Hajar", command = calc)
S1.place(y = 157 , x = 280, width = 100, height = 25)
Judul = Tkinter.Label(frame, text = "Traffic Bot For Your Website")
Judul.place(y = 20, width = 500, height = 30)

E4 = Tkinter.Button(frame, text = "Berhenti", command = stop)
E4.place(y = 180,x = 280, width = 100, height = 25)

E4 = Tkinter.Button(frame, text = "Exit", command = Exit)
E4.place(y = 460, width = 500, height = 40)

root.mainloop()