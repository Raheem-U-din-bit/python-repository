class Employee:
    def info(self, name, age):
        self.name = name
        self.age = age

raheem = Employee()
raheem.info("raheem", "19 Years")
print(raheem.name, raheem.age)

elon = Employee()
elon.info("elon", "36 Years")
print(elon.name, elon.age)




























# def tablesfunc(n):
#     table = "" 
#     for i in range(1, 11):
#         table += (f"{n} x {i} = {n * i}\n")

#     with open(f"score/table_{n}.txt", "w") as f:
#              f.write(table)

# for i in range(1, 21):
#     tablesfunc(i)




# table created which you want.

# user_input = int(input("enter a number upto 20: "))     

# if (user_input > 20 or user_input < 1):
#     print("please enter the limited number")
# else:
#     table = ""

#     for i in range(1, 11):
#         line = f"{user_input} x {i} = {user_input * i}\n"
#         table += line
#         print(line, end="")
#     with open(f"score/{user_input}.txt", "w") as f:        
#          f.write(table)