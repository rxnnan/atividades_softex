class NumerosComplexos:
    def __init__(self, z, w, v):
        self.z = z
        self.w = w
        self.v = v


print(f"Primeiro Número ")
z1 = float(input("Digite a parte real do primeiro número complexo: "))
z2 = float(input("Digite a parte imaginaria do primeiro número complexo: "))
print(f"Segundo Número")
w1 = float(input("Digite a parte real do segundo número complexo: "))
w2 = float(input("Digite a parte imaginaria do segundo número complexo: "))
print(f"Terceiro Número")
v1 = float(input("Digite a parte real do terceiro número complexo: "))
v2 = float(input("Digite a parte imaginaria do terceiro número complexo: "))

z = complex(z1, z2)
w = complex(w1, w2)
v = complex(v1, v2)

print(f"Os números digitados foram z = {z}, w = {w} e v = {v}")
print(f'A parte real e imaginária de z são, respectivamente: {z1} e {z2}')
print(f'A parte real e imaginária de w são, respectivamente: {w1} e {w2}')
print(f'A parte real e imaginária de v são, respectivamente: {v1} e {v2}')
print('Soma entre os números:')
print(f'z + w = {z+w}\nz + v = {z+v}\nw + v = {w+v}\nz + w + v = {z+w+v}')
print('Subtração entre os números:')
print(f'z - w = {z-w}\nz - v = {z-v}\nw - v = {w-v}\nz - w - v = {z-w-v}')
print(f'Produto entre os números:')
print(f'z * w = {z*w}\nz * v = {z*v}\nw * v = {w*v}\nz * w * v = {z*w*v}')
print(f'Quociente entre os números:')
print(f'z÷w = {z/w}\nz÷v = {z/v}\nw÷v = {w/v}\nw÷z = {w/z}\nv÷z = {v/z}\nv÷w = {v/w}\nz÷w÷v = {z/w/v}\nw÷z÷v = {w/z/v}\nv÷z÷w = {v/z/w}\n')
# Note que na divisão a comutatividade não é válida.
# Já nas outras operações básicas a comutatividade é sempre válida.
