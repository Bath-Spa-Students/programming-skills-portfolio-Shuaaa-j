''' Instructions for practice questions 4.3
Write a python program with nested decision structures that perform the following: If amount1
is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2'''


# Assigning values to the variables
amount_1 = 50
amount_2 = 90

# Declaring the if else condition
if amount_1 > 10:
    if amount_2 < 100:
        if amount_1 > amount_2:
            print("The greater of amount1 and amount2 is:", amount_1)
        else:
            print("The greater of amount1 and amount2 is:", amount_2)
    else:
        print("amount2 is not less than 100")
else:
    print("amount1 is not greater than 10")



