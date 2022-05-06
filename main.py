import random


def randombiblesection():
    # init variablees
    biblebook = 0
    chapter = 0
    verse = 0
    
    # Add if to see if New (40-66) or Old (1-39) Test
    biblebook = randomNumber(1, 66)
    print(biblebook)

    chapter = 999
    verse = 999

    return biblebook, chapter, verse



def randomNumber(low, high):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, between {low} and {high}')  # Press Ctrl+F8 to toggle the breakpoint.
    return random.randint(low, high)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    book, chapter, verse = randombiblesection()
    print(book, chapter, verse)
