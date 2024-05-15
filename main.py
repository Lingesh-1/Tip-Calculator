#TIP CALCULATOR

print("Welcome to Tip Calculator!")
t=eval(input("What was the total bill?"))
per=int(input("How much Tip you like to give? 5,3,2?"))
tips= t*(per/100)
split=int(input("How many of you going to split the bill?"))
tb=(t+tips)/split
r=round(tb,2)
print("Each person should pay:",r)
