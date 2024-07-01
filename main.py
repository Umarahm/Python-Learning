# print(3*(3+3)/3-3)
# print(round(8/3,3))
# score=0
# height=1.8
# weight=80                          #Fstring
# isWinning=True
# print(f'your score is {score},your height is {height},your weight is {weight},you are winning is {isWinning}')
print("Welcome to Tip Calculator")
bill_amt=float(input("What was the total bill?"))
tip=int(input('How much tip would ya like to give? 10, 12 or 15?'))
split=int(input("How many people to split the bill?"))
split_bill_amt=float(bill_amt/split)
total_tip=float((split_bill_amt*tip/100)+split_bill_amt)
total_tip=round(total_tip,2)
print(f"Each person should pay: {total_tip}")