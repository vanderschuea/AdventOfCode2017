

with open("pass.txt") as f:
    content = f.readlines()
content = [x.strip().split() for x in content]
count = 0
for phrase in content:
    unique = set()
    ok = True
    for word in phrase:
        if word in unique:
            ok = False
            break
        else:
            unique.add(word)
    if ok:
        count += 1
print(count)
