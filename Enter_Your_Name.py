additionalWords = 'hi '
maxLetterLimit = 27 - len(additionalWords)
def isWord(name):
    if name == '' or len(name) > maxLetterLimit:
        return False

    for i in name:
        if i not in '! 林 a b c d e f g h i j k l m n o p q r s t u v w x y z'.split():
            if i == ' ':
                continue
            return False
    return True

def appendLetterToList(letter, nameList):
    if letter == 'a':
        nameList.append('. . . . .'.split())
        nameList.append('. . 0 0 0'.split())
        nameList.append('. 0 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('. 0 0 . .'.split())
        nameList.append('. . 0 0 0'.split())
    if letter == 'b':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('. 0 0 . 0'.split())
        nameList.append('. . . 0 .'.split())
    if letter == 'c':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
    if letter == 'd':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('. 0 . 0 .'.split())
        nameList.append('. . 0 . .'.split())
    if letter == 'e':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 . 0 . 0'.split())
    if letter == 'f':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . . . .'.split())
    if letter == 'g':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('. . 0 0 .'.split())
        nameList.append('. . 0 . .'.split())
    if letter == 'h':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('. . 0 . .'.split())
        nameList.append('. . 0 . .'.split())
        nameList.append('. . 0 . .'.split())
        nameList.append('0 0 0 0 0'.split())
    if letter == 'i':
        nameList.append('. . . . .'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
    if letter == 'k':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('. . 0 . .'.split())
        nameList.append('. 0 . 0 .'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('. . . . .'.split())
    if letter == 'j':
        nameList.append('. . . . .'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 0 0 0 .'.split())
        nameList.append('0 . . . .'.split())
        nameList.append('0 . . . .'.split())
    if letter == 'l':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('. . . . 0'.split())
        nameList.append('. . . . 0'.split())
        nameList.append('. . . . 0'.split())
        nameList.append('. . . . 0'.split())
    if letter == 'm':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . . . .'.split())
        nameList.append('0 0 0 0 .'.split())
        nameList.append('0 . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
    if letter == 'n':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('. 0 . . .'.split())
        nameList.append('. . 0 . .'.split())
        nameList.append('. . . 0 .'.split())
        nameList.append('0 0 0 0 0'.split())
    if letter == 'o':
        nameList.append('. . . . .'.split())
        nameList.append('. 0 0 0 .'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('. 0 0 0 .'.split())
    if letter == 'p':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('. 0 . . .'.split())
    if letter == 'q':
        nameList.append('. . . . .'.split())
        nameList.append('. 0 . . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 0 0 0 0'.split())
    if letter == 'r':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('0 . 0 . .'.split())
        nameList.append('. 0 . 0 0'.split())
    if letter == 's':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 . 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 . 0 0 0'.split())
    if letter == 't':
        nameList.append('. . . . .'.split())
        nameList.append('0 . . . .'.split())
        nameList.append('0 . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('0 . . . .'.split())
        nameList.append('0 . . . .'.split())
    if letter == 'u':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('. . . . 0'.split())
        nameList.append('. . . . 0'.split())
        nameList.append('. . . . 0'.split())
        nameList.append('0 0 0 0 0'.split())
    if letter == 'v':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 . .'.split())
        nameList.append('. . . 0 .'.split())
        nameList.append('. . . . 0'.split())
        nameList.append('. . . 0 .'.split())
        nameList.append('0 0 0 . .'.split())
    if letter == 'w':
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('. . . 0 .'.split())
        nameList.append('. . 0 . .'.split())
        nameList.append('. . . 0 .'.split())
        nameList.append('0 0 0 0 0'.split())
    if letter == 'x':
        nameList.append('. . . . .'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('. 0 . 0 .'.split())
        nameList.append('. . 0 . .'.split())
        nameList.append('. 0 . 0 .'.split())
        nameList.append('0 . . . 0'.split())
    if letter == 'y':
        nameList.append('. . . . .'.split())
        nameList.append('0 . . . .'.split())
        nameList.append('. 0 . . .'.split())
        nameList.append('. . 0 0 0'.split())
        nameList.append('. 0 . . .'.split())
        nameList.append('0 . . . .'.split())
    if letter == 'z':
        nameList.append('. . . . .'.split())
        nameList.append('0 . . . 0'.split())
        nameList.append('0 . . 0 0'.split())
        nameList.append('0 . 0 . 0'.split())
        nameList.append('0 0 . . 0'.split())
        nameList.append('0 . . . 0'.split())
    if letter == ' ':
        nameList.append('. . . . .'.split())
        nameList.append('. . . . .'.split())
        nameList.append('. . . . .'.split())
        nameList.append('. . . . .'.split())
        nameList.append('. . . . .'.split())
        nameList.append('. . . . .'.split())
    if letter == '林':
        nameList.append('. . . . .'.split())
        nameList.append('. 0 . 0 .'.split())
        nameList.append('. 0 0 . .'.split())
        nameList.append('0 0 0 0 0'.split())
        nameList.append('. 0 0 . .'.split())
        nameList.append('. 0 . 0 .'.split())
    if letter == '!':
        nameList.append('. . . . .'.split())
        nameList.append('. . . . .'.split())
        nameList.append('0 0 0 . 0'.split())
        nameList.append('0 0 0 . 0'.split())
        nameList.append('. . . . .'.split())
        nameList.append('. . . . .'.split())
        return nameList

name = ''
while not isWord(name):
    print('Enter your name.')
    name = input().lower()

if name == 'brian':
    additionalWords = 'welcome back '
    name = 'owner'

name = additionalWords + name
nameList = []

for letter in name:
    appendLetterToList(letter, nameList)

for y in range(5):
    for x in range(len(name) * 6):
        print(nameList[x][y], end='')
    print()
