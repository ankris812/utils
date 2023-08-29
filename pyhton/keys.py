import random

def generate_random_key():
    key = [random.randint(0, 255) for _ in range(6)]
    return " ".join(format(byte, '02X') for byte in key)

num_keys = 100

print(f"Generando {num_keys} claves aleatorias para Mifare Classic:\n")

for i in range(num_keys):
    print(f"Clave {i+1}: {generate_random_key()}")