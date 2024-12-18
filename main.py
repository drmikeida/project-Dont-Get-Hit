import pyxel
import time

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        # Set the initial position of the candy cane
        # Draw candy cane
        pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)
        
        self.x = 65
        self.y = 55
        self.score = 0
        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2
        # Timer for score increment (in frames, 1 frame = 1/60 seconds)
        self.score_timer = 0
        self.game_over = False
        # Start the game loop
        pyxel.run(self.update, self.draw)
    def update(self):
        # Update the square's position based on arrow keys
        self.game_over == False
        if self.game_over == False:
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= 2
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += 2
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 2
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 2
        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy
        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1
       
        
        # Increment score every 0.5 seconds
        self.score_timer += 1
        if self.game_over == False:
            if self.score_timer >= 20:  # 60 frames = 1 seconds (60 frames per second)
                self.score += 1
                self.score_timer = 0
            
        # Collision Detection
        if abs(self.x  - self.sprite_x) <= 10 and abs(self.y - self.sprite_y) <= 10:
            self.game_over = True
    
    def draw(self):
        # Clear the screen with red (color 4)
        pyxel.cls(4)
        # Draw a square (color 9)
        pyxel.rect(self.x, self.y, 10, 10, 4)
        # Draw candy cane
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)
        # Draw the moving sprite (color 7)
        pyxel.circ(self.sprite_x, self.sprite_y, 5, 7)
        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        # Display a message when score is high
        if self.score >= 15:
            pyxel.text(50, 50, "You’re doing great!", 8) 
        if self.game_over == True:
            pyxel.text(60, 60, "GAME OVER", 1)
            pyxel.text(60, 70, "SCORE: " + str(self.score), 7)
            pyxel.text(60, 80, "PRESS Q TO QUIT", 7)
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
# Run the game
App()