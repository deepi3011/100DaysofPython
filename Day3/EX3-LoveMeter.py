#You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.

CODE:
//LoveMeter
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
name1=name1.lower()
name2=name2.lower()
#Write your code below this line 👇
Tru_Tot=0
Love_Tot=0
Love_score=0
Tru_Tot=name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")+name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")
Love_Tot=name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")

Love_score = int(str(Tru_Tot) + str(Love_Tot))
# print(Tru_Tot)
# print(Love_Tot)
# print(type(Love_score))

if((Love_score <10)or(Love_score>90)):
    print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif((Love_score>40)and(Love_score<50)):
    print(f"Your score is {Love_score}, you are alright together.")
else:
     print(f"Your score is {Love_score}.")
