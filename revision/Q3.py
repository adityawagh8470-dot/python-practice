text = 'programming'
print(text[:5:])
print(text[::-1])
character = [ ch for ch in text if text.count(ch)>1]
print(character)
new = set(text)
print(new)
print(len(new))
