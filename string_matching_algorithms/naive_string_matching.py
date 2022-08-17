pattern = "aab"
text = "acaabc"

for s in range(0, (len(text) - len(pattern))):
    if pattern == text[s:s+len(pattern)]:
        print("Valid Shift at ", s)