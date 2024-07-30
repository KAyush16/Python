'''
banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

'''
def banner_text(text):
    """
     Print a banner with centered text within a specified width.

    This function prints a banner with the given text centered within
    a line of asterisks. If the text is a single asterisk ('*'), it
    prints a line of asterisks with the specified width. If the text
    exceeds the width limit, it prints a warning message.

    :param text: The text to be printed in the banner.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :type text: str
    :raises ValueError: If the text is too long to fit in the specified width.
    """

    screen_width=80 # we can also define width in the function parameter 
    if(len(text)>screen_width-4):
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
    
    if text=="*":
        print("*"*screen_width)
    else:
        centerd_text=text.center(screen_width-4) 
# this part of the function centers the text within a space of 76 characters (screen_width - 4).
        output_string="**{0}**".format(centerd_text) 
#It then formats the centered text by enclosing it with two asterisks (**) on each side and prints it
        print(output_string)
    
banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life....")
banner_text("*")