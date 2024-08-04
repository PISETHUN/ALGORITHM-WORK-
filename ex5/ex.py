user_input = int(input("enter your number"))
user_mesage = ''
if user_input < 0:
    user_mesage = "Negative Number"
else:
    user_mesage = "Positive Number"
print(user_mesage)