#Task 1

from drawbot_skia.drawbot import oval, rect, polygon, fill, saveImage, newDrawing, text, font
y = -100
step = 150
for i in range(35):
    oval(500, y, 100, 100)
    y = y + step
saveImage("task-1.pdf")


#Task 2
newDrawing()
x = 50
y = 50
step = 200
for i in range(5):
    for j in range (5):
        oval(x, y, 100, 100)
        y = y + step
    y = 50
    x = x + step
x = 150
y = 50
step = 200
for i in range(4):
    for j in range (35):
        rect(x, y, 100, 100)
        y = y + step
    y = 50
    x = x + step
saveImage("task-2.pdf")


#Task 3 
newDrawing()


y = -100
step = 100
for i in range(35):
    oval(490, y, 120, 120)
    fill (.35, .05, .05)
    y = y + step
y = -100
step = 50
for i in range(35):
    oval(500, y, 100, 100)
    fill (.2, .1, .1)
    y = y + step
font("Times-Italic", 50)
fill (0,0,0)
text("hemorrhoids", (200, 600))
text(")^:", (300, 500))
saveImage("task-3.pdf")
