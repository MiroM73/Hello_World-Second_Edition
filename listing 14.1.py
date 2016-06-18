# This tells Python we're making a class
class Ball:
    
    # This is method bounce()
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
