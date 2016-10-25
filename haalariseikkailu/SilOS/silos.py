import time
import pygame
from pygame.locals import *



def ms_to_string(ms):
    m, ms = divmod(ms, 60000)
    s = float(ms) / 1000
    return "%2i:%05.2f"%(m,s)


info_messages = ["Welcome to SilOS. This system is protected by eight-phase authentication",
                 "Are you sure you are ready to proceed? (yes/no)"]

riddles = [
    ("Entering here will take more than mere logic", "this is a mirage"),
    ("Whats your favorite color?", "fuksianpunainen"),
    ("How do you talk with a PSX controller?", "0x01 0x41"),
    ("Hey Chris", "did you drink my water"),
    ("Shoots venom around itself on death", "golden scorpion"),
    ("Kissa", "punaherukkalimonadi"),
    ("Joka vuoro, kortti tuottaa pelaajan valitseman resurssin", "secret warehouse"),
    ("Aina ja kaikkialla", "astrobostek")
]




BLACK = (  0,  0,  0)
RED =   (255,  0,  0)
GREEN = (  0,255,  0)
BLUE =  (  0,  0,255)
WHITE = (255,255,255)

WINSIZE = [1280,720]

font_text = "fonts/PixelCarnageMonoCode.fon"
font_clock = "fonts/Code 7x5.ttf"

def draw_prompt(screen, message):
    textobj = pygame.font.Font(font_text, 10)

    if len(message) != 0:
        pos = ((screen.get_width() / 2) - 350, (screen.get_height() / 2) + 200)
        screen.blit(textobj.render(message, 1, WHITE), pos)

def update_box(input_string, question):

    event = pygame.event.poll()
    if event.type != KEYDOWN:
        draw_prompt(g_screen, question + " : " + input_string[0])
        return None

    key = event.key
    if key == K_BACKSPACE:
        input_string[0] = input_string[0][0:-2] + "_"
    elif key == K_RETURN:
        return input_string[0][0:-1]
    elif key <= 127:
        input_string[0] = input_string[0][0:-1] + chr(key) + "_"
        draw_prompt(g_screen, question + " : " + input_string[0])



g_screen = pygame.display.set_mode(WINSIZE)

def draw_text(text, font, pos, size, color):
    font = pygame.font.Font(font, size)
    img = font.render(text, False, color, BLACK)
    g_screen.blit(img,pos)

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.toggle_fullscreen()

    clock = pygame.time.Clock()
    input_string = ["_"]
    phase = -1

    while 1:
        if phase == -1:
            counter = 120000
          
            ret = False
            while ret != "yes":
                ret = None
                while ret == None:
                    g_screen.fill(BLACK)
                    input_string = [""]  
                    ret = update_box(input_string, info_messages[0])
                    clock.tick(50)
                    pygame.display.flip() 
                
                ret = None
                while ret != "yes" and ret != "no":
                    g_screen.fill(BLACK)
                    ret = update_box(input_string, info_messages[1])
                    clock.tick(50)
                    pygame.display.flip()
            
            phase += 1
            input_string = ["_"]
        
        ret = update_box(input_string, riddles[phase][0])
        if ret:
            input_string = ["_"]
            guess = ret.lower()

            if guess == riddles[phase][1]:
                phase += 1
                if phase == len(riddles):
                    victory()      

        counter -= clock.tick(50)
        if counter < 0:
            phase = -1
        
        draw_text(ms_to_string(counter), font_clock, [WINSIZE[0]/2-450, 100], 150, RED)
        pygame.display.flip()
        g_screen.fill(BLACK)

def victory(): 
    g_screen.fill(BLACK)
    font = pygame.font.Font(font_clock, 25)
    img = font.render("Missile launch aborted.", False, WHITE, BLACK)
    g_screen.blit(img,(400,300))
    font = pygame.font.Font(font_clock, 50)
    img = font.render("MISSION ACCOMPLISHED!", False, GREEN, BLACK)
    g_screen.blit(img,(220,400))
    pygame.display.flip()
    while 1:
        time.sleep(1)
    sys.exit(0)


if __name__ == "__main__":
	main()

