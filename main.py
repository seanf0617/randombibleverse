import random
import xml.sax


def randombiblesection(bible):
    # init variablees
    biblebook = 0
    chapter = 0
    verse = 0
    
    # Add if to see if New (40-66) or Old (1-39) Test
    biblebook = randomNumber(1, 66)
    print(biblebook)

    chapter = 1
    verse = 1

    return biblebook, chapter, verse


def randomNumber(low, high):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, between {low} and {high}')  # Press Ctrl+F8 to toggle the breakpoint.
    return random.randint(low, high)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bible = "NIV"
    book, chapter, verse = randombiblesection(bible)
    print(book, chapter, verse)

    # set bible xml file
    if bible == "NIV":
        file="Bible_English_TNIV.xml"        
    else:
        print("No Bible")
