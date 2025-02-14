# Script General de la implementación de todas las compuertas partiendo desde la Nand

# Compuerta NAND: Realiza la operación lógica NAND sobre dos entradas.
# Retorna 1 si no es verdad (no a AND b), de lo contrario, retorna 0.
def NAND(a, b):
    return 1 if not (a and b) else 0

# Compuerta NOT: Invierte el valor de la entrada utilizando una NAND.
def NOT(a):
    return NAND(a, a)

# Compuerta AND: Realiza la operación lógica AND utilizando una NOT sobre la salida de una NAND.
def AND(a, b):
    return NOT(NAND(a, b))

# Compuerta OR: Realiza la operación lógica OR utilizando NOT y NAND.
def OR(a, b):
    return NAND(NOT(a), NOT(b))

# Compuerta XOR: Realiza la operación lógica XOR utilizando AND, NAND y OR.
def XOR(a, b):
    return AND(NAND(a, b), OR(a, b))

# Multiplexor (MUX): Selecciona entre dos entradas a y b basándose en la señal de selección (sel).
def MUX(a, b, sel):
    return OR(AND(a, NOT(sel)), AND(b, sel))

# Demultiplexor (DMUX): Distribuye una entrada (inp) en dos salidas dependiendo de la señal de selección (sel).
def DMUX(inp, sel):
    return (AND(inp, NOT(sel)), AND(inp, sel))

# Compuerta NOT16: Invierte cada bit de una lista de 16 bits.
def NOT16(a):
    return [NOT(bit) for bit in a]

# Compuerta AND16: Realiza la operación lógica AND entre cada par de bits de dos listas de 16 bits.
def AND16(a, b):
    return [AND(a[i], b[i]) for i in range(16)]

# Compuerta OR16: Realiza la operación lógica OR entre cada par de bits de dos listas de 16 bits.
def OR16(a, b):
    return [OR(a[i], b[i]) for i in range(16)]

# Multiplexor de 16 bits (MUX16): Selecciona entre las entradas a y b bit a bit, dependiendo de la señal de selección (sel).
def MUX16(a, b, sel):
    return [MUX(a[i], b[i], sel) for i in range(16)]

# Compuerta OR de 8 entradas (OR8Way): Realiza una operación OR entre un conjunto de 8 entradas.
def OR8Way(a):
    return OR(OR(OR(a[0], a[1]), OR(a[2], a[3])), OR(OR(a[4], a[5]), OR(a[6], a[7])))

# Multiplexor de 4 entradas de 16 bits (MUX4Way16): Selecciona entre cuatro entradas de 16 bits en función de las señales de selección (sel).
def MUX4Way16(a, b, c, d, sel):
    return MUX16(MUX16(a, b, sel[0]), MUX16(c, d, sel[0]), sel[1])

# Multiplexor de 8 entradas de 16 bits (MUX8Way16): Selecciona entre ocho entradas de 16 bits en función de las señales de selección (sel).
def MUX8Way16(a, b, c, d, e, f, g, h, sel):
    return MUX16(MUX4Way16(a, b, c, d, sel[:2]), MUX4Way16(e, f, g, h, sel[:2]), sel[2])

# Demultiplexor de 4 entradas (DMUX4Way): Distribuye una entrada de 16 bits en 4 salidas en función de las señales de selección (sel).
def DMUX4Way(inp, sel):
    a, b = DMUX(inp, sel[1])
    a0, a1 = DMUX(a, sel[0])
    b0, b1 = DMUX(b, sel[0])
    return a0, a1, b0, b1

# Demultiplexor de 8 entradas (DMUX8Way): Distribuye una entrada de 16 bits en 8 salidas en función de las señales de selección (sel).
def DMUX8Way(inp, sel):
    a, b = DMUX(inp, sel[2])
    return (*DMUX4Way(a, sel[:2]), *DMUX4Way(b, sel[:2]))



