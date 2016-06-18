class Ball:
    # Here's __init__() method.
    # 2 underscores on either side of init.
    # Total of 4 underscores, 2 on either side.
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction
        
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

# Attributes are passed in as arguments to __init__()
myBall = Ball("red","small","down")
print "I just created a ball."

print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "Now I'm going to bounce the ball"
print

myBall.bounce()
print "Now the ball direction is", myBall.direction
