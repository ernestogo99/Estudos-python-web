import time


phones = [f"Phone {i}" for i in range(100000)]

cod_grav = "GRAV001"


start = time.time()
params1 = []
for phone in phones:
    params1.append((cod_grav, phone))
end = time.time()
print(f"For + append: {end - start:.5f} segundos")


start = time.time()
params2 = [(cod_grav, phone) for phone in phones]
end = time.time()
print(f"List comprehension: {end - start:.5f} segundos")
