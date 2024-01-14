import math

cat_a = int(input('Введите первый катет'))
cat_b = int(input('Введите второй катет'))

square = (cat_a * cat_b) / 2

print(square)

hypotenuse = (cat_a**2 + cat_b**2)
print(math.sqrt(hypotenuse))
