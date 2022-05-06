import random
import xml.etree.ElementTree as RB


def randombiblebook(test):
    # Add if to see if New (40-66) or Old (1-39) Test
    biblebook = random.randint(1, 66)

    return biblebook


def randombiblechap(maxchap):
    # How do we determine the # of chapters and do a random on this
    chapter = random.randint(1, maxchap)

    return chapter

def randombiblecverse(maxverse):
    # How do we determine the # of verses and do a random on this
    verse = random.randint(1, maxverse)

    return verse


def biblesection():
    bible = "NIV"

    # set bible xml file
    if bible == "NIV":
        file="Bible_English_TNIV.xml"        
    else:
        print("No Bible")

    tree = RB.parse(file)
    root = tree.getroot()

    book = randombiblebook(bible)

    ###  determine the number of Chapters in a given Book
    for childbook in root[book]:
        maxchap = childbook.attrib['cnumber']
    chapter = randombiblechap(int(maxchap))
    
    ###  determine the number of Verses in a given Chapter
    #
    # TRYING TO FIND RANDOM BUG !!!!!!
    #
    print(book,chapter)
    for childchap in root[book][chapter]:
        maxverse = childchap.attrib['vnumber']
        print(maxverse)
    verse = randombiblecverse(int(maxverse))

    print(book, chapter, verse)


    print(f'{root[book].attrib["bname"]}  {chapter}:{verse}')
    print(root[book][chapter][verse].text)


if __name__ == '__main__':
    biblesection()
