phrase1 = str(input("First phrase:"))
phrase2 = str(input("Second phrase:"))
if set(phrase1) == set(phrase2) and len(phrase1) == len(phrase2):
    print("Anagrams")
else:
    print("No")