from random import choice

lines = []

poem = ""

while len(lines) > 0:
    line = choice(lines)
    poem = poem + line
    poem = poem + "\n"
    lines.remove(line)

print(poem)
