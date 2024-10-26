"""
#LOGIN 1.1
#Login basico sin bucles perofunciona

usuario = "lukspilot"
contrasena = "lukspilot@"

user = input("Ingrese usuario: ")
contra = input("Ingrese contraseña: ")

if user == usuario and contra == contrasena:
    print("Sesion Iniciada")
else:
    print("Usuario o contrasña incorrectos, intente nuevamente.")


#LOGIN 1.2
#Aca le sumamos un bucle para que se repita en caso de que el usuario o 
#contraseña sea incorrecto

while True:
    usuario = "lukspilot"
    contrasena = "lukspilot"

    user = input("Ingrese usuario: ")
    contra = input("Ingrese contraseña: ")

    if user == usuario and contra == contrasena:
        print("Sesion Iniciada")
        break
    else:
        print("Usuario o contrasña incorrectos, intente nuevamente.")


#LOGIN 1.3
#Aca agregar numero de intentos (Max 3)
#Cuando pasen los 3 intentos saldra un mensaje de error que diga 
# "Cuenta Bloqueada"

contador = 0
while contador <= 2:
    usuario = "lukspilot"
    contrasena = "lukspilot"

    user = input("Ingrese usuario: ")
    contra = input("Ingrese contraseña: ")

    if user == usuario and contra == contrasena:
        print("Sesion Iniciada")
        break
    else:
        contador = contador + 1
        print("Usuario o contrasña incorrectos")
        continue
if contador >2:
    print("Cuenta Bloqueada")



#LOGIN 1.4
#Aca vamos a pulir un detalle que diga la cantidad de intentos 
# que le quedan al usuario antes de bloquear la cuenta"

intentos = 3
while intentos >0:
    usuario = "lukspilot"
    contrasena = "lukspilot"

    user = input("Ingrese usuario: ")
    contra = input("Ingrese contraseña: ")

    if user == usuario and contra == contrasena:
        print("Sesion Iniciada")
        break
    else:
        intentos -= 1
        print(f'Usuario o contrasña incorrectos, te quedan {intentos} intentos.')

if intentos == 0:
    print("Cuenta Bloqueada")

"""
#LOGIN 1.5
#Aca intentaré que la cobtraseña se vea con asteriscos y no con letras y números.

intentos = 3
while intentos >0:
    usuario = "lukspilot"
    contrasena = "lukspilot"

    user = input("Ingrese usuario: ")
    contra = input("Ingrese contraseña: ")

    if user == usuario and contra == contrasena:
        print("Sesion Iniciada")
        break
    else:
        intentos -= 1
        print(f'Usuario o contrasña incorrectos, te quedan {intentos} intentos.')

if intentos == 0:
    print("Cuenta Bloqueada")