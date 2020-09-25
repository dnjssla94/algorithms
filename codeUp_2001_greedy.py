
p1 = int(input())
p2 = int(input())
p3 = int(input())
d1 = int(input())
d2 = int(input())

pastas = [p1, p2, p3]
drinks = [d1, d2]
sorted_pastas = sorted(pastas)
sorted_drinks = sorted(drinks)

total = (sorted_pastas[0] + sorted_drinks[0])*1.1

print("%.1f"%total)