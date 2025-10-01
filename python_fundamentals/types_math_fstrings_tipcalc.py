print(int("1234") + int("1234"))

#we can convert data into
int()
float()
str()
bool()


name_of_user = (input("Enter your name"))
len_of_name = len(name_of_user)
print("Numbers of letter in your name:" + str(len_of_name))

print(6 / 3) #prints 2.0 which is a float
print(6 // 3)#prints 2 which is an int
print(2 ** 8)#2 power 8


#PEMDAS
#()
#**
#*
#/
#+
#-

bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi, 2))


#tip calculator
print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? "))  # Convert input to float
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15 "))  # Convert to int
num_people = int(input("How many people will split the bill? "))  # Convert to int

tip_amount = total_bill * tip_percentage / 100  # Calculate tip amount
total_amount = total_bill + tip_amount  # Total bill including tip
amount_per_person = total_amount / num_people  # Divide total among people

print(f"Each person should pay: ${amount_per_person:.2f}")  # Print rounded to 2 decimal places




