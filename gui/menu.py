'''
GUI functions for GUI based tic-tac-toe
Date: 04.08.2019
'''

from gui.variables import *
from gui.constants import *
import pygame
import time
import winsound
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def drawBkg(screen):
    global THEME
    global BACKGROUND
    global BG_IMAGE
    t = THEME[0]
    bg = resource_path(BACKGROUND[t])
    bg = pygame.image.load(bg)
    BG_IMAGE = pygame.transform.scale(bg, (Twidth, Theight))
    screen.blit(BG_IMAGE, (0,0))

def drawMenu():
    global GREENish
    global BLUEish
    global menu_colour
    global MENU_OPTIONS
    global BORDER_THIN
    global text_colour
    global op_colour
    global MENU_BOXES
    global CYAN_HIGHLIGHT
    global BLACK_HIGHLIGHT
    MENU_BOXES = []
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render('Menu', False, menu_colour)
    screen = pygame.display.get_surface()
    #resetBoard(screen)
    drawBkg(screen)
    see_through = pygame.Surface((400,20)).convert_alpha()
    see_through_1 = pygame.Surface((400,400)).convert_alpha()
    see_through.fill(CYAN_HIGHLIGHT)
    see_through_1.fill(BLACK_HIGHLIGHT)
    screen.blit(see_through, (50,30))
    screen.blit(see_through_1, (50,50))
    screen.blit(textsurface,(250,30))
    optext = myfont.render('Menu', False, menu_colour)
    titleBox = pygame.draw.rect(screen,BLUEish,(50, 30,400,20), BORDER_THIN)
    overAllBox = pygame.draw.rect(screen,GREENish,(50, 50,400,400), BORDER_THIN)
    p, q = 200, 60
    for op in MENU_OPTIONS:
        optext = myfont.render(op, False, op_colour)
        screen.blit(optext,(p,q))
        MENU_BOXES.append([p, q])
        q += 50 
    pygame.display.update()

def initMenu():
    screen = pygame.display.get_surface()
    
def checkMouseInBox(box, mousex, mousey):
    if mousex >= box[0] and mousex < box[0] + 200 :
        if mousey >= box[1] and mousey < box[1] + 50 :
            return(True)
    return(False)
    
def updateReq(mousex, mousey):
    global MENU_BOXES
    for box in MENU_BOXES:
        if checkMouseInBox(box, mousex, mousey):
            return True
    return False

def redrawBgd(screen):
    global GREENish
    global BLUEish
    global menu_colour
    global MENU_OPTIONS
    global BORDER_THIN
    global text_colour
    global op_colour
    global MENU_BOXES
    global CYAN_HIGHLIGHT
    global BLACK_HIGHLIGHT
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render('Menu', False, menu_colour)
    screen = pygame.display.get_surface()
    drawBkg(screen)
    see_through = pygame.Surface((400,20)).convert_alpha()
    see_through_1 = pygame.Surface((400,400)).convert_alpha()
    see_through.fill(CYAN_HIGHLIGHT)
    see_through_1.fill(BLACK_HIGHLIGHT)
    screen.blit(see_through, (50,30))
    screen.blit(see_through_1, (50,50))
    optext = myfont.render('Menu', False, menu_colour)
    screen.blit(textsurface,(250,30))
    titleBox = pygame.draw.rect(screen,BLUEish,(50, 30,400,20), BORDER_THIN)
    overAllBox = pygame.draw.rect(screen,GREENish,(50, 50,400,400), BORDER_THIN)
    p, q = 200, 60
    for op in MENU_OPTIONS:
        optext = myfont.render(op, False, op_colour)
        screen.blit(optext,(p,q))
        q += 50 
    pygame.display.update()
    
def highlightBox(screen, i):
    global GREENish
    global MENU_BOXES
    global BORDER_THICK
    global Sound
    screen = pygame.display.get_surface()
    x, y = MENU_BOXES[i][0], MENU_BOXES[i][1]
    P = pygame.draw.rect(screen,GREENish,(x-50, y-5,250,30), BORDER_THICK)
    if Sound[0]:
        winsound.Beep(Sound[2],200)
    pygame.display.update()
    
def NormalBox(screen, i):
    f = 8
    
def menuCheckCursor():
    mousex, mousey = pygame.mouse.get_pos()
    global MENU_BOXES
    global background_colour
    global MENU_OPTIONS
    bx_nr = None
    if updateReq(mousex, mousey):
        i = 0
        inBox = False
        screen = pygame.display.get_surface()
        screen.fill(background_colour)
        redrawBgd(screen)
        for box in MENU_BOXES:
            if checkMouseInBox(box, mousex, mousey):
                inBox = True
                bx_nr = i
                highlightBox(screen, i)
            i += 1
        if (inBox) and pygame.mouse.get_pressed()[0]:
            print("MENU option ", MENU_OPTIONS[bx_nr], " is selected." )
        else:
            bx_nr = None
    return(bx_nr)
            
def togglePlayerChar():
    global player_character
    if player_character[0] == 1:
        player_character[0] = 2
    elif player_character[0] == 2:
        player_character[0] = 1

def updateTheme():
    global THEME
    global BG_IMAGE
    global X_IMAGE
    global O_IMAGE
    global BACKGROUND
    global ICON_X
    global ICON_O
    global Twidth
    global Theight
    global Iwidth
    global Iheight
    bg, i_x, i_o = resource_path(BACKGROUND[THEME[0]]), resource_path(ICON_X[THEME[0]]), resource_path(ICON_O[THEME[0]])
    bg = pygame.image.load(bg)
    BG_IMAGE = pygame.transform.scale(bg, (Twidth, Theight))
    o = pygame.image.load(i_o)
    x = pygame.image.load(i_x)
    O_IMAGE = pygame.transform.scale(o, (Iwidth, Iheight))
    X_IMAGE = pygame.transform.scale(x, (Iwidth, Iheight))

def ChangeTheme():
    global THEME
    current = THEME[0]
    if current+2 == len(THEME):
        THEME[0] = 0
    else:
        THEME[0] = current+1
    updateTheme()
    
def toggleMusic():
    # toggle Music
    global Music
    global MENU_SONG
    Music = not(Music)
    menuSong = resource_path(MENU_SONG[0])
    if Music:
        pygame.mixer.music.load(menuSong)
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()
    print('Music is played: ', str(Music))

def toggleSound():
    # toggle Sound
    global Sound
    Sound[0] = not(Sound[0])
    print('Sound is played : ', str(Sound[0]))
    
def displayCredits():
    # Displaying credits
    global CREDITS
    global BG_IMAGE
    global BLACK_HIGHLIGHT
    global MENU_SONG
    global Music
    menuSong = resource_path(MENU_SONG[1])
    if Music:
        pygame.mixer.music.load(menuSong)
        pygame.mixer.music.play(-1)
    color_line = (49, 150, 100)
    screen = pygame.display.get_surface()
    con_msg = "Click anywhere to continue......."
    screen.blit(BG_IMAGE, (0,0))
    see_through = pygame.Surface((550,550)).convert_alpha()
    see_through.fill(BLACK_HIGHLIGHT)
    screen.blit(see_through, (0,0))
    ms = ""
    step_up = 25
    heights = [400] * len(CREDITS)
    step = 1
    for i in range(0, step_up * (len(CREDITS)+1)):
        k = 0
        screen.blit(BG_IMAGE, (0,0))
        screen.blit(see_through, (0,0))
        for line in CREDITS:
            if step == k + 1:
                break;
            if heights[k] > 10:
                myfont = pygame.font.SysFont('Comic Sans MS', 15)
                textsurface = myfont.render(line, False, text_colour)
                screen.blit(textsurface,(100,heights[k]))
                pygame.display.update()
                heights[k] = heights[k] - 3
            k += 1
        if i % step_up == 0 and i != 0:
            step +=1
        time.sleep(0.1)
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render(con_msg, False, color_line)
    screen.blit(textsurface,(100,450))
    pygame.display.update()

def menuLoop():
    while True:
        event = pygame.event.wait()
        op_selected = menuCheckCursor()
        if(op_selected != None):
            if event.type == pygame.QUIT or op_selected == 6:
                pygame.quit()           # Be interpreter friendly
                sys.exit()
            if op_selected == 1:
                togglePlayerChar()
            if op_selected == 2:
                ChangeTheme()
            if op_selected == 3:
                toggleMusic()
            if op_selected == 4:
                toggleSound()
            if op_selected == 5:
                displayCredits()
            if op_selected == 0:
                return True
        elif op_selected == None and event.type == pygame.QUIT:
            pygame.quit()           # Be interpreter friendly
            sys.exit()
            return False

def displayMenu(): 
    global MENU_SONG
    global Music
    menuSong = resource_path(MENU_SONG[0])
    if Music:
        pygame.mixer.music.load(menuSong)
        pygame.mixer.music.play(-1)
    drawMenu()
    menuLoop()