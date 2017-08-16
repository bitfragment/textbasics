from random import choice

article = ""

bag = article.split()

poem = ""

while len(bag) > 0:
    word = choice(bag)
    poem = poem + word
    poem = poem + " "
    bag.remove(word)

print(poem)
