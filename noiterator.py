list = ["coma","zeta","arroz","casa"]
# tupple = ("coma","zeta","arroz","casa")
# dictionary = {"coma"
#     ,"zeta"
#     ,"arroz"
#     ,"casa"}
# print(next(list))
# print("------")
# print(next(list))
# print("------")
# print(next(list))

#-------commnad fixed------
def cromand(x):
    for i in x:
        yield i 

variable= cromand(list)
print(next(variable))
print(next(variable))
print(next(variable))