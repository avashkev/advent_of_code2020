import sys
import re

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #ignore 'cid'

def isValidValue(key, value):
    isValid = True
    if key == 'byr': #byr (Birth Year) - four digits; at least 1920 and at most 2002.
        isValid = (int(value) >=1920 and int(value) <= 2002)
    elif key == 'iyr': #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        isValid = (int(value) >= 2010 and int(value) <= 2020)
    elif key == 'eyr': #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        isValid = (int(value) >= 2020 and int(value) <= 2030)
    elif key == 'hgt': #hgt (Height) - a number followed by either cm or in:
        pattern = r'[0-9]{1,}'
        height = int(re.search(pattern, value).group(0))
        if 'cm' in value: #   If cm, the number must be at least 150 and at most 193.
            isValid = height>= 150 and height<= 193
        elif 'in' in value: #   If in, the number must be at least 59 and at most 76.
            isValid = height >= 59 and height <= 76
        else:
            isValid = False
    elif key == 'hcl': #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        pattern = r'^#([a-f0-9]){6}'
        if re.match(pattern,value):
            isValid = True
        else:
            isValid = False
    elif key == 'ecl': #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        eyeColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        isValid = value in eyeColours
    elif key == 'pid': #pid (Passport ID) - a nine-digit number, including leading zeroes.
        if len(value) == 9:
            pattern = r'\d{9}'
            if re.match(pattern,value):
                isValid = True
            else:
                isValid = False
        else:
            isValid = False
   # elif key == 'cid': #cid (Country ID) - ignored, missing or not.
    else:
        print("NOT A VALID KEY")
        isValid = False
    
    return isValid


def isValidPassport(passport):
    isValid = True

    validKeys = 0
    for key in keys:
        if key in passport:
            validKeys += 1
            if not isValidValue(key, passport[key]):
                isValid = False
        else:
            isValid = False

    return isValid
   
if __name__ == "__main__":
    filepath = sys.argv[1]
    file = open(filepath)
    
    array = file.read().split('\n\n')
    pattern = re.compile('(?P<key>[a-z]{3}):(?P<value>[^ \n]+)', re.MULTILINE)
    
    allPassports = []
    for el in array:
        allPassports.append(dict(pattern.findall(el)))
    
    countValid = 0

    for passport in allPassports:
        isValid = isValidPassport(passport)
        if isValid:
            countValid += 1

    print("Valid Passports: ", countValid)