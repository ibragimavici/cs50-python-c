import sys
import pyfiglet
import random
import requests
import re


response = requests.get("http://www.figlet.org/fontdb.cgi")
content = response.content
x

#now lets find the pattern
pattern = re.compile(re.escape("font=") + "(.*?)" + re.escape(".flf"))
font_names = re.findall(pattern, string_obj)



try:
    if len(sys.argv) == 3:
        #first arg should be -f or --font and second should be the fonts name, make those shit connected to a parameter, we'll inp and print later
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            #check if the font name exists

            fontName = sys.argv[2]
            if fontName in font_names:
                text_inp = input("input: ")
                print(pyfiglet.figlet_format(text_inp, font=fontName))
            else:
                raise ValueError

        else:
            raise ValueError


    elif len(sys.argv) == 1:
        #randomize the font and print it, make them shit connected to a parameter we'll inp and print later
        random_font = random.choice(font_names)
        text_inp = input("input= ")
        print(pyfiglet.figlet_format(text_inp, font=random_font))

    else:
        raise ValueError

except:
    print("Error:")
    sys.exit(1)


