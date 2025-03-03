from xml.etree import ElementTree

def getChild(root, lvl):
    global rezDict
    lvl += 1
    rezDict[root.attrib['color']] += lvl
    for child in root:
        if child.getchildren():
            getChild(child, lvl)
        else:
            lvl += 1
            rezDict[child.attrib['color']] += lvl
            lvl -= 1

rezDict = {'green':0, 'red':0, 'blue':0}
xmlFile = input()
tree = ElementTree.fromstring(xmlFile)
root = tree
lvl = 0
getChild(root, lvl)
print('{} {} {}'.format(rezDict['red'],rezDict['green'],rezDict['blue']))