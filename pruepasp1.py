# pruebas generales para cada compuerta
print(f"NOT--- {NOT(1)}")
print(f"NAND--- {NAND(1, 1)}")
print(f"AND--- {AND(1, 0)}")
print(f"OR--- {OR(1, 0)}")
print(f"XOR--- {XOR(1, 0)}")
print(f"MUX--- {MUX(0, 1, 0)}")
print(f"DMUX--- {DMUX(1, 0)}")
# Pruebas para las de 16 bits
a16 = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
b16 = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
c16 = [1]*16
d16 = [0]*16
e16 = [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
f16 = [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]
g16 = [1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0]
h16 = [0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1]
print(f"NOT16--- {NOT16(a16)}")
print(f"AND16--- {AND16(a16, b16)}")
print(f"OR16--- {OR16(a16, b16)}")
print(f"MUX16--- {MUX16(a16, b16, 0)}")
print(f"MUX16--- {MUX16(a16, b16, 1)}")
print(f"OR8Way--- {OR8Way([0,0,0,0,0,0,0,1])}")
print(f"MUX4Way16--- {MUX4Way16(a16, b16, c16, d16, [0,0])}")
print(f"MUX8Way16--- {MUX8Way16(a16, b16, c16, d16, e16, f16, g16, h16, [1,1,0])}")
print(f"DMUX4Way--- {DMUX4Way(1, [0,1])}")
print(f"DMUX8Way--- {DMUX8Way(1, [1,0,1])}")