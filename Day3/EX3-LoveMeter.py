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
