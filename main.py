import random


def randombiblesection():
    # Add if to see if New or Old Test
    biblebook = randomNumber(1, 66)
    print(book)

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
    # https://bible-api.com/jn 3:16
    # https://www.ph4.org/b4_mobi.php?q=zefania
    print(book, chapter, verse)
