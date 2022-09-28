"""An example of for in syntax."""

names: list[str] = ["Kris", "Kaki", "Ezri", "Marc"]

i : int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

for name in names:
    print(name)