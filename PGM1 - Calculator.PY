NUM1 = input("Enter your first num:")
OPT = input("enter your operator(+,-,*,/,%) :")
NUM2 = input("Enter your second num:")

NUM1=float(NUM1)
NUM2=float(NUM2)

if OPT == "+" :
    print(NUM1 + NUM2)
elif OPT == "-":
    print(NUM1 - NUM2)
elif OPT == "*":
    print(NUM1 * NUM2)
elif OPT == "/":
    print(NUM1 / NUM2)
elif OPT == "%":
    print(NUM1 % NUM2)
else:
    print("Invalid Operator...")