# Lucas Miller UCID: 30245853
# Purpose: Use the input values from the user as a coordinate to center the 

# Have the user enter the coordinates the smiley face will be centered on.
x = int(input("Enter an X coordinate: "))
y = int(input("Enter an Y coordinate: "))

# Next import the SimpleGraphics library.
from SimpleGraphics import *

# Smiley Face Shape
setOutline("black")
setFill("yellow")
ellipse(x-200,y-200,400,400)

# Smiley Face Eyes
setOutline("black")
setFill("black")
ellipse(x-145,y-90,85,85)
ellipse(x+60,y-90,85,85)

# Smiley Face Mouth
setOutline("red")
setWidth(18)
arc(x-95,y-45,190,190,180,180)

# Smiley Face Nose
setOutline("black")
setFill("orange")
setWidth(1)
rect(x-10,y-20,25,75)

# Smiley Face Hair
setOutline("black")
setFill("saddle brown")
pieSlice(x-193,y-215,390,190,0,180)

# Name
setOutline("steel blue")
setFont("Times","12", "bold")
text(690,580, "This is your smiley face!")
