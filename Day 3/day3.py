text = open('input.txt', 'r')

forest = text.readlines()

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
#slopes = [[1,2]]
treeProduct = 1

for slope in slopes:
    right = slope[0]
    down = slope[1]

    pos = right
    treeCount = 0

    rowCount = 1
    downCounter = 0

    print("Slope: ",right,",",down)
    for line in forest:
        line = line.strip('\n')
    # print("Position: ", rowCount, ", ", pos)

        if rowCount > 1 and downCounter == down:
            #print(rowCount, ", ", downCounter)
            if(line[pos] == '#'):
                treeCount += 1
        #        line = line[:pos] + 'X' + line[pos+1:]
        #        print(line)
        #        line = line[:pos] + '#' + line[pos+1:]
        #    else:
        #        line = line[:pos] + '0' + line[pos+1:]
        #        print(line)
        #        line = line[:pos] + '.' + line[pos+1:]

            pos += right
            if pos >= len(line):
                pos -= len(line)
    #    else:
    #        print(line)

        rowCount +=1
        downCounter +=1
        if downCounter > down:
            downCounter = 1
    print("Total Trees: ", treeCount, "\n")
    treeProduct *= treeCount

print("Total Product: ", treeProduct, "\n")

text.close()