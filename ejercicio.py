email = input("Introduce tu correo electronico: , ")
while email.startswith("@") or email.endswith("@"):
    print("Tu correo electronico no puede empezar ni acabar con @")
    email = input("Introduce tu correo electronico: , ")

while email.count("@")==0:
    print("Tu correo debe tener al menos un @")
    email = input("Introduce tu correo electronico: , ")

print("Tu correo electronico es correcto")