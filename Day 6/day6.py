import sys

if __name__ == "__main__":
    filepath = sys.argv[1]
    file = open(filepath)
    
    array = file.read().split('\n\n')

    sumOfUnions = 0
    sumOfIntersections = 0

    answers = []
   
   #parse the input file into a set of answers
    for el in array:
        setAnswer = set()
        answer = []
        for l in el.split('\n'):
            setAnswer = (set(l))
            answer.append(setAnswer)
        answers.append(answer)

    for answer in answers:
        unionSet = {} #part 1

        
        intersectionSet = {} #part 2
        counter = 0

        for answerSet in answer:
            
            unionSet = answerSet.union(unionSet)

            if counter == 0:
                intersectionSet = answerSet
            intersectionSet = answerSet.intersection(intersectionSet)
            counter += 1
       # print(intersectionSet)
        sumOfUnions += len(unionSet)
        sumOfIntersections += len(intersectionSet)
    
    print("Sum of Unions: ", sumOfUnions) #part 1
    print("Sum of Intersections: ", sumOfIntersections) #part 2
