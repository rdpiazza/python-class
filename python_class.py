#!runscript

def bottles_lyrics(bottle = 99):
    while bottle > 0:
        print(str(bottle) + bottles_word(bottle) + "of beer on the wall,")

        if bottle < 5:
            print("ALMOST OUT!")
        elif bottle < 10:
            print("RUNNING LOW!")
        elif bottle % 2 == 0:
            print("IT'S EVEN!")
        else:
            print("THAT'S ODD")

        print(str(bottle) + bottles_word(bottle) + "of beer,")
        print("take one down, pass it around,")
        bottle -= 1
        print(str(bottle) + bottles_word(bottle) + "of beer on the wall!\n")
    return None

def bottles_word(bottle):
    if bottle is 1:
        word = " bottle "
    elif bottle is 0:
        word = " empties "
    else:
        word = " bottles "
    
    return word

bottles_lyrics(12)
