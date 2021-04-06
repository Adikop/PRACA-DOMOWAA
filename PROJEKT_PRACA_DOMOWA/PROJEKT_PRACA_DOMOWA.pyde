def setup():
    size(400, 400)
    textSize(50)
def draw():
    clear()
    background(200, 100, 200)
    fill(60, 255, 40)
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.vertex(300, 100)
    s.vertex(100, 50)
    s.vertex(230, 200)
    s.vertex(60, 60)
    s.vertex(100, 20)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    text("Adrian K", width/14, height/1.5)
    if hex(get(mouseX, mouseY)) =='FF0000FF':
        fill(200, 0, 150)
        text("Adrian K", width/14, height/1.5)
      #brakuje zaznaczania napisu na klikanie A i K na klawiaturze  
#1,25pkt
