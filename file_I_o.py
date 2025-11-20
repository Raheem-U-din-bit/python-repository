import random
user_input = int(input("enter a number upto 20: "))     

if (user_input > 20 or user_input < 1):
    print("please enter the limited number")
else:
    table = ""

    for i in range(1, 11):
        line = f"{user_input} x {i} = {user_input * i}\n"
        table += line
        print(line, end="")
    with open(f"score/{user_input}.txt", "w") as f:        
         f.write(table)