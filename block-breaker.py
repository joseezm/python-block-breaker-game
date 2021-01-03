# -- coding: utf-8 --
import os
import time
import random

from Tkinter import *

import os
root = Tk()
root.withdraw()


def printMat(m):
	for j in range(len(m[0])):
		c=""
		for i in range(len(m)):
			c+= str(m[i][j])
#		time.sleep(0.01)
		print c



                        

def barra(a,b):
        for k in range (a,b):
                L[int(k)][int(35)]=chr(220)

        
def paredes():        
        for y in range (0,len(L)):
                L[int(y)][int(39)]="_"
        	L[int(y)][int(0)]="."
        for u in range (0,40):
                L[int(0)][int(u)]="."
                L[len(L)-1][int(u)]="."
    
def nivel_0():

        for p in range (12,28):
                L[int(p)][int(3)]=chr(219)
        for p in range (29,36):
                L[int(p)][int(3)]=chr(219)
        for p in range (39,48):
                L[int(p)][int(3)]=chr(219)
        for p in range (11,12):
                L[int(p)][int(4)]=chr(219)
        for p in range (27,28):
                L[int(p)][int(4)]=chr(219)
        for p in range (29,30):
                L[int(p)][int(4)]=chr(219)
        for p in range (35,36):
                L[int(p)][int(4)]=chr(219)
        for p in range (39,40):
                L[int(p)][int(4)]=chr(219)
        for p in range (47,49):
                L[int(p)][int(4)]=chr(219)
        for p in range (11,12):
                L[int(p)][int(5)]=chr(219)
        for p in range (14,21):
                L[int(p)][int(5)]=chr(219)
        for p in range (23,28):
                L[int(p)][int(5)]=chr(219)
        for p in range (29,30):
                L[int(p)][int(5)]=chr(219)
        for p in range (32,33):
                L[int(p)][int(5)]=chr(219)
        for p in range (35,36):
                L[int(p)][int(5)]=chr(219)
        for p in range (39,40):
                L[int(p)][int(5)]=chr(219)
        for p in range (43,45):
                L[int(p)][int(5)]=chr(219)
        for p in range (48,49):
                L[int(p)][int(5)]=chr(219)
        for p in range (11,13):
                L[int(p)][int(6)]=chr(219)
        for p in range (15,17):
                L[int(p)][int(6)]=chr(219)
        for p in range (20,21):
                L[int(p)][int(6)]=chr(219)
        for p in range (23,24):
                L[int(p)][int(6)]=chr(219)
        for p in range (28,29):
                L[int(p)][int(6)]=chr(219)
        for p in range (31,34):
                L[int(p)][int(6)]=chr(219)
        for p in range (36,37):
                L[int(p)][int(6)]=chr(219)
        for p in range (39,40):
                L[int(p)][int(6)]=chr(219)
        for p in range (43,45):
                L[int(p)][int(6)]=chr(219)
        for p in range (48,49):
                L[int(p)][int(6)]=chr(219)
        for p in range (12,14):
                L[int(p)][int(7)]=chr(219)
        for p in range (16,17):
                L[int(p)][int(7)]=chr(219)
        for p in range (20,21):
                L[int(p)][int(7)]=chr(219)
        for p in range (23,24):
                L[int(p)][int(7)]=chr(219)
        for p in range (28,29):
                L[int(p)][int(7)]=chr(219)
        for p in range (31,34):
                L[int(p)][int(7)]=chr(219)
        for p in range (36,37):
                L[int(p)][int(7)]=chr(219)
        for p in range (39,40):
                L[int(p)][int(7)]=chr(219)
        for p in range (46,48):
                L[int(p)][int(7)]=chr(219)
        for t in range (6,14):
                L[int(t)][int(8)]=chr(219)
        for t in range (16,18):
                L[int(t)][int(8)]=chr(219)
        for t in range (20,21):
                L[int(t)][int(8)]=chr(219)
        for t in range (23,24):
                L[int(t)][int(8)]=chr(219)
        for t in range (28,29):
                L[int(t)][int(8)]=chr(219)
        for t in range (36,37):
                L[int(t)][int(8)]=chr(219)
        for t in range (39,40):
                L[int(t)][int(8)]=chr(219)
        for t in range (42,44):
                L[int(t)][int(8)]=chr(219)
        for t in range (47,53):
                L[int(t)][int(8)]=chr(219)
        for p in range (6,8):
                L[int(p)][int(9)]=chr(219)
        for p in range (16,18):
                L[int(p)][int(9)]=chr(219)
        for p in range (20,21):
                L[int(p)][int(9)]=chr(219)
        for p in range (23,24):
                L[int(p)][int(9)]=chr(219)
        for p in range (27,28):
                L[int(p)][int(9)]=chr(219)
        for p in range (31,34):
                L[int(p)][int(9)]=chr(219)
        for p in range (37,38):
                L[int(p)][int(9)]=chr(219)
        for p in range (39,40):
                L[int(p)][int(9)]=chr(219)
        for p in range (42,43):
                L[int(p)][int(9)]=chr(219)
        for p in range (44,45):
                L[int(p)][int(9)]=chr(219)
        for p in range (52,53):
                L[int(p)][int(9)]=chr(219)
        for p in range (6,18):
                L[int(p)][int(10)]=chr(219)
        for p in range (20,24):
                L[int(p)][int(10)]=chr(219)
        for p in range (27,31):
                L[int(p)][int(10)]=chr(219)
        for p in range (34,38):
                L[int(p)][int(10)]=chr(219)
        for p in range (39,43):
                L[int(p)][int(10)]=chr(219)
        for p in range (45,53):
                L[int(p)][int(10)]=chr(219)

        for p in range (6,10):
                L[int(p)][int(12)]=chr(219)
        for p in range (11,15):
                L[int(p)][int(12)]=chr(219)
        for p in range (16,20):
                L[int(p)][int(12)]=chr(219)
        for p in range (21,28):
                L[int(p)][int(12)]=chr(219)
        for p in range (30,39):
                L[int(p)][int(12)]=chr(219)
        for p in range (43,53):
                L[int(p)][int(12)]=chr(219)
        for p in range (6,8):
                L[int(p)][int(13)]=chr(219)
        for p in range (9,10):
                L[int(p)][int(13)]=chr(219)
        for p in range (11,12):
                L[int(p)][int(13)]=chr(219)
        for p in range (14,15):
                L[int(p)][int(13)]=chr(219)
        for p in range (16,17):
                L[int(p)][int(13)]=chr(219)
        for p in range (18,20):
                L[int(p)][int(13)]=chr(219)
        for p in range (21,22):
                L[int(p)][int(13)]=chr(219)
        for p in range (27,28):
                L[int(p)][int(13)]=chr(219)
        for p in range (30,31):
                L[int(p)][int(13)]=chr(219)
        for p in range (38,40):
                L[int(p)][int(13)]=chr(219)
        for p in range (42,43):
                L[int(p)][int(13)]=chr(219)
        for p in range (52,53):
                L[int(p)][int(13)]=chr(219)
        for p in range (7,8):
                L[int(p)][int(14)]=chr(219)
        for p in range (9,12):
                L[int(p)][int(14)]=chr(219)
        for p in range (14,17):
                L[int(p)][int(14)]=chr(219)
        for p in range (18,19):
                L[int(p)][int(14)]=chr(219)
        for p in range (21,22):
                L[int(p)][int(14)]=chr(219)
        for p in range (24,25):
                L[int(p)][int(14)]=chr(219)
        for p in range (27,28):
                L[int(p)][int(14)]=chr(219)
        for p in range (30,31):
                L[int(p)][int(14)]=chr(219)
        for p in range (34,36):
                L[int(p)][int(14)]=chr(219)
        for p in range (39,40):
                L[int(p)][int(14)]=chr(219)
        for p in range (42,43):
                L[int(p)][int(14)]=chr(219)
        for p in range (45,53):
                L[int(p)][int(14)]=chr(219)
        for p in range (7,8):
                L[int(p)][int(15)]=chr(219)
        for p in range (10,11):
                L[int(p)][int(15)]=chr(219)
        for p in range (15,16):
                L[int(p)][int(15)]=chr(219)
        for p in range (18,19):
                L[int(p)][int(15)]=chr(219)
        for p in range (20,21):
                L[int(p)][int(15)]=chr(219)
        for p in range (23,26):
                L[int(p)][int(15)]=chr(219)
        for p in range (28,29):
                L[int(p)][int(15)]=chr(219)
        for p in range (30,31):
                L[int(p)][int(15)]=chr(219)
        for p in range (34,36):
                L[int(p)][int(15)]=chr(219)
        for p in range (39,40):
                L[int(p)][int(15)]=chr(219)
        for p in range (42,44):
                L[int(p)][int(15)]=chr(219)
        for p in range (46,48):
                L[int(p)][int(15)]=chr(219)
        for p in range (7,9):
                L[int(p)][int(16)]=chr(219)
        for p in range (10,11):
                L[int(p)][int(16)]=chr(219)
        for p in range (12,14):
                L[int(p)][int(16)]=chr(219)
        for p in range (15,16):
                L[int(p)][int(16)]=chr(219)
        for p in range (17,19):
                L[int(p)][int(16)]=chr(219)
        for p in range (20,21):
                L[int(p)][int(16)]=chr(219)
        for p in range (23,26):
                L[int(p)][int(16)]=chr(219)
        for p in range (28,29):
                L[int(p)][int(16)]=chr(219)
        for p in range (30,31):
                L[int(p)][int(16)]=chr(219)
        for p in range (37,39):
                L[int(p)][int(16)]=chr(219)
        for p in range (43,45):
                L[int(p)][int(16)]=chr(219)
        for p in range (47,48):
                L[int(p)][int(16)]=chr(219)
        for p in range (8,9):
                L[int(p)][int(17)]=chr(219)
        for p in range (12,14):
                L[int(p)][int(17)]=chr(219)
        for p in range (17,18):
                L[int(p)][int(17)]=chr(219)
        for p in range (20,21):
                L[int(p)][int(17)]=chr(219)
        for p in range (28,29):
                L[int(p)][int(17)]=chr(219)
        for p in range (30,31):
                L[int(p)][int(17)]=chr(219)
        for p in range (33,35):
                L[int(p)][int(17)]=chr(219)
        for p in range (38,45):
                L[int(p)][int(17)]=chr(219)
        for p in range (47,49):
                L[int(p)][int(17)]=chr(219)
        for p in range (8,9):
                L[int(p)][int(18)]=chr(219)
        for p in range (12,14):
                L[int(p)][int(18)]=chr(219)
        for p in range (17,18):
                L[int(p)][int(18)]=chr(219)
        for p in range (19,20):
                L[int(p)][int(18)]=chr(219)
        for p in range (23,26):
                L[int(p)][int(18)]=chr(219)
        for p in range (29,31):
                L[int(p)][int(18)]=chr(219)
        for p in range (33,34):
                L[int(p)][int(18)]=chr(219)
        for p in range (35,36):
                L[int(p)][int(18)]=chr(219)
        for p in range (47,49):
                L[int(p)][int(18)]=chr(219)
        for p in range (8,12):
                L[int(p)][int(19)]=chr(219)
        for p in range (14,18):
                L[int(p)][int(19)]=chr(219)
        for p in range (19,23):
                L[int(p)][int(19)]=chr(219)
        for p in range (26,34):
                L[int(p)][int(19)]=chr(219)
        for p in range (36,48):
                L[int(p)][int(19)]=chr(219)
        for p in range (25,26):
                L[int(p)][int(25)]="P"
        for p in range (26,27):
                L[int(p)][int(25)]="R"
        for p in range (27,28):
                L[int(p)][int(25)]="E"
        for p in range (28,29):
                L[int(p)][int(25)]="S"
        for p in range (29,30):
                L[int(p)][int(25)]="S"
        for p in range (30,31):
                L[int(p)][int(25)]=" "
        for p in range (31,32):
                L[int(p)][int(25)]="A"
 
        
        

def nivel_1 ():
        
        for p in range (22,34):
                L[int(p)][int(2)]=chr(177)
        for p in range (20,22):
                L[int(p)][int(3)]=chr(177)
        for p in range (34,36):
                L[int(p)][int(3)]=chr(177)
        for p in range (18,20):
                L[int(p)][int(4)]=chr(177)
        for p in range (36,38):
                L[int(p)][int(4)]=chr(177)
        for p in range (16,18):
                L[int(p)][int(5)]=chr(177)
        for p in range (38,40):
                L[int(p)][int(5)]=chr(177)
        for p in range (14,16):
                L[int(p)][int(6)]=chr(177)
        for p in range (40,42):
                L[int(p)][int(6)]=chr(177)
        for p in range (14,16):
                L[int(p)][int(7)]=chr(177)
        for p in range (40,42):
                L[int(p)][int(7)]=chr(177)
        for p in range (14,42):
                L[int(p)][int(8)]=chr(177)
        for p in range (14,16):
                L[int(p)][int(9)]=chr(177)
        for p in range (18,26):
                L[int(p)][int(9)]=chr(177)
        for p in range (30,38):
                L[int(p)][int(9)]=chr(177)
        for p in range (40,42):
                L[int(p)][int(9)]=chr(177)
        for p in range (14,16):
                L[int(p)][int(10)]=chr(177)
        for p in range (20,24):
                L[int(p)][int(10)]=chr(177)
        for p in range (32,36):
                L[int(p)][int(10)]=chr(177)
        for p in range (40,42):
                L[int(p)][int(10)]=chr(177)
        for p in range (14,16):
                L[int(p)][int(11)]=chr(177)
        for p in range (26,30):
                L[int(p)][int(11)]=chr(177)
        for p in range (40,42):
                L[int(p)][int(11)]=chr(177)
        for p in range (12,14):
                L[int(p)][int(12)]=chr(177)
        for p in range (24,26):
                L[int(p)][int(12)]=chr(177)
        for p in range (30,32):
                L[int(p)][int(12)]=chr(177)
        for p in range (42,44):
                L[int(p)][int(12)]=chr(177)
        for p in range (12,14):
                L[int(p)][int(13)]=chr(177)
        for p in range (16,18):
                L[int(p)][int(13)]=chr(177)
        for p in range (22,24):
                L[int(p)][int(13)]=chr(177)
        for p in range (32,34):
                L[int(p)][int(13)]=chr(177)
        for p in range (38,40):
                L[int(p)][int(13)]=chr(177)
        for p in range (42,44):
                L[int(p)][int(13)]=chr(177)
        for p in range (12,14):
                L[int(p)][int(14)]=chr(177)
        for p in range (18,20):
                L[int(p)][int(14)]=chr(177)
        for p in range (36,38):
                L[int(p)][int(14)]=chr(177)
        for p in range (42,44):
                L[int(p)][int(14)]=chr(177)
        for p in range (12,14):
                L[int(p)][int(15)]=chr(177)
        for p in range (26,30):
                L[int(p)][int(15)]=chr(177)
        for p in range (42,44):
                L[int(p)][int(15)]=chr(177)
        for p in range (12,14):
                L[int(p)][int(16)]=chr(177)
        for p in range (20,22):
                L[int(p)][int(16)]=chr(204)#
        for p in range (24,26):
                L[int(p)][int(16)]=chr(177)
        for p in range (30,32):
                L[int(p)][int(16)]=chr(177)
        for p in range (34,36):
                L[int(p)][int(16)]=chr(206)#
        for p in range (42,44):
                L[int(p)][int(16)]=chr(177)
        for p in range (14,18):
                L[int(p)][int(17)]=chr(177)
        for p in range (24,26):
                L[int(p)][int(17)]=chr(177)
        for p in range (30,32):
                L[int(p)][int(17)]=chr(177)
        for p in range (38,42):
                L[int(p)][int(17)]=chr(177)
        for p in range (18,22):
                L[int(p)][int(18)]=chr(177)
        for p in range (23,24):
                L[int(p)][int(18)]=chr(206)#
        for p in range (32,33):
                L[int(p)][int(18)]=chr(204)#
        for p in range (33,38):
                L[int(p)][int(18)]=chr(177)

def nivel_2():

        for k in range (25,35):
                L[int(k)][int(3)]=chr(178)
        for p in range (21,25):
                L[int(p)][int(4)]=chr(178)
        for p in range (29,31):
                L[int(p)][int(4)]=chr(177)#
        for p in range (35,39):
                L[int(p)][int(4)]=chr(178)
        for p in range (7,15):
                L[int(p)][int(5)]=chr(178)
        for p in range (19,21):
                L[int(p)][int(5)]=chr(178)
        for p in range (25,35,4):
                L[int(p)][int(5)]=chr(177)#
        for p in range (26,36,4):
                L[int(p)][int(5)]=chr(177)#
        for p in range (39,41):
                L[int(p)][int(5)]=chr(178)
        for p in range (45,53):
                L[int(p)][int(5)]=chr(178)
        for p in range (5,7):
                L[int(p)][int(6)]=chr(178)
        for p in range (15,21):
                L[int(p)][int(6)]=chr(178)
        for p in range (21,23):
                L[int(p)][int(6)]=chr(177)#
        for p in range (37,39):
                L[int(p)][int(6)]=chr(177)#
        for p in range (39,45):
                L[int(p)][int(6)]=chr(178)
        for p in range (53,55):
                L[int(p)][int(6)]=chr(178)
        for p in range (5,11):
                L[int(p)][int(7)]=chr(178)
        for p in range (17,19):
                L[int(p)][int(7)]=chr(178)
        for p in range (25,35):
                L[int(p)][int(7)]=chr(177)#
        for p in range (41,43):
                L[int(p)][int(7)]=chr(178)
        for p in range (49,55):
                L[int(p)][int(7)]=chr(178)
        for p in range (11,13):
                L[int(p)][int(8)]=chr(178)
        for p in range (21,29):
                L[int(p)][int(8)]=chr(178)
        for p in range (31,39):
                L[int(p)][int(8)]=chr(178)
        for p in range (47,49):
                L[int(p)][int(8)]=chr(178)
        for p in range (7,9):
                L[int(p)][int(9)]=chr(204)##
        for p in range (13,19):
                L[int(p)][int(9)]=chr(178)
        for p in range (23,25):
                L[int(p)][int(9)]=chr(206)##
        for p in range (25,27):
                L[int(p)][int(9)]=chr(178)
        for p in range (33,35):
                L[int(p)][int(9)]=chr(204)##
        for p in range (35,37):
                L[int(p)][int(9)]=chr(178)
        for p in range (41,47):
                L[int(p)][int(9)]=chr(178)
        for p in range (51,53):
                L[int(p)][int(9)]=chr(206)##
        for p in range (17,19):
                L[int(p)][int(10)]=chr(178)
        for p in range (23,27):
                L[int(p)][int(10)]=chr(178)
        for p in range (33,37):
                L[int(p)][int(10)]=chr(178)
        for p in range (41,43):
                L[int(p)][int(10)]=chr(178)
        for p in range (17,19):
                L[int(p)][int(11)]=chr(178)
        for p in range (19,25):
                L[int(p)][int(11)]=chr(177)#
        for p in range (35,41):
                L[int(p)][int(11)]=chr(177)#
        for p in range (41,43):
                L[int(p)][int(11)]=chr(178)
        for p in range (17,21):
                L[int(p)][int(12)]=chr(178)
        for p in range (27,33):
                L[int(p)][int(12)]=chr(178)
        for p in range (39,43):
                L[int(p)][int(12)]=chr(178)
        for p in range (21,25):
                L[int(p)][int(13)]=chr(178)
        for p in range (35,39):
                L[int(p)][int(13)]=chr(178)
        for p in range (25,35):
                L[int(p)][int(14)]=chr(178)
                
def nivel_3():

        for w in range (24,28):
                L[int(w)][int(3)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(3)]=chr(178)#
        for w in range (30,32):
                L[int(w)][int(3)]=chr(177)
        for w in range (32,34):
                L[int(w)][int(3)]=chr(178)#
        for w in range (34,38):
                L[int(w)][int(3)]=chr(177)
        for w in range (20,24):
                L[int(w)][int(4)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(4)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(4)]=chr(178)#
        for w in range (38,42):
                L[int(w)][int(4)]=chr(177)
        for w in range (52,54):
                L[int(w)][int(4)]=chr(219)##
        for w in range (16,20):
                L[int(w)][int(5)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(5)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(5)]=chr(178)#
        for w in range (42,46):
                L[int(w)][int(5)]=chr(177)
        for w in range (50,52):
                L[int(w)][int(5)]=chr(219)##
        for w in range (52,54):
                L[int(w)][int(5)]=chr(245)##
        for w in range (54,56):
                L[int(w)][int(5)]=chr(219)##
        for w in range (16,18):
                L[int(w)][int(6)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(6)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(6)]=chr(178)#
        for w in range (44,46):
                L[int(w)][int(6)]=chr(177)
        for w in range (52,54):
                L[int(w)][int(6)]=chr(219)##
        for w in range (6,8):
                L[int(w)][int(7)]=chr(219)##
        for w in range (14,18):
                L[int(w)][int(7)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(7)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(7)]=chr(178)#
        for w in range (44,48):
                L[int(w)][int(7)]=chr(177)
        for w in range (4,6):
                L[int(w)][int(8)]=chr(219)##
        for w in range (6,8):
                L[int(w)][int(8)]=chr(202)##
        for w in range (8,10):
                L[int(w)][int(8)]=chr(219)##
        for w in range (14,16):
                L[int(w)][int(8)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(8)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(8)]=chr(178)#
        for w in range (46,48):
                L[int(w)][int(8)]=chr(177)
        for w in range (6,8):
                L[int(w)][int(9)]=chr(219)##
        for w in range (14,16):
                L[int(w)][int(9)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(9)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(9)]=chr(178)#
        for w in range (46,48):
                L[int(w)][int(9)]=chr(177)
        for w in range (12,14):
                L[int(w)][int(10)]=chr(177)
        for w in range (28,30):
                L[int(w)][int(10)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(10)]=chr(178)#
        for w in range (48,50):
                L[int(w)][int(10)]=chr(177)
        for w in range (12,14):
                L[int(w)][int(11)]=chr(177)
        for w in range (20,30):
                L[int(w)][int(11)]=chr(178)#
        for w in range (32,42):
                L[int(w)][int(11)]=chr(178)#
        for w in range (48,50):
                L[int(w)][int(11)]=chr(177)
        for w in range (12,14):
                L[int(w)][int(12)]=chr(177)
        for w in range (18,20):
                L[int(w)][int(12)]=chr(178)#
        for w in range (28,30):
                L[int(w)][int(12)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(12)]=chr(178)#
        for w in range (42,44):
                L[int(w)][int(12)]=chr(178)#
        for w in range (48,50):
                L[int(w)][int(12)]=chr(177)
        for w in range (12,14):
                L[int(w)][int(13)]=chr(177)
        for w in range (16,20):
                L[int(w)][int(13)]=chr(178)#
        for w in range (30,32):
                L[int(w)][int(13)]=chr(178)#
        for w in range (42,46):
                L[int(w)][int(13)]=chr(178)#
        for w in range (48,50):
                L[int(w)][int(13)]=chr(177)
        for w in range (10,14):
                L[int(w)][int(14)]=chr(177)
        for w in range (16,18):
                L[int(w)][int(14)]=chr(178)#
        for w in range (44,46):
                L[int(w)][int(14)]=chr(178)#
        for w in range (48,52):
                L[int(w)][int(14)]=chr(177)
        for w in range (10,12):
                L[int(w)][int(15)]=chr(177)
        for w in range (16,18):
                L[int(w)][int(15)]=chr(178)#
        for w in range (44,46):
                L[int(w)][int(15)]=chr(178)#
        for w in range (50,52):
                L[int(w)][int(15)]=chr(177)
        for w in range (10,12):
                L[int(w)][int(16)]=chr(177)
        for w in range (14,18):
                L[int(w)][int(16)]=chr(178)#
        for w in range (28,30):
                L[int(w)][int(16)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(16)]=chr(178)#
        for w in range (44,48):
                L[int(w)][int(16)]=chr(178)#
        for w in range (50,52):
                L[int(w)][int(16)]=chr(177)
        for w in range (8,10):
                L[int(w)][int(17)]=chr(177)
        for w in range (14,16):
                L[int(w)][int(17)]=chr(178)#
        for w in range (18,28):
                L[int(w)][int(17)]=chr(178)#
        for w in range (34,44):
                L[int(w)][int(17)]=chr(178)#
        for w in range (46,48):
                L[int(w)][int(17)]=chr(178)#
        for w in range (52,54):
                L[int(w)][int(17)]=chr(177)
        for w in range (8,10):
                L[int(w)][int(18)]=chr(177)
        for w in range (12,14):
                L[int(w)][int(18)]=chr(178)#
        for w in range (30,32):
                L[int(w)][int(18)]=chr(219)##
        for w in range (48,50):
                L[int(w)][int(18)]=chr(178)#
        for w in range (52,54):
                L[int(w)][int(18)]=chr(177)
        for w in range (8,10):
                L[int(w)][int(19)]=chr(177)
        for w in range (12,50,12):
                L[int(w)][int(19)]=chr(178)#
        for w in range (13,51,12):
                L[int(w)][int(19)]=chr(178)#
        for w in range (52,54):
                L[int(w)][int(19)]=chr(177)
        for w in range (8,10):
                L[int(w)][int(20)]=chr(177)
        for w in range (10,12):
                L[int(w)][int(20)]=chr(178)#
        for w in range (14,16):
                L[int(w)][int(20)]=chr(178)#
        for w in range (22,24):
                L[int(w)][int(20)]=chr(178)#
        for w in range (28,29):
                L[int(w)][int(20)]=chr(178)#
        for w in range (29,30):
                L[int(w)][int(20)]=chr(202)#
        for w in range (32,33):
                L[int(w)][int(20)]=chr(245)##
        for w in range (33,34):
                L[int(w)][int(20)]=chr(178)#
        for w in range (38,40):
                L[int(w)][int(20)]=chr(178)#
        for w in range (46,48):
                L[int(w)][int(20)]=chr(178)#
        for w in range (50,52):
                L[int(w)][int(20)]=chr(178)#
        for w in range (52,54):
                L[int(w)][int(20)]=chr(177)
        for w in range (6,10):
                L[int(w)][int(21)]=chr(177)
        for w in range (10,12):
                L[int(w)][int(21)]=chr(178)#
        for w in range (16,18):
                L[int(w)][int(21)]=chr(178)#
        for w in range (20,22):
                L[int(w)][int(21)]=chr(178)#
        for w in range (28,30):
                L[int(w)][int(21)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(21)]=chr(178)#
        for w in range (40,42):
                L[int(w)][int(21)]=chr(178)#
        for w in range (44,46):
                L[int(w)][int(21)]=chr(178)#
        for w in range (50,52):
                L[int(w)][int(21)]=chr(178)#
        for w in range (52,56):
                L[int(w)][int(21)]=chr(177)
        for w in range (6,8):
                L[int(w)][int(22)]=chr(177)
        for w in range (8,12):
                L[int(w)][int(22)]=chr(178)#
        for w in range (18,20):
                L[int(w)][int(22)]=chr(206)#
        for w in range (24,38,4):
                L[int(w)][int(22)]=chr(178)#
        for w in range (25,39,4):
                L[int(w)][int(22)]=chr(178)#
        for w in range (42,44):
                L[int(w)][int(22)]=chr(204)#
        for w in range (50,54):
                L[int(w)][int(22)]=chr(178)#
        for w in range (54,56):
                L[int(w)][int(22)]=chr(177)
        for w in range (6,8):
                L[int(w)][int(23)]=chr(177)
        for w in range (8,12):
                L[int(w)][int(23)]=chr(178)#
        for w in range (20,44,4):
                L[int(w)][int(23)]=chr(178)#
        for w in range (21,45,4):
                L[int(w)][int(23)]=chr(178)#
        for w in range (50,54):
                L[int(w)][int(23)]=chr(178)#
        for w in range (54,56):
                L[int(w)][int(23)]=chr(177)
        for w in range (4,6):
                L[int(w)][int(24)]=chr(177)
        for w in range (6,10):
                L[int(w)][int(24)]=chr(178)#
        for w in range (18,20):
                L[int(w)][int(24)]=chr(219)##
        for w in range (22,26):
                L[int(w)][int(24)]=chr(178)#
        for w in range (28,30):
                L[int(w)][int(24)]=chr(178)#
        for w in range (32,34):
                L[int(w)][int(24)]=chr(178)#
        for w in range (36,40):
                L[int(w)][int(24)]=chr(178)#
        for w in range (42,44):
                L[int(w)][int(24)]=chr(219)##
        for w in range (52,56):
                L[int(w)][int(24)]=chr(178)#
        for w in range (56,58):
                L[int(w)][int(24)]=chr(177)
        for w in range (4,6):
                L[int(w)][int(25)]=chr(177)
        for w in range (6,7):
                L[int(w)][int(25)]=chr(245)##
        for w in range (7,9):
                L[int(w)][int(25)]=chr(178)#
        for w in range (9,10):
                L[int(w)][int(25)]=chr(204)##
        for w in range (10,24):
                L[int(w)][int(25)]=chr(177)
        for w in range (24,38):
                L[int(w)][int(25)]=chr(178)#
        for w in range (38,52):
                L[int(w)][int(25)]=chr(177)
        for w in range (52,53):
                L[int(w)][int(25)]=chr(206)##
        for w in range (53,55):
                L[int(w)][int(25)]=chr(178)#
        for w in range (55,56):
                L[int(w)][int(25)]=chr(202)##
        for w in range (56,58):
                L[int(w)][int(25)]=chr(177)
        for w in range (22,40):
                L[int(w)][int(26)]=chr(177)










      
def task():
    time.sleep(0.03)
    root.after(30, task)
    

def rightKey(event):
        global incx, incy, x, i, barrrapeque, activacionDeBarraP, barraDoble, doblebarra, mov, posicionBarra1, posicionBarra2, activacionDeBarra
        posicionBarra1=126
        posicionBarra2=0
        p=0
        while posicionBarra1==126:
                if L[p][35]==chr(220):
                        posicionBarra1=p
                p=p+1
        if activacionDeBarra==1 and mov>=850 and doblebarra==True:
                posicionBarra2=posicionBarra1+25
        elif activacionDeBarraP==1 and mov>=850 and barrapeque==True:
                posicionBarra2=posicionBarra1+5
        elif activacionDeBarra==0 or activacionDeBarra==4:
                posicionBarra2=posicionBarra1+15
        
        if doblebarra==True:
###
                        if incx==0 and incy==0 and x!=(posicionBarra1+((posicionBarra2-posicionBarra1)//2)):
                            x=x+1 
            
        if posicionBarra2!=len(L)-2 :
                for k in range (posicionBarra1+1,posicionBarra2+2):
                        L[k][35]=chr(220)
                L[posicionBarra1][35]=" "
                if incx==0 and incy==0 and x!=(posicionBarra1+((posicionBarra2-posicionBarra1)//2)):
                    x=x+1
        if bala==True and i!=(posicionBarra1+((posicionBarra2-posicionBarra1)//2)):
                        if incz==0 and incc==0  and i!= (posicionBarra1+((posicionBarra2-posicionBarra1)//2)):
                            i=i+1 
      

                
        
def leftKey(event):
        global incx, incy, x, i, dobleBola, barrrapeque, activacionDeBarraP, doblebarra, posicionBarra1, mov, posicionBarra2, activacionDeBarra
        posicionBarra1=0
        posicionBarra2=0
        
        p=0

        while posicionBarra1==0:          
                if L[p][35]==chr(220):
                        posicionBarra1=p
                p=p+1
                
        if activacionDeBarra==1 and mov>=850 and doblebarra==True:
                posicionBarra2=posicionBarra1+26
        elif activacionDeBarraP==1 and mov>=850 and barrapeque==True:
                posicionBarra2=posicionBarra1+5
        elif activacionDeBarra==0 or activacionDeBarra==4:
                posicionBarra2=posicionBarra1+15

                
                            
        if posicionBarra1!=0:
                for k in range (posicionBarra1-1,posicionBarra2-1):
                        L[k][35]=chr(220)
                        
                        L[posicionBarra2][35]=" "
                if incx==0 and incy==0 and x!=(posicionBarra1+((posicionBarra2-posicionBarra1)//2)):
                    x=x-1

        if doblebarra==True :
                        if incx==0 and incy==0 and x!=(posicionBarra1+((posicionBarra2-posicionBarra1)//2)):
                            x=x-1
        
        if bala==True and i!=5 :
                        if incz==0 and incc==0 and i!=(posicionBarra1+((posicionBarra2-posicionBarra1)//2)):
                            i=i-1



        
        

def UpKey(event):
        global incz, incc, bala
        if bala==True and incz==0 and incc==0:
                incz=1
                incc=1
        

def spaceKey(event):
    global incx, incy, incz, incc
    incx=1
    incy=1
    

def AKey(event):
        global mov, doblebarra, barrapeque, vida, x, y, incx, incy, bUp, doblebola
        
        borrador()
        nivel_1()
        doblebarra=False
        barrapeque=False
        doblebola=False
        for k in range (1,len(L)-1):
                L[int(k)][int(35)]=" "
                for e in range (20,35):
                        L[int(e)][int(35)]=chr(220)
                
        vida=5
        x=27
        y=34

        incx=0
        incy=0
     
        bUp=0
        mov=0
        

def UnoKey(event):
        global mov, doblebarra, barrapeque, vida, x, y, incx, incy, bUp, doblebola
        
        borrador()
        nivel_1()
        doblebarra=False
        barrapeque=False
        doblebola=False
        for k in range (1,len(L)-1):
                L[int(k)][int(35)]=" "
                for e in range (20,35):
                        L[int(e)][int(35)]=chr(220)
                
        vida=5
        x=27
        y=34

        incx=0
        incy=0
     
        bUp=0
        mov=0



def DosKey(event):
        global mov, doblebarra, barrapeque, vida, x, y, incx, incy, bUp, doblebola
        
        borrador()
        nivel_2()
        doblebarra=False
        barrapeque=False
        doblebola=False
        for k in range (1,len(L)-1):
                L[int(k)][int(35)]=" "
                for e in range (20,35):
                        L[int(e)][int(35)]=chr(220)
                
        vida=5
        x=27
        y=34

        incx=0
        incy=0
     
        bUp=0
        mov=0

def TresKey(event):
        global mov, doblebarra, barrapeque, vida, x, y, incx, incy, bUp, doblebola
        
        borrador()
        nivel_3()
        doblebarra=False
        barrapeque=False
        doblebola=False
        for k in range (1,len(L)-1):
                L[int(k)][int(35)]=" "
                for e in range (20,35):
                        L[int(e)][int(35)]=chr(220)
                
        vida=5
        x=27
        y=34

        incx=0
        incy=0
     
        bUp=0
        mov=0
    
def MKey(event):
        global mov, doblebarra, barrapeque, vida, x, y, incx, incy, bUp, doblebola
        
        borrador()
        nivel_0()
        doblebarra=False
        barrapeque=False
        doblebola=False
        for k in range (1,len(L)-1):
                L[int(k)][int(35)]=" "
                for e in range (20,35):
                        L[int(e)][int(35)]=chr(220)
                
        vida=5
        x=27
        y=34

        incx=0
        incy=0
     
        bUp=0
        mov=0

def BKey(event):
        for y in range (3,57):
                L[int(y)][int(2)]=" "
        for y in range (3,57):
                L[int(y)][int(3)]=" "
        for y in range (3,57):
                L[int(y)][int(4)]=" "
        for y in range (3,57):
                L[int(y)][int(5)]=" "
        for y in range (3,57):
                L[int(y)][int(6)]=" "
        for y in range (3,57):
                L[int(y)][int(7)]=" "
        for y in range (3,57):
                L[int(y)][int(8)]=" "
        for y in range (3,57):
                L[int(y)][int(9)]=" "
        for y in range (3,57):
                L[int(y)][int(10)]=" "
        for y in range (3,57):
                L[int(y)][int(11)]=" "
        for y in range (3,57):
                L[int(y)][int(12)]=" "
        for y in range (3,57):
                L[int(y)][int(13)]=" "
        for y in range (3,57):
                L[int(y)][int(14)]=" "
        for y in range (3,57):
                L[int(y)][int(15)]=" "
        for y in range (3,57):
                L[int(y)][int(16)]=" "
        for y in range (3,57):
                L[int(y)][int(17)]=" "
        for y in range (3,57):
                L[int(y)][int(18)]=" "
        for y in range (3,57):
                L[int(y)][int(19)]=" "
        for y in range (3,57):
                L[int(y)][int(20)]=" "
        for y in range (3,57):
                L[int(y)][int(21)]=" "
        for y in range (3,57):
                L[int(y)][int(22)]=" "
        for y in range (3,57):
                L[int(y)][int(23)]=" "
        for y in range (3,57):
                L[int(y)][int(24)]=" "
        for y in range (3,57):
                L[int(y)][int(25)]=" "
        for y in range (3,57):
                L[int(y)][int(26)]=" "
        for y in range (3,57):
                L[int(y)][int(27)]=" "

def borrador():
        for y in range (3,57):
                L[int(y)][int(2)]=" "
        for y in range (3,57):
                L[int(y)][int(3)]=" "
        for y in range (3,57):
                L[int(y)][int(4)]=" "
        for y in range (3,57):
                L[int(y)][int(5)]=" "
        for y in range (3,57):
                L[int(y)][int(6)]=" "
        for y in range (3,57):
                L[int(y)][int(7)]=" "
        for y in range (3,57):
                L[int(y)][int(8)]=" "
        for y in range (3,57):
                L[int(y)][int(9)]=" "
        for y in range (3,57):
                L[int(y)][int(10)]=" "
        for y in range (3,57):
                L[int(y)][int(11)]=" "
        for y in range (3,57):
                L[int(y)][int(12)]=" "
        for y in range (3,57):
                L[int(y)][int(13)]=" "
        for y in range (3,57):
                L[int(y)][int(14)]=" "
        for y in range (3,57):
                L[int(y)][int(15)]=" "
        for y in range (3,57):
                L[int(y)][int(16)]=" "
        for y in range (3,57):
                L[int(y)][int(17)]=" "
        for y in range (3,57):
                L[int(y)][int(18)]=" "
        for y in range (3,57):
                L[int(y)][int(19)]=" "
        for y in range (3,57):
                L[int(y)][int(20)]=" "
        for y in range (3,57):
                L[int(y)][int(21)]=" "
        for y in range (3,57):
                L[int(y)][int(22)]=" "
        for y in range (3,57):
                L[int(y)][int(23)]=" "
        for y in range (3,57):
                L[int(y)][int(24)]=" "
        for y in range (3,57):
                L[int(y)][int(25)]=" "
        for y in range (3,57):
                L[int(y)][int(26)]=" "
        for y in range (3,57):
                L[int(y)][int(27)]=" "

        
        
                





def Pelota():
    global x, y, dobleBola, a, b, bala
    if dobleBola==True and bala==False:
        L [int(x)][int(y)]=chr(169)
        Pelota2()
    elif dobleBola==True and bala==True:
        L [int(x)][int(y)]=chr(169)
        Pelota2()
        Bala()
    if bala==True :
        L [int(x)][int(y)]=chr(169)
        Bala()
    else:
        L[int(x)][int(y)]=chr(169)

def Pelota2():
    global a, b

    L[a][b]="0"

def Bala():
    global i, o
    L[i][o]=chr(202)     

def task():
        global aUp, posicionBarra1, posicionBarra2, doblebarra, activacionDeBarra  
        global L, x, y, bRight, bUp, mov,bala, barrapeque, activacionDeBarraP, incx, incy
        global maxMove, asterisco, asteriscoa, bloque2, bloque2a, bloque3, bloque3a, dobleBola, a, b,aRight
        global incz, incc, i, o, asteriscoz, bloque2z, bloque3z, zUp, zRight, bloquepelotadoble, bloque1, bloquebarragrande, bloquebarrapeque
        global cambiodenivel, menu, nivel1, nivel2, nivel3, buscador, vida
        Pelota()
	printMat(L)
        paredes()
	
# RASTRO DE PELOTA	
	if asterisco==False:
            L[int(x)][int(y)]=chr(220)
            asterisco=True


        elif bloque2==False:
            L[int(x+0.5)][int(y+0.5)]=chr(177)
            bloque2=True

        elif bloque3==False :
            L[int(x)][int(y)]=chr(219)
            bloque3=True
        else:
            L[int(x)][int(y)]=" "
            

        if dobleBola==True:
            if asteriscoa==False:
                L[int(a)][int(b)]=chr(220)
                asteriscoa=True


            elif bloque2a==False:
                L[int(a+0.5)][int(b+0.5)]=chr(177)
                bloque2a=True

            elif bloque3a==False:
                L[int(a+0.5)][int(b+0.5)]=chr(219)
                bloque3a=True
            else:
                L[int(a+0.5)][int(b+0.5)]=" "
                
        if bala==True:

                if bloque2z==False:
                        L[int(i+0.5)][int(o+0.5)]=chr(177)
                        bloque2z=True
                        bala=False
                        incc=0
                        incz=0

                elif bloque3z==False:
                        L[int(i+0.5)][int(o+0.5)]=" "
                        bloque3z=True
                        bala=False
                        incc=0
                        incz=0

                elif bloque1==False:
                        incc=0
                        incz=0
                        L[int(i+0.5)][int(o+0.5)]=" "
                        bloque1=True
                        bala=False
                        
                elif bloquebarragrande==False:
                        incc=0
                        incz=0
                        L[int(i+0.5)][int(o+0.5)]=" "
                        bloquebarragrande=True
                        bala=False

                elif bloquebarrapeque==False:
                        incc=0
                        incz=0
                        L[int(i+0.5)][int(o+0.5)]=" "
                        bloquebarrapeque=True
                        bala=False
                elif bloquepelotadoble==False:
                        incc=0
                        incz=0
                        L[int(i+0.5)][int(o+0.5)]=" "
                        bloquepelotadoble=True
                        bala=False
                        

                else:
                        L[int(i+0.5)][int(o+0.5)]=" "
        




	
        
## EJECUTADOR EN NUEVA VENTANA	
	clear = lambda: os.system('cls')
	clear()
	print " "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+chr(201)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(187)
	print " "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+chr(186)+"BRICK BREAKER"+chr(186)
	print " "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+chr(186)+" "+" "+"STAR WARS"+" "+" "+chr(186)
	print " "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+chr(200)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(205)+chr(188)
	print " "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+" "+"VIDAS:", vida
	

	if mov>maxMove:
		
		
		incx = 1
		incy = 1
		maxMove=1000
		mov=0


## MOVIMIENDTO
	if bRight :
		x=x+incx
	else:
		x=x-incx

	if bUp :
		y=y+incy
	else:
		y=y-incy

        if dobleBola==True:
            if aRight :
                    a=a+inca
            else:
                    a=a-inca

            if aUp :
                    b=b+incb
            else:
                    b=b-incb
                    
        if bala==True:

                if zUp:
                        o=o+incc
                else:
                        o=o-incc
        
	
##CHOQUE CON LATERALES
	if int(x)>=len(L):
		x=x-1
		bRight=False

	elif int(x)<0:
		x=x+1
		bRight=True

	if int(y)>=len(L[0]):
		y=y-1
		bUp=False
	
	elif int(y)<0:
		y=y+1
		bUp=True

        if dobleBola==True:
            if int(a+0.5)>=len(L):
                    a=a-1
                    aRight=False

            elif int(a+0.5)<0:
                    a=a+1
                    aRight=True

            if int(b+0.5)>=len(L[0]):
                    b=b-1
                    aUp=False
            
            elif int(b+0.5)<0:
                    b=b+1
                    aUp=True
		
##CHOQUE DE PELOTA CON LADRILLOS NORMALES
        if bUp==False and L[int(x)][int(y)]==chr(177): 
                bUp=True
                
        elif bUp==True and L[int(x)][int(y)]==chr(177):
                bUp=False


        if dobleBola==True:
            if aUp==False and L[int(a)][int(b)]==chr(177): 
                    aUp=True
                    
            elif aUp==True and L[int(a)][int(b)]==chr(177):
                    aUp=False
                    
            if aUp==False and L[int(a)][int(b)]==chr(245): 
                    aUp=True
                    
            elif aUp==True and L[int(a)][int(b)]==chr(245):
                    aUp=False
                    
        if bala==True:
            if zUp==False and L[int(i)][int(o)]==chr(177): 
                bloque1=False
                incz=0
                incc=0
                
            if zUp==False and L[int(i)][int(o)]==chr(202): 
                bloque1=False
               
                    

                
                    
                    

                    

        

##CHOQUE CON LA BARRA
        if bUp==True and L[int(x)][int(y)]==chr(220):
                bUp=False
                asterisco=False
                
        if dobleBola==True:
            if aUp==True and L[int(a)][int(b)]==chr(220):
                    aUp=False
                    asteriscoa=False


                

##CHOQUE CON LADRILLO 2
        if bUp==False and L[int(x)][int(y)]==chr(178):
                bloque2=False
                bUp=True
        elif bUp==True and L[int(x)][int(y)]==chr(178):
                bloque2=False
                bUp=False

        if dobleBola==True:
            if aUp==False and L[int(a)][int(b)]==chr(178):
                    bloque2a=False
                    aUp=True
            elif aUp==True and L[int(a)][int(b)]==chr(178):
                    bloque2a=False
                    aUp=False
                    
        if bala==True:
                    
            if zUp==False and L[int(i)][int(o)]==chr(178):          
                    bloque2z=False
                    incz=0
                    incc=0



##CHOQUE CON LADRILLO 3
        if bUp==False and L[int(x)][int(y)]==chr(219):
                bloque3=False
                bUp=True
        elif bUp==True and L[int(x)][int(y)]==chr(219):
                bloque3=False
                bUp=False


        if dobleBola==True:
            if aUp==False and L[int(a)][int(b)]==chr(219):
                    bloque3a=False
                    aUp=True
            elif aUp==True and L[int(a)][int(b)]==chr(219):
                    bloque3a=False
                    aUp=False

        if bala==True:
                    
            if zUp==False and L[int(i)][int(o)]==chr(219):
                    bloque3z=False
                    incz=0
                    incc=0
                    

                
                
##GAME OVER
        
        if bUp==False and L[int(x)][int(y)]==".":
                bUp=True
        elif bUp==True and L[int(x)][int(y)]==".":
                bUp=False
        
        if bUp==True and L[int(x)][int(y)]=="_" and dobleBola==False:
                x=(posicionBarra1+((posicionBarra2-posicionBarra1)//2))+1
                y=34

                incx=0
                incy=0
     
                bUp=0
                mov=0
                doblebarra=False
                barrapeque=False
                doblebola=False
                vida=vida-1

                
                
        elif bUp==True and L[int(x)][int(y)]=="_" and dobleBola==True :
                incx=0
                incy=0
                x=(posicionBarra1+((posicionBarra2-posicionBarra1)//2))+1
                y=34
                doblebarra=False
                barrapeque=False
                bala=False
                doblebola=False
                vida=vida-1

        if dobleBola==True:
            if aUp==False and L[int(a)][int(b)]==".":
                    aUp=True
            elif aUp==True and L[int(a)][int(b)]==".":
                    aUp=False
            
            if aUp==True and L[int(a)][int(b)]=="_":
                    dobleBola=False

        if bala==True:
            if zUp==False and L[int(i)][int(o)]==".":
                    bala=False
                    incz=0
                    incc=0

            




##POWERUP - DOBLE PELOTA
        if bUp==False and L[int(x)][int(y)]==chr(245):
                a=(posicionBarra1+((posicionBarra2-posicionBarra1)//2))+1
                bUp=True
                dobleBola=True

        elif bUp==True and L[int(x)][int(y)]==chr(245):
                posicionBarra1+5
                bUp=False
                dobleBola=True

        if bala==True:

                if zUp==False and L[int(i)][int(o)]==chr(245):
                        a=posicionBarra1+5
                        
                        dobleBola=True
                        bloquepelotadoble=False

                elif zUp==True and L[int(i)][int(o)]==chr(245):
                        posicionBarra1+5
                        zUp=False
                        dobleBola=True
                        bloquepelotadoble=False

#POWERUP DOBLEBARRA
        if bUp==False and L[int(x)][int(y)]==chr(206) and doblebarra==False and barrapeque==False:
                bUp=True
                doblebarra=True
                mov=850
                activacionDeBarra=1
        elif bUp==False and L[int(x)][int(y)]==chr(206) and doblebarra==True and barrapeque==False:
                bUp=True
                mov=850

                
        if bUp==True and L[int(x)][int(y)]==chr(206) and doblebarra==False and barrapeque==False:
                bUp=False
                doblebarra=True
                mov=850
                activacionDeBarra=1
                
        elif bUp==True and L[int(x)][int(y)]==chr(206) and doblebarra==True and barrapeque==False:
                bUp=False
                mov=850





        if aUp==False and L[int(a)][int(b)]==chr(206) and doblebarra==False and barrapeque==False:
                aUp=True
                doblebarra=True
                mov=850
                activacionDeBarra=1
        elif aUp==False and L[int(a)][int(b)]==chr(206) and doblebarra==True and barrapeque==False:
                aUp=True
                mov=850

                
        if aUp==True and L[int(a)][int(b)]==chr(206) and doblebarra==False and barrapeque==False:
                aUp=False
                doblebarra=True
                mov=850
                activacionDeBarra=1
                
        elif aUp==True and L[int(a)][int(b)]==chr(206) and doblebarra==True and barrapeque==False:
                aUp=False
                mov=850

                


        if zUp==False and L[int(i)][int(o)]=="7" and doblebarra==False and barrapeque==False and bala==True:
                
                doblebarra=True
                mov=850
                bloquebarragrande=False
                activacionDeBarra=1
                
               
                
        elif zUp==False and L[int(i)][int(o)]=="7" and doblebarra==True and barrapeque==False and bala==True:
                
                
                bloquebarragrande=False
                mov=850





        if doblebarra==True and mov==850 and (posicionBarra2-posicionBarra1)<20 and barrapeque==False:
                if posicionBarra1<26:
                        for k in range (posicionBarra1,posicionBarra2+10):
                                L[int(k)][int(35)]=chr(220)
                elif posicionBarra1>27: 
                        for k in range (posicionBarra1-10, posicionBarra2):
                                L[int(k)][int(35)]=chr(220)

                
        if mov==0 and activacionDeBarra==1:
                for k in range (1,len(L)-1):
                        L[int(k)][int(35)]=" "
                for e in range (posicionBarra1,posicionBarra1+15):
                        L[int(e)][int(35)]=chr(220)
                
                doblebarra=False
                activacionDeBarra=0
                
                if incz==0 and incc==0:
                        i=posicionBarra1+((posicionBarra2-posicionBarra1)//2)
                if incx==0 and incy==0:
                        x=posicionBarra1+((posicionBarra2-posicionBarra1)//2)

##POWER UP BARRAPEQUE
        if bUp==False and L[int(x)][int(y)]==chr(204) and barrapeque==False and doblebarra==False:
                bUp=True
                barrapeque=True
                mov=850
                activacionDeBarraP=1
        elif bUp==False and L[int(x)][int(y)]==chr(204) and barrapeque==True and doblebarra==False:
                bUp=True
                mov=850

                
        if bUp==True and L[int(x)][int(y)]==chr(204) and barrapeque==False and doblebarra==False:
                bUp=False
                barrapeque=True
                mov=850
                activacionDeBarraP=1
                
        elif bUp==True and L[int(x)][int(y)]==chr(204) and barrapeque==True and doblebarra==False:
                bUp=False
                mov=850




        if aUp==False and L[int(a)][int(b)]==chr(204) and barrapeque==False and doblebarra==False:
                aUp=True
                barrapeque=True
                mov=850
                activacionDeBarraP=1
        elif aUp==False and L[int(a)][int(b)]==chr(204) and barrapeque==True and doblebarra==False:
                aUp=True
                mov=850

                
        if aUp==True and L[int(a)][int(b)]==chr(204) and barrapeque==False and doblebarra==False:
                aUp=False
                barrapeque=True
                mov=850
                activacionDeBarraP=1
                
        elif aUp==True and L[int(a)][int(b)]==chr(204) and barrapeque==True and doblebarra==False:
                aUp=False
                mov=850




        if zUp==False and L[int(i)][int(o)]==chr(204) and barrapeque==False and doblebarra==False:
                
                barrapeque=True
                bloquebarrapeque=False
                mov=850
                activacionDeBarraP=1
                
                
        elif zUp==False and L[int(i)][int(o)]==chr(204) and barrapeque==True and doblebarra==False:
                bloquebarrapeque=False
                
                mov=850
                



        if barrapeque==True and mov==850 and posicionBarra2-posicionBarra1<20 and doblebarra==False:
                if posicionBarra1<25 or posicionBarra2<54:
                        for q in range (posicionBarra1, len(L)-2):
                                L[int(q)][int(35)]=" "
                        for k in range (posicionBarra1,posicionBarra2-10):
                                L[int(k)][int(35)]=chr(220)
                        if incx==0 and incy==0:
                                x=posicionBarra1+2
                        if incz==0 and incc==0:
                                i=posicionBarra1+3
                elif posicionBarra2>26:
                        for q in range (posicionBarra1, len(L)-2):
                                L[int(q)][int(35)]=" "
                        for k in range (posicionBarra1+10, posicionBarra2):
                                L[int(k)][int(35)]=chr(220)
                        if incx==0 and incy==0:
                                x=posicionBarra1+2
                        if incz==0 and incc==0:
                                i=posicionBarra1+3

                
        if mov==0 and activacionDeBarraP==1:
                for k in range (1,len(L)-1):
                        L[int(k)][int(35)]=" "
                if posicionBarra1<25:
                        for e in range (posicionBarra1,posicionBarra1+15):
                                L[int(e)][int(35)]=chr(220)
                elif posicionBarra1>26:
                        for h in range (posicionBarra1-15, posicionBarra1):
                                L[int(h)][int(35)]=chr(220)
                
                barrapeque=False
                activacionDeBarraP=0
                if incz==0 and incc==0 and bala==True:
                        i=posicionBarra1+((posicionBarra2-posicionBarra1)//2)
                if incx==0 and incc==0:
                        x=posicionBarra1+((posicionBarra2-posicionBarra1)//2)


## POWER UP BALA D:
        if bUp==False and L[int(x)][int(y)]==chr(202) and bala==False:
                bUp=True
                bala=True
                i=posicionBarra1+((posicionBarra2-posicionBarra1)//2)
                o=34
                
        if bUp==True and L[int(x)][int(y)]==chr(202) and bala==False:
                bUp=False
                bala=True
                i=posicionBarra1+((posicionBarra2-posicionBarra1)//2)
                o=34

        if aUp==False and L[int(a)][int(b)]==chr(202) and bala==False:
                aUp=True
                bala=True
                i=posicionBarra1+((posicionBarra2-posicionBarra1)//2)
                o=34
        if aUp==True and L[int(a)][int(b)]==chr(202) and bala==False:
                aUp=False
                bala=True
                i=posicionBarra1+((posicionBarra2-posicionBarra1)//2)
                o=34

## DETECTOR DE BLOQUES

        if cambiodenivel==False :
                numbloques=0
                for r in range (1, len(L)-37):
                        for t in range (1,len(L[r])-2):
                                if  L[r][t]==chr(177):
                                        numbloques=numbloques+1
                                        buscador=False

                                        if numbloques==0:
                                                buscador=True
                                                nivel2=True
                                                                              

        if menu==True:
                nivel_0()
                menu=False
                mov=0
                
        if nivel1==True:
                nivel_1()
                nivel1=False
                mov=0

        if nivel2==True:
                nivel_2()
                nivel2=False
                mov=0
                
        if nivel3==True:
                nivel_3()
                nivel3=False
                mov=0

## VIDA
        if vida==0:
                borrador()
                nivel_0()
                doblebarra=False
                barrapeque=False
                doblebola=False
                for k in range (1,len(L)-1):
                        L[int(k)][int(35)]=" "
                
                        for e in range (20,35):
                                L[int(e)][int(35)]=chr(220)
                
                vida=5
                x=27
                y=34

                incx=0
                incy=0
     
                bUp=0
                mov=0
                
                
        


        mov = mov+1

	root.after(-1, task)

	
L=[]

for i in range(60):
	c=[]
	for j in range(40):
		c.append(" ")
	L.append(c)
                            

x=30
y=34
a=30
b=34
i=21
o=34

bRight=random.randint(0,1)
bUp=False

aRight=random.randint(0,1)
aUp=0

zRight=0
zUp=False



incx = 0
incy = 0

inca = 1
incb = 1

incz = 0
incc = 0

mov=0
maxMove=1000


asterisco=True
asteriscoa=True
asteriscoz=True

bloque1=True
bloque2=True
bloque2a=True
bloque3=True
bloque3a=True
bloque2z=True
bloque3z=True
bloquebarrapeque=True
bloquebarragrande=True
bloquepelotadoble=True

barraRango1=20
barraRango2=35

doblebarra=False
activacionDeBarra=4

barrapeque=False
activacionDeBarraP=4

dobleBola=False

bala=False

posicionBarra1=20
posicionBarra2=35

i=30
o=34

activacionDeBarra=4

buscador=False
cambiodenivel=False
menu=True
nivel1=False
nivel2=False
nivel3=False


vida=5







barra(barraRango1,barraRango2)                        
   


frame = Frame(root, width=100, height=100)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', UpKey)
root.bind('<space>', spaceKey)
root.bind('<b>', BKey)
root.bind('<m>', MKey)
root.bind('<q>', UnoKey)
root.bind('<w>', DosKey)
root.bind('<e>', TresKey)
root.bind('<a>', AKey)



frame.pack()

root.after(20, task)
root.mainloop()
