import re

#input file
inputFile = open('day2-input.txt','r')

passwords = []

countOne = 0
countTwo = 0

for line in inputFile.readlines():
    passwords.append(line.split(' '))


for i in passwords:
    policy = i[0].split('-')
    letter = i[1].strip(':')
    pw = i[2].strip('\n')

    countLetter = pw.count(letter)

    if countLetter >= int(policy[0]) and countLetter <= int(policy[1]):
        countOne += 1
    
    if (pw[int(policy[0])-1] == letter) is not (pw[int(policy[1])-1] == letter):
        countTwo += 1


print(countOne)
print(countTwo)


inputFile.close()