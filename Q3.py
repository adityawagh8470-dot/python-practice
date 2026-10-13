text = "programming"

print(text[:5:])
print(text[::-1])

character = [ch for ch in text if text.count(ch)>1]
print(character)

without_duplicates = set(text)
print(without_duplicates)
print(len(without_duplicates))