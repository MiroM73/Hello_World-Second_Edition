# This tells Python we're making a class Ball
# (blueprint for creating future objects / instances)
class Ball:
    
    # This is method bounce()
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

# Makes an object / instance myBall of class Ball
myBall = Ball()
# Set some attributes for myBall
myBall.direction = "down"
myBall.color = "green"
myBall.size = "small"

# Prints the object's attributes
print "I just created a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "Now I'm going to bounce the ball"
print

# Use a method
myBall.bounce()
print "Now the ball direction is", myBall.direction
