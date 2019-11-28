import turtle 
import random 

turtle.bgcolor('black')
turtles = [] 
colors = ["yellow", "green", "blue", "red", "grey", "pink"]
n = len(colors)

for index in range(n):
   new_turtle = turtle.Turtle() 
   new_turtle.penup()
   new_turtle.goto(-20, 20)
   turtles.append(new_turtle) 
   
for count in range(10): 
   for index in range(n):
      
      t = random.randint(0, 3)
      if t % 3 == 0 :
             turtles[index].shape('circle')
      elif t % 3 == 1:
             turtles[index].shape('square')
      else :
             turtles[index].shape('triangle')

      size = random.randint(2, 6)
      turtles[index].shapesize(size, size)
      turtles[index].color(colors[index % n])
      c_size = 300
      turtles[index].goto(random.randint(-c_size,c_size), random.randint(-c_size,c_size))
      turtles[index].stamp()
