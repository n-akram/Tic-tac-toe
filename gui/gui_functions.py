'''
GUI functions for GUI based tic-tac-toe
Date: 03.08.2019
'''

from gui.variables import *
from gui.constants import *
from gui.engine import resetVar
from gui.engine import isSpaceFree
from gui.engine import makeMove
import winsound
import pygame
import time

def getCurentThemedObject():
    global THEME
    global BACKGROUND
    global ICON_X
    global ICON_O
    t = THEME[0]
    #t = 0
    return(BACKGROUND[t], ICON_X[t], ICON_O[t])

def drawTiles(screen):
    global BLUEish
    global BOXES
    global BORDER_THIN
    itol = 0
    for i in range(3):
        jtol = 0
        for j in range(3):
            x = i*100 + 50 + itol
            y = j*100 + 50 + jtol
            pygame.draw.rect(screen,BLUEish,(x, y,100,100), BORDER_THIN)
            jtol += 50
            BOXES.append([x,y])
        itol += 50
    pygame.display.update()

def resetBoard(screen):
    global Twidth
    global Theight
    global BG_IMAGE
    global X_IMAGE
    global O_IMAGE
    resetVar()
    bg, i_x, i_o = getCurentThemedObject()
    bg = pygame.image.load(bg)
    BG_IMAGE = pygame.transform.scale(bg, (Twidth, Theight))
    o = pygame.image.load(i_o)
    x = pygame.image.load(i_x)
    O_IMAGE = pygame.transform.scale(o, (Iwidth, Iheight))
    X_IMAGE = pygame.transform.scale(x, (Iwidth, Iheight))
    screen.blit(BG_IMAGE, (0,0))
    drawTiles(screen)
    pygame.display.update()

def redrawBgd(screen):
    global BG_IMAGE
    screen.blit(BG_IMAGE, (0,0))
    pygame.display.update()

def getPlayerChar():
    global player_character
    return(player_character[player_character[0]])
    
def putPlayerMarker(screen, image, pos):
    global BOXES
    global SCREEN
    screen.blit(image, BOXES[pos])
    pygame.display.update()
    
def RequesMove(box_nr):
    global X_IMAGE
    global O_IMAGE
    global player_character
    global BOARD_CONTENT
    if player_character[0] == 1:
        BOARD_CONTENT = makeMove(box_nr)
        return X_IMAGE
    else:
        BOARD_CONTENT = makeMove(box_nr)
        return O_IMAGE

    
def checkBoxCont(nr):
    global TRANSLATEDORDER
    global BOARD_CONTENT
    global X_IMAGE
    global O_IMAGE
    global player_character
    if BOARD_CONTENT[nr-1] == '':
        return None
    else:
        if BOARD_CONTENT[nr-1] == 'X':
            return X_IMAGE
        else:
            return O_IMAGE

def highlightBox(screen, nr, box_nr):
    global GREENish
    global BOXES
    global BORDER_THICK
    screen = pygame.display.get_surface()
    x, y = BOXES[nr][0], BOXES[nr][1]
    im_old = checkBoxCont(box_nr)
    #global BOARD_CONTENT
    #print('gui', BOARD_CONTENT)
    im = None
    if im_old is None and pygame.mouse.get_pressed()[0]:
        im = RequesMove(box_nr)
        P = pygame.draw.rect(screen,GREENish,(x, y,100,100), BORDER_THICK)
        screen.blit(im, (x,y))
    elif im_old is None:
        P = pygame.draw.rect(screen,GREENish,(x, y,100,100), BORDER_THICK)
    else:
        P = pygame.draw.rect(screen,GREENish,(x, y,100,100), BORDER_THICK)
        screen.blit(im_old, (x,y))
    if Sound[0]:
        winsound.Beep(200,200)
    pygame.display.update()

def NormalBox(screen, nr): 
    global BORDER_THIN
    global BOXES
    global BLUEish
    global TRANSLATEDORDER
    box_nr = TRANSLATEDORDER[nr]
    x, y = BOXES[nr][0], BOXES[nr][1]
    im = None
    im = checkBoxCont(box_nr)
    if im is None:
        P = pygame.draw.rect(screen,BLUEish,(x, y,100,100), BORDER_THIN)
    else:
        P = pygame.draw.rect(screen,BLUEish,(x, y,100,100), BORDER_THIN)
        screen.blit(im, (x,y))
    pygame.display.update()

def updateScreen(screen):
    global BORDER_THIN
    global BOXES
    global BLUEish
    global TRANSLATEDORDER
    for nr in range (0, 9):
        box_nr = TRANSLATEDORDER[nr]
        x, y = BOXES[nr][0], BOXES[nr][1]
        im = None
        im = checkBoxCont(box_nr)
        if im is None:
            P = pygame.draw.rect(screen,BLUEish,(x, y,100,100), BORDER_THIN)
        else:
            P = pygame.draw.rect(screen,BLUEish,(x, y,100,100), BORDER_THIN)
            screen.blit(im, (x,y))
    pygame.display.update()

def checkMouseInBox(box, mousex, mousey):
    if mousex >= box[0] and mousex < box[0] + 100 :
        if mousey >= box[1] and mousey < box[1] + 100 :
            return(True)
    return(False)
    
def updateReq(mousex, mousey):
    global BOXES
    for box in BOXES:
        if checkMouseInBox(box, mousex, mousey):
            return True
    return False
    
def resetVarHere():
    global BOARD_CONTENT
    global BOXES
    BOARD_CONTENT = ['','','','','','','','','']
    BOXES = []
    
def checkCursorPos():
    global BOXES
    global TRANSLATEDORDER
    mousex, mousey = pygame.mouse.get_pos()
    box_nr = None
    if updateReq(mousex, mousey):
        i = 0
        inBox = False
        screen = pygame.display.get_surface()
        screen.fill(background_colour)
        redrawBgd(screen)
        for box in BOXES:
            if checkMouseInBox(box, mousex, mousey):
                inBox = True
                box_nr = TRANSLATEDORDER[i]
                highlightBox(screen, i, box_nr)
            else:
                NormalBox(screen, i)
            i += 1
        if (inBox) and pygame.mouse.get_pressed()[0]:
            print(box_nr, mousex, mousey)
            
def checkEvent(event):
    checkCursorPos()
    return(BOARD_CONTENT)

def displayEnd(STATUS, screen, winner):
    global BG_IMAGE
    global BLACK_HIGHLIGHT
    global GREEN
    global RED
    global CYAN
    global menu_colour
    global WIN_LOSE
    global Music
    msg = 'Click anywhere to continue'
    screen.blit(BG_IMAGE, (0,0))
    see_through = pygame.Surface((550,550)).convert_alpha()
    see_through.fill(BLACK_HIGHLIGHT)
    screen.blit(see_through, (0,0))
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    if winner == 1:
        textsurface = myfont.render(STATUS, False, GREEN)
    elif winner == 2:
        textsurface = myfont.render(STATUS, False, CYAN)
    else:
        textsurface = myfont.render(STATUS, False, RED)
    if Music:
            pygame.mixer.music.load(WIN_LOSE[winner-1])
            pygame.mixer.music.play(0)
    screen.blit(textsurface,(50,250))
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render(msg, False, menu_colour)
    screen.blit(textsurface,(50,400))
    pygame.display.update()
    resetVarHere()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()# Be interpreter friendly
        elif pygame.mouse.get_pressed()[0]:
            return(True)
    
    
def WelcomeAnimation(screen):
    global MENU_SONG
    global Music
    Welcome_message = "Welcome to Tic-Tac-Toe"
    con_msg = "Click anywhere to continue......."
    screen.fill(WHITE)
    color_line = (49, 150, 100)
    if Music:
        pygame.mixer.music.load(MENU_SONG[0])
        pygame.mixer.music.play(-1)
    # start logo animation
    line_length = 1
    for h in range(1, 20):
        for v in range(1, 20):
            pygame.draw.line(screen, color_line, (100, 125), (100+line_length, 125))
            pygame.draw.line(screen, color_line, (100, 250), (100+line_length, 250))
            pygame.draw.line(screen, color_line, (175, 50), (175, 50+line_length))
            pygame.draw.line(screen, color_line, (350, 50), (350, 50+line_length))
            line_length += 1
            if line_length > 300:
                break
            pygame.display.update()
            time.sleep(0.01)
    ms = ""
    for ch in Welcome_message:
        ms = ms + ch
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(ms, False, text_colour)
        screen.blit(textsurface,(100,400))
        pygame.display.update()
        time.sleep(0.01)
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render(con_msg, False, color_line)
    screen.blit(textsurface,(100,450))
    pygame.display.update()