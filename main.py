##############################################
# Title: Project 5: Computer Art- Yacht Sunset
# Programmer: Anika Sharma
# Date: 25/03/2021
# Purpose: To create an art project using Tkinter.
##############################################

#imports and screen setting
from tkinter import *
from random import *
myInterface = Tk()
s = Canvas(myInterface, width=400, height=500, background="white" )
s.pack()




#background
colours = ["#fedf42", "#fedc44", "#fed947", "#fed649", "#fecf4f", "#fdca53", "#fdbd5e", "#fcb860", "#fca96c", "#fca273", "#ff996f", "#ff8d6f", "#ff896f", "#ff7e6e", "#ff816e", "#ff7a6e", "#ff726e", "#ff736e", "#ff6e6d", "#ff6a6d", "#ff686d", "#ff656d", "#ff666d", "#ff646d", "#ff626d", "#ff606d"]

cRange = len(colours)
index = 0
y1 = 0
y2 = 10

for a in range(0,cRange):
  s.create_rectangle(0,y1, 400,y2, fill = colours[index], outline = "")
  index += 1
  y1 += 10
  y2 += 10

#bottom half of the background
colours1 = ["#fefa8f", "#fff883", "#fff861", "#fff53e", "#fef430", "#fff320", "#fff20d", "#fedf42", "#fedc44", "#fed947", "#fed649", "#fecf4f", "#fdca53", "#fdbd5e", "#fcb860", "#fca96c", "#fca273", "#ffa870", "#ffa370", "#ff936f", "#ff946f", "#ff996f", "#ff8d6f", "#ff896f"]

cRange1 = len(colours1)
index = -1

for b in range(0,cRange1):
  s.create_rectangle(0,y1, 400,y2, fill = colours1[index], outline = "")
  index -= 1
  y1 += 10
  y2 += 10




#middle area- the horizon line
s.create_rectangle(0,220, 400,280, fill = "#8b0f0f", outline = "")
s.create_rectangle(0,260, 400,280, fill = "#803225", outline = "")
s.create_rectangle(0,269, 400,280, fill = "#6a3225", outline = "")

#random lines for texture
linesize = 60
y = 265

for c in range(0,30):
  x = randint(0,360)
  s.create_line(x,y, x+linesize,y, fill = "OrangeRed4")
  y -= 1




#the sun
s.create_oval(140,70, 240,170, fill = "#f8e98e", outline = "#fbe97b", width = 2)




#cloud 1- far left
s.create_polygon(0,220, 120,220, 120,200, 80,160, 50,160, 0,180, fill = "#bf2d38", outline = "")
s.create_oval(100,190, 140,220, fill = "#bf2d38", outline = "")
s.create_oval(80,170, 120,200, fill = "#bf2d38", outline = "")
s.create_oval(60,160, 100,180, fill = "#bf2d38", outline = "")
s.create_oval(30,150, 80,180, fill = "#bf2d38", outline = "")
s.create_oval(0,155, 40,195, fill = "#bf2d38", outline = "")

#cloud 1 shadow on the bottom
x = 137
y = 208

for d in range(0,3):
  s.create_line(0,y, x,y, fill = "#8c211b", width = 8)
  x -= 5
  y += 4
s.create_arc(100,190, 140,220, start = 275, extent = 90, fill = "#8c211b", outline = "")




#cloud 2- center- under the sun
s.create_polygon(160,220, 200,180, 240,220, smooth = True, fill = "#bf2d38", outline = "")
s.create_oval(165,210, 200,220, fill = "#bf2d38", outline = "")
s.create_oval(200,200, 240,220, fill = "#bf2d38", outline = "")

#cloud 2 shadow on the bottom
s.create_arc(165,210, 200,220, start = 90, extent = 180, fill = "#8c211b", outline = "")

coorxleft = 180
cooryleftright = 215
coorxright = 225

for e in range(0,2):
  s.create_line(coorxleft,cooryleftright, coorxright,cooryleftright, fill = "#8c211b", width = 8)
  cooryleftright += 2

s.create_arc(200,200, 240,220, start = 275, extent = 90, fill = "#8c211b", outline = "")




#cloud 3- far right
s.create_polygon(280,160, 300,140, 320,140, 320,120, 360,120, 400,90, 400,160, fill = "#bf2d38", outline = "", smooth = True)
s.create_rectangle(340,120, 400,160, fill = "#bf2d38", outline = "")
s.create_oval(280,140, 320,160, fill = "#bf2d38", outline = "")
s.create_oval(300,130, 330,145, fill = "#bf2d38", outline = "")
s.create_oval(340,110, 380,130, fill = "#bf2d38", outline = "")
s.create_oval(380,100, 400,120, fill = "#bf2d38", outline = "")

#cloud 3 shadow on the bottom
s.create_arc(280,140, 320,160, start = 180, extent = 180, fill = "#8c211b", outline = "")

cloudlefty = 152

for f in range(0,3):
  s.create_line(300,cloudlefty, 400,cloudlefty, fill = "#8c211b", width = 5)
  cloudlefty += 3




#last cloud- covering the sun a tiny bit
s.create_polygon(100,120, 140,90, 180,120, fill = "#bf2d38", outline = "", smooth = True)

#shadow
s.create_oval(115,110, 165,120, fill = "#8c211b", outline = "")




#random birds
randomx = randint(40,270)

for g in range(0,2):
  s.create_line(randomx,50, randomx+20,35, randomx+30,50, randomx+40,35, randomx+60,50, fill = "black", width = 2, smooth = True)
  randomx += randint(65,80)




#lines in the lake for texture
y = 485

for h in range(0,40):
  x = randint(0,360)
  s.create_line(x,y, x+10,y-10, x+10,y, x+20,y-10, x+30,y, x+40,y-10, x+50,y, fill = "#fca426", width = 2, smooth = True)
  y -= 5




#the boat's bottom
s.create_arc(100,320, 300,440, start = 180, extent = 180, fill = "black", outline = "")




#the main lines on the right of the boat
s.create_line(200,380, 200,140, fill = "black", width = 3)
s.create_line(200,360, 320,360, fill = "black", width = 2)
s.create_line(200,160, 298,380, fill = "black", width = 5)




#the big right sail
s.create_polygon(200,360, 200,160, 220,260, 240,300, 290,360, fill = "black", outline = "", smooth = True)
s.create_line(200,160, 220,260, 240,300, 290,360, fill = "black", smooth = True, width = 4)
s.create_polygon(200,360, 200,280, 240,360, fill = "black", outline = "")
s.create_polygon(260,360, 260,320, 290,360, fill = "black", outline = "")
s.create_polygon(200,220, 200,160, 215,220, fill = "black", outline = "")




#the tiny right sail
s.create_line(300,380, 300,300, fill = "black", width = 2)
s.create_polygon(300,360, 300,300, 310,330, 315,350, 320,360, fill = "black")
s.create_line(300,360, 300,300, 310,330, 315,350, 320,360, fill = "black", width = 2)




#starting lines for 3 sails on the left
s.create_line(200,150, 120,380, fill = "black", width = 5)
s.create_line(200,210, 140,380, fill = "black", width = 7)
s.create_line(200,300, 160,380, fill = "black", width = 5)




#sail 1- farthest left
s.create_polygon(200,150, 190,180, 190,200, 190,220, 193,240, 180,240, 170,250, 160,260, fill = "black", smooth = True)
s.create_polygon(160,260, 160,280, 157,300, 160,320, 140,340, 130,360, 120,380, fill = "black", smooth = True)
s.create_line(200,150, 190,180, 190,200, 190,220, 193,240, 180,240, 170,250, 160,260, fill = "black", smooth = True, width = 2)
s.create_line(160,260, 160,280, 157,300, 160,320, 140,340, 130,360, 120,380, fill = "black", width = 4, smooth = True)




#sail 2- middle sail
s.create_polygon(200,210, 190,240, 200,260, 190,270, 180,280, 170,300, 170,320, 180,340, 160,350, 140,380, fill = "black", smooth = True)
s.create_line(200,210, 190,240, 200,260, 190,270, 180,280, 170,300, 170,320, 180,340, 160,350, 140,380, fill = "black", smooth = True, width = 3)




#sail 3- closest sail to the center
s.create_polygon(200,300, 197,320, 196,330, 200,340, 180,357, 160,380, fill = "black", smooth = True)
s.create_line(200,300, 197,320, 196,330, 200,340, 180,357, 160,380, fill = "black", smooth = True, width = 1.5)




#shadow effect under boat 1: left
leftshadowy = 430
shadowsize = 40

while leftshadowy < 500:
  s.create_text(120,leftshadowy, text= "......", fill = "black")
  leftshadowy += 3




#shadow effect under boat 2: middle
middleshadowy = 450

while middleshadowy < 500:
  s.create_text(200,middleshadowy, text = "........", fill = "black")
  middleshadowy += 3




#shadow effect under boat 3: right
rightshadowy = 430

while rightshadowy < 500:
  s.create_text(280,rightshadowy, text = "......", fill = "black")
  rightshadowy += 3




#instagram
s.create_text(5,10, text = "@anikas_artsgallery", font = "Ariel 7", fill = "black", anchor = W)

#signature
s.create_text(370,490, text = "A.S", font = "Times 9 italic", fill = "black", anchor = W)