import time
import os
import sys
import random
import termios

password = "skeletor"

colors = {"black": "[30m",
          "white": "[1;37m",
          "gray": "[37m",
          "red": "[1;31m",
          "green": "[1;32m",
          "blue": "[1;34m",
          "yellow": "[1;33m",
          "magenta": "[1;35m",
          "cyan": "[1;36m",
          "darkgray": "[1;30m",
          "darkred": "[31m",
          "darkgreen": "[32m",
          "darkblue": "[34m",
          "darkyellow": "[33m",
          "darkmagenta": "[35m",
          "darkcyan": "[36m"}


def skroller(text, speed, color = 0):
    term_color(color)
    for i in range(0,len(text)):
        sys.stdout.write(text[i])
        sys.stdout.flush()
        time.sleep(random.random()/speed)
    term_color()
    return

def dots(n):
    for i in range(0, n):
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()
    return

def term_color(color = 0):
    if color not in colors:
        esc = "\033[0m"
    else:
        esc = "\033" + colors[color]
    sys.stdout.write(esc);


while(1):
    try:
        term_color()
        os.system("clear")
        input("Press enter to load OS!")
        os.system("clear")
        skroller(
        '       d8888  .d8888b.  888             .d88888b.   .d8888b.  \n' +
        '      d88888 d88P  Y88b 888            d88P" "Y88b d88P  Y88b \n' +
        '     d88P888 Y88b.      888            888     888 Y88b.      \n' +
        '    d88P 888  "Y888b.   888888 888d888 888     888  "Y888b.   \n' +
        '   d88P  888     "Y88b. 888    888P"   888     888     "Y88b. \n' +
        '  d88P   888       "888 888    888     888     888       "888 \n' +
        ' d8888888888 Y88b  d88P Y88b.  888     Y88b. .d88P Y88b  d88P \n' +
        'd88P     888  "Y8888P"   "Y888 888      "Y88888P"   "Y8888P"\n\n', 64, "darkgreen");
        time.sleep(1);

        while(1):
            termios.tcflush(sys.stdin, termios.TCIOFLUSH) #tyhjennetään buffer estääkseen password fail loopin jos joku tymä hakkaa enter
            passtry = input("Password: ")
            skroller("\nChecking password ", 40)
            dots(3)
            if passtry == password:
                skroller(" Success!\n\n", 4, "green")
                skroller("Checking for errors ", 4)
                dots(5)
                skroller("\nERROR:\n", 64, "darkred")
                skroller("Keyboard not found\nMouse not found\nMonitor not found\nHard disk not found\nLohja not found\nSystem fan is spinning backwards\nSystem temperature over the limit\n", 64, "darkred")
                skroller("\nReceiving message from Headquarters!\nMessage contents:\nUusia tietoja vastaanotettu. OK20:ssä tapahtuu. Muistakaa tämä salasana:\ngolden scorpion\n", 32, "darkcyan")
                skroller("This laptop will self destruct in 45 seconds", 6)
                dots(45)
                skroller("\nERROR:\n", 64, "darkred")
                skroller("Detonator not found\n", 64, "darkred")
                skroller("Kernel panic!", 64)
                time.sleep(1)
                break;
            else:
                skroller(" Fail!\n\n", 4, "red")
            
    except:
        KeyboardInterrupt

