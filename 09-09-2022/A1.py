# 1.write a program to convert temperature fahrenheit to celsius and celcius to fahrenheit
# (32°F − 32) × 5/9 = 0°C | (32°C × 9/5) + 32 = 89.6°F

F = int(input("Temperature in F : "))
C = int(input("Temperature in C : "))

F1 = (C * 9/5) + 32
C1 = (F - 32) * 5/9

print(F,'F =', C1, 'C')
print(C,'C =', F1, 'F')


