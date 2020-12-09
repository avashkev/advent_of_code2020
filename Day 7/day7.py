import sys
import re
import queue

def parseInputFile(array):

    bags = []
    for line in array:
        
        string = re.split('contain |,',line[:-1])

        for s in string:
            if s == string[0]:
                string[0] = s[:-2]
        bags.append(string)

    return bags

def findBags(bags, myBag):
    q = queue.Queue()
    q.put(myBag)

    luggage = []

    while not q.empty():
        item = q.get()
       # print("Item in queue:", item)
        for bag in bags:
           # print("Looking in bag: ", bag)
            for string in bag:
                if string != bag[0] and item in string:
                    q.put(bag[0])
                    if bag[0] not in luggage:
                        luggage.append(bag[0])
    
    print(len(luggage))

def countLug(bags, mybag):
    q = queue.Queue()
    q.put(myBag)

    numBags = 1
    luggage = {}

    while not q.empty():
        item = q.get()
        
        for bag in bags:
            if item in bag[0]:
                n = 0
                for string in bag:
                    if string != bag[0]:
                        if re.search('\d', string):
                            num = int(re.search('\d', string).group())
                            foundBag = re.search('[a-z]+\s[a-z]+', string).group()
                            q.put(foundBag)
                            print("Found", num, foundBag, "bag(s) in", item)
                        


if __name__ == "__main__":
    filepath = sys.argv[1]
    file = open(filepath, 'r')

    array = file.read().split('\n')

    bags = parseInputFile(array)

    myBag = 'shiny gold'

    findBags(bags, myBag) #part 1
    countLug(bags, myBag) #part 2