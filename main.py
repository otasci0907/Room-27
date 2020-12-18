'''
Room 27

Orhan Tasci
William Zhong
Benjamin Li
'''

'''
main.py

This file contains the main functions of the game.
This file displays all the images for the game and holds the player class.
'''

#import modules needed
import pygame
import sys
import constants as cn
import levels as lvl
import os
import player as pl

#initialize pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
icon = pygame.image.load(os.path.join(cn.BG_DIR, 'room-27.png'))
pygame.display.set_icon(icon)
win = pygame.display.set_mode((cn.WIDTH, cn.HEIGHT))
pygame.display.set_caption("Room 27")
clock = pygame.time.Clock()
volume = 0.01
first = pygame.mixer.Sound(os.path.join(cn.MUSIC_DIR, 'rustboro.mp3'))
first.play(-1)

currentlySelected = "play"

leaderBoardText = "Leaderboard"
rank1 = "ABG: 15"
rank2 = "WEN: 17"
rank3 = "GER: 18"
rank4 = "TES: 21"

greenButton = pygame.Rect(lvl.greenCoords, lvl.buttonSizes)
blueButton = pygame.Rect(lvl.blueCoords, lvl.buttonSizes)
yellowButton = pygame.Rect(lvl.yellowCoords, lvl.buttonSizes)
redButton = pygame.Rect(lvl.redCoords, lvl.buttonSizes)
entered = []

green = cn.GREEN
blue = cn.BLUE
yellow = cn.YELLOW
red = cn.RED

foundCode = ['_', '_', '_', '_']
encoded = ['^', '@', '!@','!']

scrambled = "fhsokbeol"
typed = []
storySetup2 = "You heard the door lock behind you, and a scrambled message appears on the door lock!"
solveText = "Unscramble " + scrambled + " to unlock the door to the room!"
unscrambled = ['b', 'o', 'o', 'k', 's', 'h', 'e', 'l', 'f']
typedLetters = ""

typedDecode = []
decodingChallenge = "Throughout this hotel, you have been finding letters to a code to leave the hotel."
typedLettersDecode = ""
decoded = ['f', 'b', 'l', 'a']

displayLevel1Win = False
displayLevel1Lose = False

displayLevel2Win = False
displayLevel2Lose = False

displayWinGame = False
displayLoseGame = False

#function to store the procedures to redraw the game window
def redrawGameWindow():
    win.blit(cn.bg, (0,0))
    player.score = int(pygame.time.get_ticks() / 5000)
    lives = "Lives: " + str(player.lives)
    if player.gameState == "title":
        selectedFont = 60
        unselectedFont = 40
        if currentlySelected == "play":
            playText = lvl.Text(640, 360, cn.WHITE, "Play", selectedFont)
            instructionsText = lvl.Text(640, 420, cn.WHITE, "Instructions", unselectedFont)
        elif currentlySelected == "instructions":
            playText = lvl.Text(640, 360, cn.WHITE, "Play", unselectedFont)
            instructionsText = lvl.Text(640, 420, cn.WHITE, "Instructions", selectedFont)
        playText.draw(win)
        instructionsText.draw(win)
        lvl.titleText.draw(win)

    if player.gameState == "instructions":
        lvl.instructions1.draw(win)
        lvl.instructions2.draw(win)
        lvl.instructions3.draw(win)
        lvl.instructions4.draw(win)
        lvl.instructions5.draw(win)
        lvl.instructions6.draw(win)

    if player.gameState == "1":
        scoreText = lvl.Text(45, 40, cn.WHITE, str(player.score), 40)
        livesText = lvl.Text(1215, 40, cn.WHITE, lives, 40)
        livesText.draw(win)
        scoreText.draw(win)
        lvl.room1.draw(win)
        pygame.draw.rect(win, cn.WHITE, (840, 600, 400, 60))
        if lvl.room1Text == 1:
            lvl.puzzleDirections.draw(win)
        elif lvl.room1Text == 2:
            lvl.pressEnter.draw(win)
        elif lvl.room1Text == 3:
            lvl.first.draw(win)
        elif lvl.room1Text == 4:
            lvl.second.draw(win)
        elif lvl.room1Text == 5:
            lvl.third.draw(win)
        elif lvl.room1Text == 6:
            lvl.fourth.draw(win) 

    if player.gameState == "2":
        scoreText = lvl.Text(315, 40, cn.WHITE, str(player.score), 40)
        livesText = lvl.Text(960, 40, cn.WHITE, lives, 40)
        livesText.draw(win)
        scoreText.draw(win)
        lvl.room27.draw(win)
        pygame.draw.rect(win, cn.WHITE, (840, 600, 400, 60))
        if lvl.room27Text == 1:
            lvl.puzzleDirections.draw(win)
        elif lvl.room27Text == 2:
            lvl.pressEnter.draw(win)

    if player.gameState == "3":
        scoreText = lvl.Text(315, 40, cn.WHITE, str(player.score), 40)
        livesText = lvl.Text(960, 40, cn.WHITE, lives, 40)
        livesText.draw(win)
        scoreText.draw(win)
        lvl.roomSuper.draw(win)
        pygame.draw.rect(win, cn.WHITE, (840, 600, 400, 60))
        if lvl.roomSuperText == 1:
            lvl.puzzleDirections.draw(win)
        elif lvl.roomSuperText == 2:
            lvl.pressEnter.draw(win)
    
    if player.gameState == "1" or player.gameState == "2" or player.gameState == "3":
        player.draw(win)
        pygame.draw.rect(win, cn.WHITE, (0, 600, 400, 60))
        codeText = "code" + ' ' + foundCode[0] + ' ' + foundCode[1] + ' ' + foundCode[2] + ' ' + foundCode[3]
        code = lvl.Text(190, 630, cn.BLACK, codeText, 40)
        code.draw(win)
        if lvl.gamemode == True:
            pygame.draw.rect(win, cn.BLACK, (0, 0, 1280, 720))
            if player.gameState == "1":
                lvl.simonSetup.draw(win)
                lvl.simonSetup2.draw(win)
                lvl.simonDirections.draw(win)
                pygame.draw.rect(win, green, greenButton)
                pygame.draw.rect(win, blue, blueButton)
                pygame.draw.rect(win, yellow, yellowButton)
                pygame.draw.rect(win, red, redButton)

                if displayLevel1Win:
                    win1Text = lvl.Text(cn.WIDTH / 2, 650, cn.WHITE, "Congratulations! You have passed the Check in Room!", 40)
                    win1Text2 = lvl.Text(cn.WIDTH / 2, 680, cn.WHITE, "Press [Enter] to continue to the next room!", 40)
                    win1Text.draw(win)
                    win1Text2.draw(win)
                elif displayLevel1Lose:
                    lose1Text = lvl.Text(cn.WIDTH / 2, 650, cn.WHITE, "Unfortunately you have failed the Check In Room Puzzle! You have lost 1 life!", 40)
                    lose1Text2 = lvl.Text(cn.WIDTH / 2, 680, cn.WHITE, "Press [Enter] to continue to the next room!", 40)
                    lose1Text.draw(win)
                    lose1Text2.draw(win)
            if player.gameState == "2":
                directions = lvl.Text(cn.WIDTH / 2, 40, cn.WHITE, "Choose the correct unscrambling by pressing the key that corresponds with your choice", 40)
                directions.draw(win)
                if displayLevel2Win:
                    win2Text = lvl.Text(cn.WIDTH / 2, 650, cn.WHITE, "Congratulations! You have passed your room!", 40)
                    win2Text2 = lvl.Text(cn.WIDTH / 2, 680, cn.WHITE, "Press [Enter] to continue to the final room!", 40)
                    win2Text.draw(win)
                    win2Text2.draw(win)
                elif displayLevel2Lose:
                    lose2Text = lvl.Text(cn.WIDTH / 2, 650, cn.WHITE, "Unfortunately you have failed your room's puzzle! You have lost 1 life!", 40)
                    lose2Text2 = lvl.Text(cn.WIDTH / 2, 680, cn.WHITE, "Press [Enter] to continue to the next room!", 40)
                    lose2Text.draw(win)
                    lose2Text2.draw(win)
                question = lvl.Text(cn.WIDTH / 2, 200, cn.WHITE, solveText, 40)
                enteredText = lvl.Text(cn.WIDTH / 2, 250, cn.WHITE, typedLetters, 40)
                question.draw(win)
                enteredText.draw(win)
            if player.gameState == "3":
                room3Setup = lvl.Text(cn.WIDTH / 2, 40, cn.WHITE, decodingChallenge, 40)
                roomDirections = lvl.Text(cn.WIDTH / 2, 70, cn.WHITE, "Decode the following code that you have found while exploring the hotel!", 40)
                roomHint = lvl.Text(cn.WIDTH / 2, 100, cn.WHITE, "[Hint: symbols to numbers to letters]", 30)
                roomDirections.draw(win)
                roomHint.draw(win)
                if displayWinGame:
                    win3Text = lvl.Text(cn.WIDTH / 2, 650, cn.WHITE, "Congratulations! You have defeated the supervisor!", 40)
                    win3Text2 = lvl.Text(cn.WIDTH / 2, 680, cn.WHITE, "Press [Enter] to exit the hotel!", 40)
                    win3Text.draw(win)
                    win3Text2.draw(win)
                elif displayLoseGame:
                    lose2Text = lvl.Text(cn.WIDTH / 2, 650, cn.WHITE, "Unfortunately you have failed to defeat the supervisor", 40)
                    lose2Text2 = lvl.Text(cn.WIDTH / 2, 680, cn.WHITE, "Press [Enter] to continue to the next room!", 40)
                    lose2Text.draw(win)
                    lose2Text2.draw(win)
                questionDecode = lvl.Text(cn.WIDTH / 2, 200, cn.WHITE, codeText, 40)
                decodedText = lvl.Text(cn.WIDTH / 2, 250, cn.WHITE, typedLettersDecode, 40)
                questionDecode.draw(win)
                decodedText.draw(win)
        
    if player.gameState == "win":
        winText = lvl.Text(640, 200, cn.WHITE, "YOU WIN!!!", 150)
        winsubText = lvl.Text(640, 280, cn.WHITE, "You have successfully completed all the puzzles!", 50)
        winsubText3 = lvl.Text(640, 310, cn.WHITE, "and have escaped from the hotel!!", 50)
        winsubText2 = lvl.Text(640, 700, cn.WHITE, "Press [Escape] to exit the game.", 40)
        winText.draw(win)
        winsubText.draw(win)
        winsubText2.draw(win)
        winsubText3.draw(win)
    if player.gameState == "lose":
        loseText = lvl.Text(640, 200, cn.WHITE, "You have failed!", 150)
        losesubText = lvl.Text(640, 280, cn.WHITE, "You have lost all of your lives", 50)
        losesubText3 = lvl.Text(640, 310, cn.WHITE, "and could not escape the hotel", 50)
        losesubText2 = lvl.Text(640, 700, cn.WHITE, "Press [Escape] to exit the game.", 40)
        loseText.draw(win)
        losesubText.draw(win)
        losesubText2.draw(win)
        losesubText3.draw(win)

    if player.gameState == "win" or player.gameState == "lose":
        if player.gameState == "lose":
            rank5 = "YOU: failed"
        elif player.gameState == "win":
            rank5 = "YOU: " + str(player.score)
        leaderboard = lvl.Text(640, 430, cn.WHITE, leaderBoardText, 40)
        rankText1 = lvl.Text(640, 450, cn.WHITE, rank1, 30)
        rankText2 = lvl.Text(640, 470, cn.WHITE, rank2, 30)
        rankText3 = lvl.Text(640, 490, cn.WHITE, rank3, 30)
        rankText4 = lvl.Text(640, 510, cn.WHITE, rank4, 30)
        yourRank = lvl.Text(640, 530, cn.WHITE, rank5, 30)
        leaderboard.draw(win)
        rankText1.draw(win)
        rankText2.draw(win)
        rankText3.draw(win)
        rankText4.draw(win)
        yourRank.draw(win)
    pygame.display.update()

#create main player object
player = pl.Player(cn.WIDTH / 2 - 32, cn.HEIGHT / 2 + 100, 76, 108)

simonSays = False
correct = []

jumbled = False

decode = False

#main loop
run = True
while run:
    #get the clock ticking
    clock.tick(27)
    keys = pygame.key.get_pressed()

    if player.gameState == "1" and lvl.gamemode == True:
        simonSays = True
    else:
        simonSays = False

    if player.gameState == "2" and lvl.gamemode == True:
        jumbled = True
    else:
        jumbled = False

    if player.gameState == "3" and lvl.gamemode == True:
        decode = True
    else:
        decode = False

    #if the program is quit, close it (duh)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            first.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if simonSays:
                green = cn.GREEN
                yellow = cn.YELLOW
                blue = cn.BLUE
                red = cn.RED
                if greenButton.collidepoint(mouse_pos):
                    entered.append("green")
                    green = (0, 200, 0)
                elif yellowButton.collidepoint(mouse_pos):
                    entered.append("yellow")
                    yellow = (200, 200, 0)
                elif blueButton.collidepoint(mouse_pos):
                    entered.append("blue")
                    blue = (0, 0, 200)
                elif redButton.collidepoint(mouse_pos):
                    entered.append("red")
                    red = (200, 0, 0)

                if len(entered) == 4:
                    for i in range(len(entered)):
                        if entered[i] == lvl.simonPattern[i]:
                            correct.append("true")
                        else:
                            player.lives = 1
                            if player.lives == 0:
                                player.gameState = "lose"

    if correct.count("true") == 4 and player.gameState == "1":
        foundCode[1] = '@'
        displayLevel1Win = True
        if keys[pygame.K_RETURN]:
            lvl.gamemode = False
            displayLevel1Win = False
            player.gameState = "2"

    elif len(entered) == 4 and correct.count("true") != 4 and player.gameState == "1":
        player.lives = 1
        if player.lives == 0:
            player.gameState = "lose"
        else:
            displayLevel1Lose = True
            if keys[pygame.K_RETURN]:
                displayLevel1Lose = False
                lvl.gamemode = False
                player.gameState = "2"

    if len(entered) > 4 and player.gameState == "1":
        player.lives = 1
        if player.lives == 0:
            player.gameState = "lose"
        else:
            displayLevel1Lose = True
            if keys[pygame.K_RETURN]:
                displayLevel1Lose = False
                lvl.gamemode = False
                player.gameState = "2"

    if player.gameState == "1":
        for i in range(len(lvl.room1.furniture)):
            if player.rect.colliderect(lvl.room1.furniture[i].get_rect(topleft = lvl.room1.coords[i])):
                player.collided = True

        couch1Rect = lvl.room1.furniture[5].get_rect(topleft = lvl.room1.coords[5])
        tableRect = lvl.room1.furniture[10].get_rect(topleft = lvl.room1.coords[10])
        couchRect = lvl.room1.furniture[2].get_rect(topleft = lvl.room1.coords[2])
        deskRect = lvl.room1.furniture[8].get_rect(topleft = lvl.room1.coords[8])
        sofaRect = lvl.room1.furniture[0].get_rect(topleft = lvl.room1.coords[0])
        codeRect = lvl.room1.furniture[3].get_rect(topleft = lvl.room1.coords[3])
        if player.rect.top - 10 <= deskRect.top + deskRect.height and player.rect.left + player.rect.width + 10 >= deskRect.left and player.rect.left - 10 <= deskRect.left + deskRect.width and player.rect.top + player.rect.height + 10 >= deskRect.top:
            lvl.room1Text = 2
            if keys[pygame.K_RETURN]:
                lvl.gamemode = True
            elif keys[pygame.K_w]:
                entered = []
        elif player.rect.top - 10 <= couchRect.top + couchRect.height and player.rect.left + player.rect.width + 10 >= couchRect.left and player.rect.left - 10 <= couchRect.left + couchRect.width and player.rect.top + player.rect.height + 10 >= couchRect.top:
            lvl.room1Text = 3
        elif player.rect.top - 10 <= tableRect.top + tableRect.height and player.rect.left + player.rect.width + 10 >= tableRect.left and player.rect.left - 10 <= tableRect.left + tableRect.width and player.rect.top + player.rect.height + 10 >= tableRect.top:
            lvl.room1Text = 4
        elif player.rect.top - 10 <= couch1Rect.top + couch1Rect.height and player.rect.left + player.rect.width + 10 >= couch1Rect.left and player.rect.left - 10 <= couch1Rect.left + couch1Rect.width and player.rect.top + player.rect.height + 10 >= couch1Rect.top:
            lvl.room1Text = 5
        elif player.rect.top - 10 <= sofaRect.top + sofaRect.height and player.rect.left + player.rect.width + 10 >= sofaRect.left and player.rect.left - 10 <= sofaRect.left + sofaRect.width and player.rect.top + player.rect.height + 10 >= sofaRect.top:
            lvl.room1Text = 6
        elif player.rect.top - 10 <= codeRect.top + codeRect.height and player.rect.left + player.rect.width + 10 >= codeRect.left and player.rect.left - 10 <= codeRect.left + codeRect.width and player.rect.top + player.rect.height + 10 >= codeRect.top:
            foundCode[0] = '^'
        else:
            lvl.room1Text = 1

    if player.gameState == "2":
        for i in range(len(lvl.room27.furniture)):
            if player.rect.colliderect(lvl.room27.furniture[i].get_rect(topleft = lvl.room27.coords[i])):
                player.collided = True

        deskRect = lvl.room27.furniture[3].get_rect(topleft = lvl.room27.coords[3])
        ottomanRect = lvl.room27.furniture[0].get_rect(topleft = lvl.room27.coords[0])
        if player.rect.top - 10 <= deskRect.top + deskRect.height and player.rect.left + player.rect.width + 10 >= deskRect.left and player.rect.left - 10 <= deskRect.left + deskRect.width and player.rect.top + player.rect.height + 10 >= deskRect.top:
            lvl.room27Text = 2
            if keys[pygame.K_RETURN]:
                lvl.gamemode = True
            elif keys[pygame.K_w]:
                lvl.gamemode = False
        elif player.rect.top - 10 <= ottomanRect.top + ottomanRect.height and player.rect.left + player.rect.width + 10 >= ottomanRect.left and player.rect.left - 10 <= ottomanRect.left + ottomanRect.width and player.rect.top + player.rect.height + 10 >= ottomanRect.top:
            foundCode[2] = '!@'
        else:
            lvl.room27Text = 1

    if player.gameState == "3":
        for i in range(len(lvl.roomSuper.furniture)):
            if player.rect.colliderect(lvl.roomSuper.furniture[i].get_rect(topleft = lvl.roomSuper.coords[i])):
                player.collided = True

        deskRect = lvl.roomSuper.furniture[4].get_rect(topleft = lvl.roomSuper.coords[4])
        if player.rect.top - 10 <= deskRect.top + deskRect.height and player.rect.left + player.rect.width + 10 >= deskRect.left and player.rect.left - 10 <= deskRect.left + deskRect.width and player.rect.top + player.rect.height + 10 >= deskRect.top:
            lvl.roomSuperText = 2
            if keys[pygame.K_RETURN]:
                lvl.gamemode = True
            elif keys[pygame.K_w]:
                lvl.gamemode = False
        else:
            lvl.roomSuperText = 1

    if player.gameState != "title" and player.gameState != "win" and player.gameState != "lose":
        #detect arrow key presses and move the player accordingly
        if player.gameState == "1":
            if keys[pygame.K_LEFT] and player.x > player.vel  and player.collided == False:
                player.rect.left -= player.vel
                player.x -= player.vel
                player.left = True
                player.right = False
                player.up = False
                player.down = False
                cn.char = cn.standLeft

            elif keys[pygame.K_RIGHT] and player.rect.x < cn.WIDTH - player.rect.width - player.vel  and player.collided == False:
                player.rect.left += player.vel
                player.x += player.vel
                player.right = True
                player.left = False
                player.up = False
                player.down = False
                cn.char = cn.standRight

            elif keys[pygame.K_UP] and player.rect.y > player.vel + 100  and player.collided == False:
                player.rect.top -= player.vel
                player.y -= player.vel
                player.left = False
                player.right = False
                player.up = True
                player.down = False
                cn.char = cn.standBack

            elif keys[pygame.K_DOWN] and player.rect.y < cn.HEIGHT - player.rect.height - player.vel  and player.collided == False:
                player.rect.top += player.vel
                player.y += player.vel
                player.right = False
                player.left = False
                player.up = False
                player.down = True
                cn.char = cn.standForward
            
            elif player.collided == True:
                if cn.char == cn.standLeft:
                    player.x += player.vel
                    player.rect.left += player.vel
                    player.right = True
                    player.left = False
                    player.up = False
                    player.down = False
                    player.collided = False
                    cn.char = cn.standRight
                elif cn.char == cn.standRight:
                    player.x -= player.vel
                    player.rect.left -= player.vel
                    player.right = False
                    player.left = True
                    player.up = False
                    player.down = False
                    player.collided = False
                    cn.char = cn.standLeft
                elif cn.char == cn.standBack:
                    player.rect.top += player.vel
                    player.y += player.vel
                    player.right = False
                    player.left = False
                    player.up = False
                    player.down = True
                    player.collided = False
                    cn.char = cn.standForward
                elif cn.char == cn.standForward:
                    player.rect.top -= player.vel
                    player.y -= player.vel
                    player.right = False
                    player.left = False
                    player.up = True
                    player.down = False
                    player.collided = False
                    cn.char = cn.standBack

            #if the player is not moving, reset the walking animation
            else:
                player.right = False
                player.left = False
                player.up = False
                player.down = False
                player.walkCount = 0
                player.collided = False

        if player.gameState != "1":
            if keys[pygame.K_LEFT] and player.x > player.vel + 308 and player.collided == False:
                player.rect.left -= player.vel
                player.x -= player.vel
                player.left = True
                player.right = False
                player.up = False
                player.down = False
                cn.char = cn.standLeft

            elif keys[pygame.K_RIGHT] and player.rect.x < cn.WIDTH - player.rect.width - player.vel  and player.collided == False:
                player.rect.left += player.vel
                player.x += player.vel
                player.right = True
                player.left = False
                player.up = False
                player.down = False
                cn.char = cn.standRight

            elif keys[pygame.K_UP] and player.rect.y > player.vel + 100  and player.collided == False:
                player.rect.top -= player.vel
                player.y -= player.vel
                player.left = False
                player.right = False
                player.up = True
                player.down = False
                cn.char = cn.standBack

            elif keys[pygame.K_DOWN] and player.rect.y < cn.HEIGHT - player.rect.height - player.vel  and player.collided == False:
                player.rect.top += player.vel
                player.y += player.vel
                player.right = False
                player.left = False
                player.up = False
                player.down = True
                cn.char = cn.standForward
            
            elif player.collided == True:
                if cn.char == cn.standLeft:
                    player.x += player.vel
                    player.rect.left += player.vel
                    player.right = True
                    player.left = False
                    player.up = False
                    player.down = False
                    player.collided = False
                    cn.char = cn.standRight
                elif cn.char == cn.standRight:
                    player.x -= player.vel
                    player.rect.left -= player.vel
                    player.right = False
                    player.left = True
                    player.up = False
                    player.down = False
                    player.collided = False
                    cn.char = cn.standLeft
                elif cn.char == cn.standBack:
                    player.rect.top += player.vel
                    player.y += player.vel
                    player.right = False
                    player.left = False
                    player.up = False
                    player.down = True
                    player.collided = False
                    cn.char = cn.standForward
                elif cn.char == cn.standForward:
                    player.rect.top -= player.vel
                    player.y -= player.vel
                    player.right = False
                    player.left = False
                    player.up = True
                    player.down = False
                    player.collided = False
                    cn.char = cn.standBack

            #if the player is not moving, reset the walking animation
            else:
                player.right = False
                player.left = False
                player.up = False
                player.down = False
                player.walkCount = 0
                player.collided = False

    #if X or ESC are pressed, quit the game
    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    if player.gameState == "title":
        if keys[pygame.K_UP] and currentlySelected == "instructions":
            currentlySelected = "play"
        elif keys[pygame.K_DOWN] and currentlySelected == "play":
            currentlySelected = "instructions"
        if keys[pygame.K_RETURN]:
            if currentlySelected == "play":
                player.gameState = "1"
            elif currentlySelected == "instructions":
                player.gameState = "instructions"

    if player.gameState == "instructions" and keys[pygame.K_w]:
        player.gameState = "title"


    if jumbled and player.gameState == "2":
        if keys[pygame.K_b] and typed.count('b') < 1:
            typed.append('b')
        elif keys[pygame.K_o] and typed.count('o') < 2:
            typed.append('o')
        elif keys[pygame.K_k] and typed.count('k') < 1:
            typed.append('k')
        elif keys[pygame.K_s] and typed.count('s') < 1:
            typed.append('s')
        elif keys[pygame.K_h] and typed.count('h') < 1:
            typed.append('h')
        elif keys[pygame.K_e] and typed.count('e') < 1:
            typed.append('e')
        elif keys[pygame.K_l] and typed.count('l') < 1:
            typed.append('l')
        elif keys[pygame.K_f] and typed.count('f') < 1:
            typed.append('f')

        for i in range(len(typed)):
            if typed[i] == 'b' and typedLetters.count('b') < 1:
                typedLetters += typed[i]
            elif typed[i] == 'o' and typedLetters.count('o') < 2:
                typedLetters += typed[i]
            elif typed[i] == 'k' and typedLetters.count('k') < 1:
                typedLetters += typed[i]
            elif typed[i] == 's' and typedLetters.count('s') < 1:
                typedLetters += typed[i]
            elif typed[i] == 'h' and typedLetters.count('h') < 1:
                typedLetters += typed[i]
            elif typed[i] == 'e' and typedLetters.count('e') < 1:
                typedLetters += typed[i]
            elif typed[i] == 'l' and typedLetters.count('l') < 1:
                typedLetters += typed[i]
            elif typed[i] == 'f' and typedLetters.count('f') < 1:
                typedLetters += typed[i]

        correctTyped = []
        if len(typed) == 9:
            for i in range(len(typed)):
                if typed[i] == unscrambled[i]:
                    correctTyped.append("true")
                else: 
                    correctTyped.append("false")
        
            if correctTyped.count("true") == 9:
                foundCode[3] = '!'
                displayLevel2Win = True
                if keys[pygame.K_RETURN]:
                    lvl.gamemode = False
                    displayLevel2Win = False
                    player.gameState = "3"
            elif correctTyped.count("false") > 0:
                if  player.lives == 1:
                    displayLevel2Lose = True
                    if keys[pygame.K_RETURN]:
                        lvl.gamemode = False
                        displayLevel2Lose = False
                        player.gameState = "lose"
                else:
                    player.lives == 1
                    foundCode[3] = '!'
                    displayLevel2Lose = True
                    if keys[pygame.K_RETURN]:                           
                        lvl.gamemode = False
                        displayLevel2Lose = False
                        player.gameState = "3"

    if decode and player.gameState == "3":
        if keys[pygame.K_b] and typedDecode.count('b') < 1:
            typedDecode.append('b')
        elif keys[pygame.K_a] and typedDecode.count('a') < 1:
            typedDecode.append('a')
        elif keys[pygame.K_c] and typedDecode.count('c') < 1:
            typedDecode.append('c')
        elif keys[pygame.K_d] and typedDecode.count('d') < 1:
            typedDecode.append('d')
        elif keys[pygame.K_g] and typedDecode.count('g') < 1:
            typedDecode.append('g')
        elif keys[pygame.K_e] and typedDecode.count('e') < 1:
            typedDecode.append('e')
        elif keys[pygame.K_l] and typedDecode.count('l') < 1:
            typedDecode.append('l')
        elif keys[pygame.K_f] and typedDecode.count('f') < 1:
            typedDecode.append('f')

        for i in range(len(typedDecode)):
            if typedDecode[i] == 'b' and typedLettersDecode.count('b') < 1:
                typedLettersDecode += typedDecode[i]
            elif typedDecode[i] == 'a' and typedLettersDecode.count('a') < 1:
                typedLettersDecode += typedDecode[i]
            elif typedDecode[i] == 'c' and typedLettersDecode.count('c') < 1:
                typedLettersDecode += typedDecode[i]
            elif typedDecode[i] == 'd' and typedLettersDecode.count('d') < 1:
                typedLettersDecode += typedDecode[i]
            elif typedDecode[i] == 'g' and typedLettersDecode.count('g') < 1:
                typedLettersDecode += typedDecode[i]
            elif typedDecode[i] == 'e' and typedLettersDecode.count('e') < 1:
                typedLettersDecode += typedDecode[i]
            elif typedDecode[i] == 'l' and typedLettersDecode.count('l') < 1:
                typedLettersDecode += typedDecode[i]
            elif typedDecode[i] == 'f' and typedLettersDecode.count('f') < 1:
                typedLettersDecode += typedDecode[i]

        correctTypedDecode = []
        if len(typedDecode) == 4:
            for i in range(len(typedDecode)):
                if typedDecode[i] == decoded[i]:
                    correctTypedDecode.append("true")
                else: 
                    correctTypedDecode.append("false")
        
            if correctTypedDecode.count("true") == 4:
                displayWinGame = True
                if keys[pygame.K_RETURN]:
                    lvl.gamemode = False
                    displayWinGame = False
                    player.gameState = "win"
            elif correctTypedDecode.count("false") > 0:
                displayLoseGame = True
                if keys[pygame.K_RETURN]:
                    lvl.gamemode = False
                    displayLoseGame = False
                    player.gameState = "lose"

    if player.gameState == "title":
        cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'titleScreen.jpg'))

    elif player.gameState == "instructions":
        cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'titleScreen.jpg'))

    elif player.gameState == "win":
        cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'titleScreen.jpg'))

    elif player.gameState == "lose":
        cn.bg = pygame.image.load(os.path.join(cn.BG_DIR, 'titleScreen.jpg'))

    #call the game window update function from earlier
    redrawGameWindow()

pygame.quit()
