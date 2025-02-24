from SimpleGraphics import *

# Background (Sky) 
background("light sky blue")

# Grass
setFill("medium sea green")
setOutline("medium sea green")
rect(0,475,800,200)

# Sun
setFill("gold")
setOutline("gold")
ellipse(600,50,150,150)

# Cloud
setFill("ghost white")
setOutline("ghost white")
ellipse(200,100,75,75)
ellipse(150,100,75,75)
ellipse(100,100,75,75)
ellipse(125,75,75,75)
ellipse(175,75,75,75)

# Name
setOutline("black")
text(730,570, "Lucas Miller")

# House Walls
setFill("seashell3")
setOutline("black")
rect(280,340,225,180)

# House Roof
setFill("tomato3")
setOutline("black")
polygon(260,340,395,220,525,340)

# House Door
setFill("saddle brown")
setOutline("black")
rect(420,400,50,119)

# Window Background
setFill("yellow1")
setOutline("black")
rect(300,400,100,60)

# Window Frames
setOutline("black")
line(350,400,350,460)
line(300,430,400,430)
