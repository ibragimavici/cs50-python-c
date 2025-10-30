txt = input("input: ")
txt = txt.translate(str.maketrans("", "", "aeiouAEIOU"))
print("output:", txt)
