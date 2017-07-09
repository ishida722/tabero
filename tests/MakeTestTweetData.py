import sys,os
sys.path.append(os.getcwd())
from tabero.twapi import Search

search = Search('食べたい', 10)
print(list(search))
