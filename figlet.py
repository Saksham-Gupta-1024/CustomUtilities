import sys
#import figlet function from pyfiglet module
from pyfiglet import Figlet
#import sys module
import sys

#if the second word in the terminal command is not -f or -font, then exit and show an error for invalid usage
if sys.argv[1] not in ["-f", "-font"]:
    sys.exit("Invalid usage")
#define a variable string for the user input
inp: str = input("Input: ")

#activate the figlet() and figlet.getfonts commands in the figlet module
figlet = Figlet()
figlet.getFonts()

#set the figlet font to the one input by the user
figlet.setFont(font = sys.argv[2])

#print the final text
print(figlet.renderText(inp))