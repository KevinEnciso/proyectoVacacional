print("Bienvenido al script de prueba")

def prueba (a, b):
    if a and b:
        return True
    elif a or b:
        return True
    else:
        return False

print(prueba(True, True))
print(prueba(True, False))
print(prueba(False, False))