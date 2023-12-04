from drawbot_skia.drawbot import rect, oval, newPage, saveImage, fill, stroke, strokeWidth, newDrawing, font, text
rules = [1, 0, 1, 0, 2, 0, 1, "гусь"] * 20
w, h = 742.5, 1050
newPage(w, h)
margin=80
x = margin
y = h - margin
step = (w - margin * 2) / 6
size = step
for rule in rules:
    if rule == 0:
        fill(0)
        strokeWidth(0)
        oval(x, y - step, size, size)
    elif rule == 1:
        fill(0)
        strokeWidth(0)
        rect(x, y - step, size, size)
    elif rule == 2:
        fill(None)
        stroke(0, 0, 0)
        strokeWidth(3)
        oval (x, y - step, size, size)
    else:
        print(rule, "<— неизвестное правило")
    x += step
    if x >= w - margin:
        x = margin
        y -= step
    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin
saveImage("task-1.pdf")

newDrawing()
rules = [0, 1, 2, 0, 1, 2, "гусь"] * 20
w, h = 742.5, 1050
newPage(w, h)
margin=80
x = margin
y = h - margin
step = (w - margin * 2) / 10
size = step

for rule in rules:
    # круг, если правило == 0
    if rule == 0:
        fill(None)
        stroke(0, 0, 0)
        strokeWidth(1)
        oval (x, y - step, size, size)
        font("Arial", size - 10)
        fill (0,1,0)
        text(":)", (x + 10, y + 15 - step))
    # квадрат, если правило == 1
    elif rule == 1:
        fill(None)
        stroke(0, 0, 0)
        strokeWidth(1)
        oval (x, y - step, size, size)
        font("Arial", size - 10)
        fill (1,0,0)
        text(":(", (x + 10, y + 15 - step))
    elif rule == 2:
        fill(None)
        stroke(0, 0, 0)
        strokeWidth(1)
        oval (x, y - step, size, size)
        font("Arial", size - 10)
        fill (0,0,0)
        text(":/", (x + 10, y + 15 - step))
     # всё другое print в консоль
    else:
        print(rule, "<— неизвестное правило")
    x += step
    if x >= w - margin:
        x = margin
        y -= step
    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin
saveImage("Task-2.pdf")