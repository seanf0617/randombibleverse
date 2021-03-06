import random
import xml.etree.ElementTree as RB


def randombiblebook(test):
    # Add if to see if New (40-66) or Old (1-39) Test
    biblebook = random.randint(0, 65)

    return biblebook


def randombiblechap(maxchap):
    # How do we determine the # of chapters and do a random on this
    chapter = random.randint(0, maxchap-1)

    return chapter

def randombiblecverse(maxverse):
    # How do we determine the # of verses and do a random on this
    verse = random.randint(0, maxverse-1)

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
    
    for childchap in root[book][chapter]:
        maxverse = childchap.attrib['vnumber']
    verse = randombiblecverse(int(maxverse))

    print(f'{root[book].attrib["bname"]}  {chapter+1}:{verse+1}')
    print(root[book][chapter][verse].text)


if __name__ == '__main__':
    biblesection()
