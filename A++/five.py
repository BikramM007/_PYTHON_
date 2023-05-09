A = input("Enter string:")
B = ""
for i in range(1, len(A)+1):
    B = B + A[-i]
print(f"print B value:{B}")
if A == B:
    print("Polindrone")
else:
    print("Not polindrone")