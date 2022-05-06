from logging import root
import random
import xml.etree.ElementTree as RB


def randombiblesection(bible):
    # Add if to see if New (40-66) or Old (1-39) Test
    biblebook = random.randint(1, 66)
    print(biblebook)

    # How do we determine the # of chapters and do a random on this
    chapter = 1

    # How do we determine the # of verses and do a random on this
    verse = 1

    return biblebook, chapter, verse

def biblesection():
    bible = "NIV"
    book, chapter, verse = randombiblesection(bible)
    print(book, chapter, verse)

    # set bible xml file
    if bible == "NIV":
        file="Bible_English_TNIV.xml"        
    else:
        print("No Bible")

    tree = RB.parse(file)
    root = tree.getroot()
    print(f'{root[book].attrib["bname"]}  {chapter}:{verse}')
    print(root[book][chapter][verse].text)



if __name__ == '__main__':
    biblesection()
