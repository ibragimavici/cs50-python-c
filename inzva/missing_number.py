n = int(input())
the_row = input().split()
total = sum(map(int, the_row))


missing = (n * (n + 1) // 2) - total
print(missing)