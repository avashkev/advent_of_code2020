import sys

def calcRow(boardingPass, minNum, maxNum, position):
    middle = (minNum + maxNum) // 2

    if position == 6:
        if boardingPass[position] == 'F':
            return minNum
        elif boardingPass[position] == 'B':
            return maxNum

    #calculate Row
    # F means lower Half (front)
    # B means upper Half (back)
    if boardingPass[position] == 'F':
       # print("Boarding Pass Position (F): ", boardingPass[position], minNum, middle)
        return calcRow(boardingPass, minNum, middle, position+1)
    elif boardingPass[position] == 'B':
      #  print("Boarding Pass Position (B): ", boardingPass[position], middle+1, maxNum)
        return calcRow(boardingPass, middle+1, maxNum, position+1)

def calcCol(boardingPass, minNum, maxNum, position):
    middle = (minNum + maxNum) // 2

    if position == 2:
        if boardingPass[position] == 'L':
            return minNum
        elif boardingPass[position] == 'R':
            return maxNum
    
    #calculate Row
    # L means lower Half (front)
    # R means upper Half (back)
    if boardingPass[position] == 'L':
       # print("Boarding Pass Position (L): ", boardingPass[position], minNum, middle)
        return calcCol(boardingPass, minNum, middle, position+1)
    elif boardingPass[position] == 'R':
       # print("Boarding Pass Position (R): ", boardingPass[position], middle+1, maxNum)
        return calcCol(boardingPass, middle+1, maxNum, position+1)

def findSeatID(seats):
    seats.sort()
    pos=1
    while pos != len(seats):
        diff = seats[pos] - seats[pos-1]
        if diff == 2:
            return seats[pos]-1
        pos += 1
    return 0

if __name__ == "__main__":
    filepath = sys.argv[1]
    file = open(filepath)
    outputfile = open('output.txt', 'w')

    passes = file.readlines()

    seats = []
    for boardingPass in passes:
        boardingPass = boardingPass.strip('\n')
        row = calcRow(boardingPass[:7], 0, 127, 0)

        col = calcCol(boardingPass[7:], 0, 7, 0)

       # print(row, ",", col)

        seats.append(row*8+col)
    
    seatID = findSeatID(seats)
    outputfile.writelines(str(seats))

    print("seat ID:", seatID)
    print(max("highest seat ID:", seats))
    # print(passes)