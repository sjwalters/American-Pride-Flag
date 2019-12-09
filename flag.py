"""This program draws a version of the American flag reimaged as a pride flag."""

#fastest speed setting so Tracy draws the flag quickly
speed(0)

#Set Tracy's starting position to the upper left corner of the canvas
penup()
setposition(-200,200)
pendown()

#Length of the flag
fly = 400

#Width of flag (proportions obtained from usflag.org)
hoist = (1/1.9)*400

#length of blue square(black for this version)
fly_of_union = 0.76*hoist

#width of blue square (black for this version)
hoist_of_union = 0.5385*hoist

#There are nine rows of stars on the US flag, this variable keeps track of the 
#current row number
star_row_number = 1

#List holds the stripe colors in order
colors = ["black", "red" ,"black", "orange", "black", "yellow", "black", "green"
,"black", "blue","black", "magenta", "black"]

#This function will draw the stripes when called, it takes one parameter
#stripe_color. stripe_color will come from the colors list
def draw_stripes(stripe_color):
    begin_fill()
    color(stripe_color)
    forward(fly)
    right(90)
    forward(0.0780*hoist)
    right(90)
    forward(fly)
    left(180)
    end_fill()   

#This for loop draws all thirteen strips.  It useds the index of the colors list
#to know what color to pass into the draw_stripes function
for i in range(13):
    draw_stripes(colors[i])

#After drawing the stripes, set Tracy's position back to the upper left corner
penup()
setposition(-200, 200)
pendown()

# This function draws the black square
begin_fill()
for i in range(2):
    color("black")
    forward(fly_of_union)
    right(90)
    forward(hoist_of_union)
    right(90)
end_fill()  

#This fuction moves Tracy to the correct position to draw stars if the stars 
#are in an odd row, it takes one parameter the star_row_number (1-9)
def move_to_position_odd_row(star_row_number):
    penup()
    setposition(-200, 200)
    color("white")
    forward(0.063*hoist - 0.0308)
    right(90)
    forward(star_row_number*0.054*hoist)
    left(90)
    
#This fuction moves Tracy to the correct position to draw stars if the stars 
#are in an even row, it takes one parameter the star_row_number (1-9)
def move_to_position_even_row(star_row_number):
    penup()
    setposition(-200, 200)
    color("white")
    forward(0.126*hoist - 0.0308)
    right(90)
    forward(star_row_number*(0.054*hoist))
    left(90)    

#This function draws a white five-pointed star    
def draw_stars():
    begin_fill()
    color("white")
    for i in range(4):
        pendown()
        forward(0.0616*hoist_of_union)
        right(144)
    forward(0.0616*hoist_of_union)
    right(144)
    penup()
    forward(0.1232*hoist)
    end_fill()
    
#This loop draws all 50 stars in their proper configuration
for i in range(9): #9 is the total number of rows of stars   
    if star_row_number % 2 != 0: # odd row number
        move_to_position_odd_row(star_row_number)
        for i in range(6):
            draw_stars()
    else: # meaning its an even row
        move_to_position_even_row(star_row_number)
        for i in range(5):
            draw_stars()
    star_row_number += 1 # very important! increases the varible coutning the star row

#Moves Tracy to the bottom of the screen so she is not on the flag when it is done
setposition(0,-200)


"""Standard US Flag Proportions
Hoist (width) of flag (A) 1.0
Fly (length) of flag (B) 1.9
Hoist (width) of Union (C) 0.5385 (7/13)
Fly (length) of Union (D) 0.76
(E) 0.054
(F) 0.054
(G) 0.063
(H) 0.063
Diameter of star (K) 0.0616
Width of stripe (L) 0.0769 ( 1/13)"""
