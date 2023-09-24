import os

text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

num_char=list(map(len,["How", "I", "want", "a", "drink","alcoholic","of",
"course","after","the", "heavy","chapters","involving",
"quantum","mechanics","All","of","thy","geometry","Herr","Planck","is",
"fairly","hard"]))

n=int("".join(map(str,num_char)))
print(n)