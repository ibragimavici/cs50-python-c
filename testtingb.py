inp = """7 5
HSHHH"""
splitted = inp.split()
N = int(splitted[0])
K = int(splitted[1])
results = splitted[2]

if K>N:
    raise ValueError

count_H = results.count("H")
count_S = results.count("S")


if count_H > (N/2):
    print("Harun")
elif count_S > (N/2):
    print("Sami")
else:
    print("cilek")

