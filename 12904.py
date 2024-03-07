S = input()
T = input()

while len(T) > len(S):
    if T.strip()[-1] == "B":
        T = T[:-1]
        T = T[::-1]
    elif T.strip()[-1] == "A":
        T = T[:-1]

if T == S:
    print(1)
else:
    print(0)
