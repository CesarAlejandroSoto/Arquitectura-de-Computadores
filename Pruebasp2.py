###############################################################################

# Pruebas para el Half Adder
pruebas = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1)
]

# Imprimir resultados
print("---------------------------------------------")

print("HalfAdder")
print("\n")
print("| a | b | sum | acarreo |")
print("|---|---|-----|-------|")
for a, b in pruebas:
    suma, acarreo = HalfAdder(a, b)
    print(f"| {a} | {b} |  {suma}  |   {acarreo}   |")

print("---------------------------------------------")
print("\n")

###############################################################################

# Pruebas para el Full Adder
pruebas_full_adder = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]

# Imprimir resultados
print("---------------------------------------------")

print("FullAdder")
print("\n")
print("| a | b | acarreo_entrada | sum | acarreo_salida |")
print("|---|---|-----------------|-----|----------------|")
for a, b, acarreo_entrada in pruebas_full_adder:
    suma_final, acarreo_final = FullAdder(a, b, acarreo_entrada)
    print(f"| {a} | {b} |        {acarreo_entrada}        |  {suma_final}  |        {acarreo_final}        |")

print("---------------------------------------------")
print("\n")

###############################################################################

# Pruebas de la Add16

pruebas_add16 = [
    ([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]),
]

# Imprimir resultados
print("---------------------------------------------")

print("Add16")
print("\n")
print("| a                 | b                 | sum               |")
print("|-------------------|-------------------|-------------------|")
for a, b in pruebas_add16:
    sum_result = Add16(a, b)
    print(f"| {''.join(map(str, a))} | {''.join(map(str, b))} | {''.join(map(str, sum_result))} |")

print("---------------------------------------------")
print("\n")

###############################################################################

# Pruebas para el Inc16
pruebas_inc16 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Imprimir resultados
print("---------------------------------------------")

print("Inc16")
print("\n")
print("| a                 | sum               |")
print("|-------------------|-------------------|")
for a in pruebas_inc16:
    sum_result = Inc16(a)
    print(f"| {''.join(map(str, a))} | {''.join(map(str, sum_result))} |")

print("---------------------------------------------")
print("\n")

###############################################################################

# Definir entradas
x = [0] * 16  # 0000000000000000
y = [1] * 16  # 1111111111111111
zx, nx, zy, ny, f, no = 1, 1, 1, 0, 1, 0  # Flags de control

# Ejecutar la ALU con los valores de prueba
out, zr, ng = ALU(x, y, zx, nx, zy, ny, f, no)

# Mostrar resultados
print("Salida ALU:", "".join(map(str, out)))  # Mostrar como cadena de bits
print("(zr):", zr)
print("(ng):", ng)

def test_ALU():
    test_cases = list(product([0, 1], repeat=6))  # Generar todas las combinaciones de zx, nx, zy, ny, f, no
    x = [0] * 16  # No importa el valor de x y y en la prueba automatizada
    y = [0] * 16

    results = []
    for case in test_cases:
        zx, nx, zy, ny, f, no = case
        out, zr, ng = ALU(x, y, zx, nx, zy, ny, f, no)
        results.append((zx, nx, zy, ny, f, no, out, zr, ng))

    for r in results:
        print(f"zx={r[0]}, nx={r[1]}, zy={r[2]}, ny={r[3]}, f={r[4]}, no={r[5]} -> out={r[6]}, zr={r[7]}, ng={r[8]}")

test_ALU()

###############################################################################