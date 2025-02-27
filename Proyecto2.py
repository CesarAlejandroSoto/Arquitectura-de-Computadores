# Proyecto 2: Aritmética Booleana basada en NAND

# Compuerta NAND: Base de todas las demás operaciones
def NAND(a, b):
    return 1 if not (a and b) else 0

# Compuertas básicas
def NOT(a):
    return NAND(a, a)

def AND(a, b):
    return NOT(NAND(a, b))

def OR(a, b):
    return NAND(NOT(a), NOT(b))

def XOR(a, b):
    return AND(NAND(a, b), OR(a, b))

# Half Adder: Suma dos bits y devuelve (suma, acarreo)
def HalfAdder(a, b):
    suma = XOR(a, b)
    acarreo = AND(a, b)
    return suma, acarreo

# Sumador Completo: Suma tres bits y devuelve (suma, acarreo)
def FullAdder(a, b, acarreo_entrada):
    suma1, acarreo1 = HalfAdder(a, b)
    suma_final, acarreo2 = HalfAdder(suma1, acarreo_entrada)
    acarreo_salida = OR(acarreo1, acarreo2)
    return suma_final, acarreo_salida

# Add16: Suma dos números de 16 bits
def Add16(a, b):
    resultado_suma = [0] * 16
    acarreo = 0
    for i in range(16):
        resultado_suma[i], acarreo = FullAdder(a[i], b[i], acarreo)
    return resultado_suma

# Inc16: Incrementa un número de 16 bits en 1
def Inc16(a):
    uno = [1] + [0] * 15  # Representa el número 1 en 16 bits
    return Add16(a, uno)

# ALU (Unidad Aritmético-Lógica) de Hack
def ALU(x, y, zx, nx, zy, ny, f, no):
    # Aplicar zx y nx a x
    x = [0] * 16 if zx else x
    x = [NOT(bit) for bit in x] if nx else x

    # Aplicar zy y ny a y
    y = [0] * 16 if zy else y
    y = [NOT(bit) for bit in y] if ny else y

    # Operación principal: AND o ADD
    out = Add16(x, y) if f else [AND(x[i], y[i]) for i in range(16)]

    # Aplicar negación final si es necesario
    out = [NOT(bit) for bit in out] if no else out

    # Cálculo de los flags zr y ng
    zr = 1 if all(bit == 0 for bit in out) else 0
    ng = out[0]  # Primer bit indica si el número es negativo en complemento a dos

    return out, zr, ng


