
# calculate weighted grade of labs

def calcLabs(labGrade:int) -> int:

    numberOfLabs = labGrade

    # if greater than 6, then we automatically give them 100% for this part


    if numberOfLabs >= 6:
        
        return 20
    
    else:

        return (20/6) * numberOfLabs


    

# calculate weighted grade of quizzes

def calcQuiz(quizGrade:int) -> int:

    numberOfQuiz = quizGrade

    # if greater than 6, then we automatically give them 100% for this part

    if numberOfQuiz >= 6:
        
        return 15
    
    else:
        
        return (15/6) * numberOfQuiz


# calculate weighted grade of assignments

def calcAssignment(assignmentGrade:int) -> int:
    
    assignmentCount = 0
    
    assignmentGrade = 0

    # loop through and change the assignment number
    
    for assignment in range(4):
        
        assignmentCount += 1

        assignmentGrade += int(input("Enter grade for Assignment " + str(assignmentCount) + ": "))


    # take the average of 4 assignments
    
    assignmentGrade /= 4

    # total is worth 16%, or .16

    assignmentGrade *= .16


    return assignmentGrade


# calculate weighted grade of midterms

def calcMidTerm(midtermGrade:int) -> int:

    midtermCount = 0

    # loop to change the midterm number

    for midterm in range(2):
        
        midtermCount += 1

        midtermGrade += int(input("Enter grade for Midterm " + str(midtermCount) + ": "))

    # take the average of 2 midterms
    
    midtermGrade /= 2

    # midterm worth 25%, or .25
    
    midtermGrade *= .25

    return midtermGrade


# calculate weighted grade of final exams

def calcFinalExam(examGrade:int) -> int:
    
    examGrade = int(input("Enter grade for Final Exam: "))

    # final worth 18%, or .18

    examGrade *= .18

    return examGrade



# calculate weighted grade of prep tests

def calcPrep(prepGrade:int) -> int:
    prepGrade = int(input("Enter grade for Midterms and Final Preparation: "))

    # prep is worth 6%, or .06
 
    prepGrade *= .06

    return prepGrade
    
# asks for number of labs and quizzes separately

numLabs = int(input("Enter the number of labs completed: "))
numQuiz = int(input("Enter the number of quizzes completed: "))


# adds all grades together into 1 variable

finalGrade = calcLabs(numLabs) + calcQuiz(numQuiz) + calcAssignment(int()) + calcMidTerm(0) + calcFinalExam(0) + calcPrep(0)

# prints out the grade, with 1 decimal
print("Your grade is: " + str( round(finalGrade, 2) )  )

