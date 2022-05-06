from logging import root
import random
import xml.etree.ElementTree as RB


def randombiblesection(bible):
    # Add if to see if New (40-66) or Old (1-39) Test
    biblebook = random.randint(1, 66)
    print(biblebook)

    chapter = 1
    verse = 1

    return biblebook, chapter, verse


if __name__ == '__main__':
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
    print(root)
    print(root[book].attrib)
    print(root[book][chapter][verse].text)
