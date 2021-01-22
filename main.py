from __future__ import print_function
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
lettersUp = [
    'A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = [
    ',', '.', '.', '/', ':', '#', '@', '$', '%', '^', '&', '*', '-', '_', '!','?'
]
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
final = []
spacei = []
og = []


def rot(lis):
    for i in lis:
        if i in letters:
            val = letters.index(i)
            if val+13 >= letters.__len__():
                ind = (val+13)-letters.__len__()
                final.append(letters[ind])
            else:
                ind = val+13
                final.append(letters[ind])
        elif i in lettersUp:
            val = lettersUp.index(i)
            if val+13 >= lettersUp.__len__():
                ind = (val+13)-lettersUp.__len__()
                final.append(lettersUp[ind])
            else:
                ind = val+13
                final.append(lettersUp[ind])
        elif i in symbols and i != " ":
            val = symbols.index(i)
            if val+13 >= symbols.__len__():
                ind = (val+13)-symbols.__len__()
                final.append(symbols[ind])
            else:
                ind = val+13
                final.append(symbols[ind])
        elif i == ' ':
            final.append(i)
        elif i in num:
            val = num.index(i)
            if val+13 >= num.__len__():
                ind = (val+13)-num.__len__()
                final.append(num[ind])
            else:
                ind = val+13
                final.append(num[ind])


def split(word):
    return [char for char in word]


def unrot(string):
    lis = split(string)
    for i in lis:
        if i in letters:
            if letters.index(i)-13>=0:
              ind = letters.index(i) - 13
              og.append(letters[ind])
            else:
              ind = letters.__len__() - abs(letters.index(i)-13)
              og.append(letters[ind])
        elif i in lettersUp:
            if lettersUp.index(i)-13>=0:
              ind = lettersUp.index(i) - 13
              og.append(lettersUp[ind])
            else:
              ind = lettersUp.__len__() - abs(lettersUp.index(i)-13)
              og.append(lettersUp[ind])
        elif i in symbols and i != " ":
            if symbols.index(i)-13>=0:
              ind = symbols.index(i) - 13
              og.append(symbols[ind])
            else:
              ind = symbols.__len__() - abs(symbols.index(i)-13)
              og.append(symbols[ind])
        elif i == " ":
            og.append(i)
        elif i in num:
            if num.index(i)-13>=0:
              ind = num.index(i) - 13
              og.append(num[ind])
            else:
              ind = num.__len__() - abs(num.index(i)-13)
              og.append(num[ind])


lista = []
for character in raw_input('String to Encrypt: '):
    lista.append(character)
rot(lista)
c = 0
stry = ''
for element in final:
    stry = stry + str(element)

print(stry)
if raw_input('')=='decrypt':
  unrot(stry)
  print(*og, sep="")