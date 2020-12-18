import datetime
def addition():
    num1=int(input("Enter the 1st number to add :"))
    num2=int(input("enter the 2nd number to add :"))
    print("the addition of the two number is :",num1+num2)
def substraction():
    num1=int(input("enter the 1st number :"))
    num2=int(input("Enter the 2nd number :"))
    print("The substraction of the two number is :",num1-num2)
def multiplication():
    num1=int(input("Enter the 1st number :"))
    num2=int(input("Enter the 2nd number:"))
    print("The multiplication is :",num1*num2)
def division():
    num1=int(input("Enter the 1st number :"))
    num2 = int(input("Enter the 2nd number :"))
    print("the division is :",num1/num2)
def percentage():
    num1=int(input("Enter the number :"))
    num2=int(input("Enter the percentage you want to calculate:"))
    print("the percentage of the number is:",num1*(num2/100))

def celcious_to_farenhight ():
    celcious= float(input("Enter the temparture in celcious :"))
    print("Temparature in farenhight :",(celcious*9/5)+32)
def farenhight_to_celcious():
    farenhight= float(input("Enter the temparature in farenhight :"))
    print("temparature in celcious :",(farenhight-32)*5/9)
def kg_to_pound():
     kg=float(input("Enter weight in kg to convert into pound :"))
     print("weight in pound :",kg*2.2046)
def pound_to_kg():
     pound=float(input("Enter weight in pound to convert into kg :"))
     print("weight in kg :",pound*0.453592)
def rupees_to_dollar():
    rupees=float(input("enter the Rupees :"))
    print ("dollar=",rupees/64)
def dollar_to_rupees():
    dollar=float(input("Enter the dollar:"))
    print("rupees=",dollar*64)
def feet_to_cm():
    feet=float(input("Enter the hight in feet"))
    print("hight in cm=",(feet/3.26)*100)
def cm_to_feet():
    cm=float(input("Enter the hight in cm"))
    print("hight in feet=",0.0328*cm)


def calculator():
    print("What do you want to do ? \n 1.Addition \n 2.substraction \n 3.multiplication \n 4.Division \n 5.percentage")

    choice = int(input("Please enter your choice :"))
    if choice == 1:
        addition()
    elif choice == 2:
        substraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        percentage()
    else:
        print("You have entered an invalid input")

print("what do you want to do ?")
print("1.calculator \n 2.celcious to farenhight \n 3. kg to pound \n 4. rupees and dollar \n 5.feet and cm \n 6. age")
first_choice= int(input("Please enter your choice :"))

if first_choice == 1:
    calculator()
elif first_choice == 2:
    print("What do you want to do ? \n 1. celcious to farenhight \n 2. farenhight to celcious  ")
    choice = int(input("Please enter your choice :"))
    if choice == 1:
        celcious_to_farenhight()
    elif choice == 2:
        farenhight_to_celcious()
elif first_choice == 3:
    print("what do you want to do ? \n 1.kg to pound \n 2. pound to kg ")
    choice = int(input("Please Enter your choice :"))
    if choice == 1:
      kg_to_pound()
    elif choice == 2:
      pound_to_kg()
elif first_choice == 4:
    print("what do you want to do? \n 1.rupees to dollar \n 2. dollar to rupees")
    choice= int(input("Enter your choice :"))
    if choice == 1 :
        rupees_to_dollar()
    elif choice == 2:
        dollar_to_rupees()
elif first_choice == 5:
    print("What do you want to do? \n 1.feet to cm \n 2.cm to feet")
    choice=int(input("Enter your choice :"))
    if choice == 1:
        feet_to_cm()
    elif choice== 2:
        cm_to_feet()
elif first_choice == 6:

    birth_year=int(input("Enter your birth year :"))
    yrs=datetime.datetime.now().year-birth_year
    birth_month=int(input("Enter your birth month :"))
    mth= 12-birth_month
    birth_day=int(input("Enter your birth day :"))
    day= 30-birth_day
    print("you re", yrs,"years",mth,"months",day,"days old" )

else:
    print("please select a valid option :")
