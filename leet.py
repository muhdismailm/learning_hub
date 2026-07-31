s = "abbbabbcaabc"
s1 = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        s1.append(s[i:j])

longest = ""

for sub in s1:
    if len(set(sub)) == len(sub):  # no duplicate characters
        if len(sub) > len(longest):
            longest = sub

print(longest)
print(len(longest))