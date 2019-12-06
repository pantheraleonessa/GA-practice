import turtle

window = turtle.Screen()
spiral = turtle.Turtle() #name for turtle
spiral.shape("turtle")

current = 0 #where we are
seen = set() #where we've been

#increase by 1
for step_size in range(1,100):

    backwards = current - step_size

#step backwards if positive & never been there
    if backwards > 0 and backwards not in seen:
        spiral.setheading(90) #90 degrees straight up
        spiral.circle(step_size/2, 180) #180 degrees means "draw a semicircle"
        current = backwards
        seen.add(current)

#otherwise, go forwards
    else:
        spiral.setheading(270) #270 degrees is straight down
        spiral.circle(step_size/2, 180)
        current += step_size
        seen.add(current)