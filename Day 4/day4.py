import sys
import re

keys = ["byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"]
       # "cid"]


#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

def isValidValue(key, value):
    isValid = True
    if key == 'byr':
        isValid = (int(value) >=1920 and int(value) <= 2002)
    elif key == 'iyr':
        isValid = (int(value) >= 2010 and int(value) <= 2020)
    elif key == 'eyr':
        isValid = (int(value) >= 2020 and int(value) <= 2030)
    elif key == 'hgt':
        pattern = r'[0-9]{1,}'
        height = int(re.search(pattern, value).group(0))
        if 'cm' in value:
            #print("Hight: ", height, " cm")
            isValid = height>= 150 and height<= 193
        elif 'in' in value:
            #print("Hight: ", int(re.match(pattern,value)), " in")
            isValid = height >= 59 and height <= 76
        else:
            isValid = False
    elif key == 'hcl':
        pattern = r'^#([a-f0-9]){6}'
        if re.match(pattern,value):
            isValid = True
        else:
            isValid = False
    elif key == 'ecl':
        eyeColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        isValid = value in eyeColours
    elif key == 'pid':
        if len(value) == 9:
            pattern = r'\d{9}'
            print(re.match(pattern,value))
            if re.match(pattern,value):
                isValid = True
            else:
                isValid = False
        else:
            isValid = False
   # elif key == 'cid':

    else:
        print("NOT A VALID KEY")
        isValid = False
    
  #  if isValid:
       # print(key, ": ", value, " is ", isValid)
    return isValid



def isValidPassport(passport):
    isValid = True
    #print(passport)

    validKeys = 0
    for key in keys:
        if key in passport:
            validKeys += 1
            if not isValidValue(key, passport[key]):
                isValid = False
               # print("invalid: ", key, ": ", passport[key])
        else:
            isValid = False
           # print("missing: ", key)

   # if isValid:
       # print(passport, "is ", isValid)
    return isValid
    
def parsePassportData(passportData):
    passports = []

    data = {}
    #pattern = re.compile('(?P<key>[a-z]+):(?P<value>[0-9][a-z]+)')
    counter = 0
    #print("length of passport data: ", len(passportData))
    for el in passportData:
        #print("el: ", el)
        #print("counter: ", counter)
        counter += 1 
        for e in el:
            #print("\te: ", e)
            line = e.strip().split()
            if len(line) == 0:
                passports.append(data)
                data = {}
            else:
                #print("\tline: ", line)
                for l in line:
                    #print("\t\tl:", l)
                    pair = l.split(':')
                    #print("\t\tpair:", pair)
                    key = pair[0]
                    value = pair[1]
                    data[key] = value
                    #print("\t\tdata:", data)
                if counter == len(passportData):
                    passports.append(data)

        
        #print("counter: ", counter)
    
    #for passport in passports:
        #print("passport: ", passport)
    return passports

def parseFile(file):
    blank_line_regex = r"(?:\r?\n\n){2,}"

    with open(file, "r") as inf:
        return [re.split(r"\n\n", line.strip()) for line in inf]

    

if __name__ == "__main__":
    filepath = sys.argv[1]
    array = parseFile(filepath)

    #for ar in array:
    #    print(ar)

    allPassports = parsePassportData(array)

    #print(allPassports)
   # allPassports = [passport1, passport2, passport3]
    
    countValid = 0
    countPassport = 0
    for passport in allPassports:
        countPassport += 1
        isValid = isValidPassport(passport)
        if isValid:
            countValid += 1
            passport = sorted(passport.items())
            print("Passport #", countPassport, passport, " is ", isValid)
        
        
    print("Total Passports: ", countPassport)
    print("Valid Passports: ", countValid)
    





    
