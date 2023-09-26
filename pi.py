import os
import re
#正規表現の実装

text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

textnew=re.findall(r'\b\w+\b',text)
#\bは単語の境界（スペース）　　　\wは英数文字と下線

charnum=list(map(len,textnew))

n=int("".join(map(str,charnum)))
print(n)