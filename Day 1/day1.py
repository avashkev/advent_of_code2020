#the report that contains the numbers
report = open('day1-input.txt','r')

#array of the numbers
content = report.readlines() 

numbers = []

#the target number that we need to add up to  
target = 2020

# Iterating through the content 
# Of the file 
for line in content: 
    numbers.append(int(line.strip('\n')))

#Two Number hashing
twoNumHash = set()
twoNumProduct = []

for num in numbers:
    inverseNum = target-num
    if(inverseNum in twoNumHash):
        twoNumProduct.append(inverseNum*num)
    twoNumHash.add(num)

print("Two Numbers:")
print(twoNumProduct)

#Three Number hashing
threeNumHash = set()
threeNumProduct = []

for numOne in numbers:
    inverseNumOne = target-numOne
    
    for numTwo in numbers:
        if(numOne != numTwo):
            inverseNumTwo = inverseNumOne-numTwo
            if(inverseNumTwo in threeNumHash):
                print(numOne, "+", numTwo, "+", inverseNumTwo, "=", numOne+numTwo+inverseNumTwo)
                print("Product = ", inverseNumTwo*numOne*numTwo)
                threeNumProduct.append(inverseNumTwo*numOne*numTwo)
            threeNumHash.add(numTwo)
    threeNumHash.add(numOne)
        

print("\nThree Numbers:")
print(threeNumProduct)
report.close()
