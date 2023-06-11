import flask
#Print Hello world
print("Hellow world")

# Taking input from a user
teacher = input("Who is your favourite teacher: ")
print("My favourite teacher is", teacher)

age = input("How old are you?: ")
birth_year = 2023 - int(age)
print(birth_year)


costPrice = input("How much is the can of millo? ")
payment = input("your payment: ")
sub = int(costPrice) -int(payment)
print("Balance: " + str(sub))

myprog = " I love programming and i will love fast"
print(myprog.upper())
print(myprog.lower())

#Car speed check
carSpeed = 80
if carSpeed > 120:
    print("Driver you drive too fasr")
elif carSpeed < 50:
    print("Driver! you are driving too slow, this is a highway")
else:
    print("Driver your speed is good")
print("Ready")


#Checking Qualification of candidate for employment
degree = input("What is your highest degree? Bachelor, Master or PhD")
experience = input("How many years of experience do you have?")
if degree == "Master" or degree == "master" or degree == "PhD" or degree == "phd":
    if int(experience)>= 2:
        print("Congratulation! You are accepted for the interview")
    else:
        print("Sorry You don't have enough experience")
else:
    print("Sorry, You don't have the require degree for this job, Better luck next time")


## While loop

i = 0
while i<=5:
    print(i)
    i =i+1


# for loop
temperature = [67, 30, 70, 91]
for item in temperature:
    print(item)

numbers = range(10)
for number in numbers:
    print(number)



#You are a university professor that gave a practice test to its students.
#Your job is to grade your students based on their percentage grade.
#Grading scale :90–100% = A  80–89% = B  70–79% = C  60–69% = D  0–59% = F

percentage_grade = 75

if percentage_grade >= 90:
    print("A")
elif percentage_grade >= 80:
    print("B")
elif percentage_grade >= 70-79:
    print("C")
elif percentage_grade >= 60-69:
    print("D")
else:
    print("F")
