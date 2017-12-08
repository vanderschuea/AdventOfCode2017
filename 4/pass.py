

def palindrome(word, st):
    for w in st:
        if len(word) == len(w):
            for letter in word:
                w = w.replace(letter, '', 1)
        if len(w) == 0:
            return True
    return False


with open("pass.txt") as f:
    content = f.readlines()
content = [x.strip().split() for x in content]
count = 0
for phrase in content:
    unique = set()
    ok = True
    for word in phrase:
        if word in unique or palindrome(word,unique):
            ok = False
            break
        else:
            unique.add(word)
    if ok:
        count += 1
print(count)
